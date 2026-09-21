import { useCallback, useEffect, useState } from "react"
import { call } from "../lib/api"
import { serverError } from "../lib/resource"
import { useAuth } from "../lib/auth"
import { Button } from "./ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card"

const inputCls =
  "w-full rounded-lg border border-zinc-300 bg-white px-3 py-1.5 text-sm " +
  "focus:outline-2 focus:outline-offset-1 focus:outline-brand-600"

const M = "kamra.connect.client."

interface Advisory {
  name: string
  title: string
  severity: "Info" | "Update" | "Security" | "Critical"
  body: string
  action?: string
  published_on?: string
}
interface Status {
  linked: boolean
  hub_url: string
  install: string | null
  owner_email: string | null
  plan: string | null
  plan_expires: string | null
  wallet_balance: number
  monitor_state: string | null
  backup_enabled: boolean
  share_benchmarks: boolean
  last_heartbeat: string | null
  last_backup: string | null
  last_backup_status: string | null
  last_restore: string | null
  has_recovery_key: boolean
  entitlements: Record<string, number | boolean>
  advisories: Advisory[]
  benchmark: {
    area: string
    peers: number
    occupancy: number
    adr: number
    mine: { occupancy: number; adr: number }
  } | null
}
interface Backup {
  name: string
  finished_on: string
  total_bytes: number
  kamra_version: string
}

const sevCls: Record<string, string> = {
  Critical: "border-red-300 bg-red-50 text-red-800",
  Security: "border-amber-300 bg-amber-50 text-amber-900",
  Update: "border-sky-200 bg-sky-50 text-sky-900",
  Info: "border-zinc-200 bg-zinc-50 text-zinc-700",
}

const mb = (n: number) => `${(n / 1024 / 1024).toFixed(1)} MB`

/** Settings → Kamra Connect: link this install to Kamra's hosted services.
 *  Optional. Kamra works the same whether or not it is linked. */
export function ConnectCard({ property }: { property: string }) {
  const { roles } = useAuth()
  const isSysMgr = roles.includes("System Manager") || roles.includes("Administrator")
  const [s, setS] = useState<Status | null>(null)
  const [busy, setBusy] = useState<string | null>(null)
  const [msg, setMsg] = useState<string | null>(null)
  const [email, setEmail] = useState("")
  const [key, setKey] = useState("")
  const [amount, setAmount] = useState("1000")
  const [backups, setBackups] = useState<Backup[] | null>(null)
  const [recovery, setRecovery] = useState<string | null>(null)

  const load = useCallback(() => {
    call<Status>(M + "status").then(setS).catch((e) => setMsg(serverError(e)))
  }, [])
  useEffect(load, [load])

  async function act<T>(label: string, fn: () => Promise<T>, after?: (r: T) => void) {
    setBusy(label)
    setMsg(null)
    try {
      const r = await fn()
      after?.(r)
    } catch (e) {
      setMsg(serverError(e))
    } finally {
      setBusy(null)
    }
  }
  const openUrl = (r: { url: string }) => window.open(r.url, "_blank", "noopener")

  if (!s) return null
  const ent = s.entitlements || {}

  return (
    <Card>
      <CardHeader>
        <CardTitle>Kamra Connect</CardTitle>
        <p className="text-sm text-zinc-500">
          Optional services for self-hosted Kamra: security alerts, uptime monitoring,
          encrypted offsite backups, benchmarks and AI credits. Kamra works the same
          without it; nothing in the PMS is locked.
        </p>
      </CardHeader>
      <CardContent className="space-y-4 text-sm">
        {msg && <p className="rounded-lg bg-red-50 px-3 py-2 text-red-700">{msg}</p>}

        {!s.linked ? (
          <div className="grid gap-4 sm:grid-cols-2">
            <div className="space-y-2 rounded-lg border border-zinc-200 p-3">
              <p className="font-medium text-zinc-800">Register this install, free</p>
              <p className="text-zinc-500">Security and update alerts for your exact version.</p>
              <input className={inputCls} type="email" placeholder="owner@yourhotel.com"
                value={email} onChange={(e) => setEmail(e.target.value)} />
              <Button disabled={!email || !!busy}
                onClick={() => act("register", () => call<Status>(M + "register", { owner_email: email }), setS)}>
                {busy === "register" ? "Registering…" : "Register free"}
              </Button>
            </div>
            <div className="space-y-2 rounded-lg border border-zinc-200 p-3">
              <p className="font-medium text-zinc-800">I have a Connect key</p>
              <p className="text-zinc-500">From Kamra or your implementation partner.</p>
              <input className={inputCls} placeholder="kc_…" value={key}
                onChange={(e) => setKey(e.target.value)} />
              <Button variant="outline" disabled={!key || !!busy}
                onClick={() => act("link", () => call<Status>(M + "link", { connect_key: key }), setS)}>
                {busy === "link" ? "Linking…" : "Link"}
              </Button>
            </div>
          </div>
        ) : (
          <>
            <div className="flex flex-wrap items-center gap-x-6 gap-y-2">
              <span><b>{s.plan}</b>{s.plan_expires ? ` · until ${s.plan_expires}` : ""}</span>
              <span>Install {s.install}</span>
              {ent.monitoring && (
                <span className={s.monitor_state === "Down" ? "text-red-700" : "text-emerald-700"}>
                  Uptime: {s.monitor_state || "checking"}
                </span>
              )}
              <span>Wallet ₹{Math.round(s.wallet_balance).toLocaleString()}</span>
              <span className="text-zinc-400">
                Last check-in {s.last_heartbeat ? s.last_heartbeat.slice(0, 16) : "never"}
              </span>
            </div>

            <div className="flex flex-wrap gap-2">
              {s.plan === "Free" && (
                <Button disabled={!!busy}
                  onClick={() => act("trial", () => call<Status>(M + "start_trial"), setS)}>
                  Start 14-day Pro trial
                </Button>
              )}
              {["Essentials", "Pro"].map((p) => (
                <Button key={p} variant="outline" disabled={!!busy || s.plan === p}
                  onClick={() => act("sub", () => call<{ url: string }>(M + "subscribe", { plan: p }), openUrl)}>
                  {s.plan === p ? `On ${p}` : `Subscribe to ${p}`}
                </Button>
              ))}
              <Button variant="ghost" disabled={!!busy}
                onClick={() => act("refresh", () => call<Status>(M + "refresh"), setS)}>
                Refresh
              </Button>
            </div>

            {s.advisories.length > 0 && (
              <div className="space-y-2">
                <p className="font-medium text-zinc-800">Advisories for your version</p>
                {s.advisories.map((a) => (
                  <div key={a.name} className={`rounded-lg border px-3 py-2 ${sevCls[a.severity] || sevCls.Info}`}>
                    <p className="font-medium">{a.severity}: {a.title}</p>
                    <p className="mt-1 whitespace-pre-line">{a.body}</p>
                    {a.action && <p className="mt-1 font-mono text-xs whitespace-pre-line">{a.action}</p>}
                  </div>
                ))}
              </div>
            )}

            {ent.backups ? (
              <div className="space-y-2 rounded-lg border border-zinc-200 p-3">
                <div className="flex flex-wrap items-center justify-between gap-2">
                  <p className="font-medium text-zinc-800">Encrypted offsite backups</p>
                  <label className="flex items-center gap-2">
                    <input type="checkbox" className="size-4 accent-brand-600" checked={s.backup_enabled}
                      onChange={(e) => act("pref", () => call<Status>(M + "update_preferences",
                        { backup_enabled: e.target.checked ? 1 : 0 }), setS)} />
                    Nightly at 02:30
                  </label>
                </div>
                <p className="text-zinc-500">
                  Kept {String(ent.retention_days)} days. Encrypted on this server before upload;
                  Kamra cannot read them. {s.last_backup_status ? `Last: ${s.last_backup_status}` : "No backup yet."}
                </p>
                <div className="flex flex-wrap gap-2">
                  <Button variant="outline" disabled={!!busy}
                    onClick={() => act("backup", () => call(M + "backup_now"),
                      () => setMsg(null))}>
                    {busy === "backup" ? "Queuing…" : "Back up now"}
                  </Button>
                  <Button variant="ghost" disabled={!!busy}
                    onClick={() => act("list", () => call<Backup[]>(M + "list_backups"), setBackups)}>
                    Show backups
                  </Button>
                  {isSysMgr && (
                    <Button variant="ghost" disabled={!!busy}
                      onClick={() => act("key", () => call<{ recovery_key: string }>(M + "reveal_recovery_key"),
                        (r) => setRecovery(r.recovery_key))}>
                      Show recovery key
                    </Button>
                  )}
                </div>
                {recovery && (
                  <div className="rounded-lg border border-amber-300 bg-amber-50 px-3 py-2 text-amber-900">
                    <p className="font-medium">Store this offline. Without it, no backup can be restored.</p>
                    <code className="mt-1 block select-all break-all text-xs">{recovery}</code>
                  </div>
                )}
                {backups && (
                  <ul className="divide-y divide-zinc-100">
                    {backups.length === 0 && <li className="py-1 text-zinc-500">No backups yet.</li>}
                    {backups.map((b) => (
                      <li key={b.name} className="flex flex-wrap items-center justify-between gap-2 py-1.5">
                        <span>{b.finished_on.slice(0, 16)} · {mb(b.total_bytes)} · v{b.kamra_version}</span>
                        {isSysMgr && (
                          <Button variant="ghost" disabled={!!busy}
                            onClick={() => act("restore", () => call(M + "prepare_restore", { backup: b.name }),
                              () => setMsg(null))}>
                            Prepare restore
                          </Button>
                        )}
                      </li>
                    ))}
                  </ul>
                )}
                {s.last_restore && (
                  <pre className="whitespace-pre-wrap rounded-lg bg-zinc-900 px-3 py-2 text-xs text-zinc-100">{s.last_restore}</pre>
                )}
              </div>
            ) : (
              <p className="text-zinc-500">Offsite backups and uptime monitoring come with Essentials and Pro.</p>
            )}

            <div className="space-y-2 rounded-lg border border-zinc-200 p-3">
              <label className="flex items-center gap-2">
                <input type="checkbox" className="size-4 accent-brand-600" checked={s.share_benchmarks}
                  onChange={(e) => act("pref", () => call<Status>(M + "update_preferences",
                    { share_benchmarks: e.target.checked ? 1 : 0 }), setS)} />
                Share anonymous occupancy and ADR for area benchmarks
              </label>
              {s.benchmark ? (
                <p>
                  Last 30 days: you <b>{s.benchmark.mine.occupancy}%</b> at ADR {Math.round(s.benchmark.mine.adr)};
                  {" "}{s.benchmark.area} average <b>{s.benchmark.occupancy}%</b> at ADR {Math.round(s.benchmark.adr)}
                  {" "}({s.benchmark.peers} other properties).
                </p>
              ) : (
                <p className="text-zinc-500">
                  {ent.benchmarks ? "Benchmarks appear once at least 3 other properties in your area share." : "Benchmarks come with Pro."}
                </p>
              )}
            </div>

            <div className="flex flex-wrap items-end gap-2 rounded-lg border border-zinc-200 p-3">
              <div className="grow">
                <p className="font-medium text-zinc-800">Kamra AI credits</p>
                <p className="text-zinc-500">
                  Use Kamra Agent without an API key of your own.
                  {ent.ai_tokens_month ? ` ${Number(ent.ai_tokens_month).toLocaleString()} tokens a month included; beyond that from your wallet.` : " Paid from your wallet."}
                </p>
              </div>
              <Button variant="outline" disabled={!!busy}
                onClick={() => act("ai", () => call(M + "use_connect_ai", { property }),
                  () => setMsg(null))}>
                Use Kamra AI here
              </Button>
              <input className={`${inputCls} w-28`} type="number" min={500} value={amount}
                onChange={(e) => setAmount(e.target.value)} />
              <Button variant="outline" disabled={!!busy}
                onClick={() => act("topup", () => call<{ url: string }>(M + "topup", { amount: Number(amount) }), openUrl)}>
                Top up wallet
              </Button>
            </div>

            <div className="flex justify-end">
              <Button variant="ghost" disabled={!!busy}
                onClick={() => act("unlink", () => call<Status>(M + "unlink"), setS)}>
                Unlink this install
              </Button>
            </div>
          </>
        )}
      </CardContent>
    </Card>
  )
}
