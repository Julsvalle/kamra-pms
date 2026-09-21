import { cur, moneyLocale } from "../lib/money"

/** What kamra.public_api.book returns, as the guest pages use it. */
export interface BookResult {
  reservation: string
  amount_after_tax: number
  advance_due: number
  payment_policy: string
  pay_at_hotel: boolean
  pay_url: string | null
  pay_amount: number | null
  pay_error: string | null
  hold_expires_on: string | null
  status: string
}

const money = (n: number) =>
  `${cur()}${Math.round(n || 0).toLocaleString(moneyLocale())}`

function holdTime(iso: string | null) {
  if (!iso) return null
  const d = new Date(iso.replace(" ", "T"))
  return Number.isNaN(d.getTime())
    ? null
    : d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" })
}

/** Confirmation panel after a guest books. When an advance is due and the
 *  property takes money online, the guest pays straight away; the booking
 *  confirms itself when the gateway reports the payment. */
export function BookingDone({ result }: { result: BookResult }) {
  const needsPay = !!result.pay_url && result.status !== "Confirmed"
  const until = holdTime(result.hold_expires_on)

  if (result.status === "Requested")
    return (
      <div className="rounded-xl border border-zinc-200 bg-zinc-50 px-4 py-4 text-zinc-700">
        <p className="text-lg font-semibold">{result.reservation}</p>
        <p className="mt-1 text-sm">
          Request sent. The host will confirm availability and get back to you.
          Total {money(result.amount_after_tax)}.
        </p>
      </div>
    )

  if (needsPay)
    return (
      <div className="space-y-3">
        <div className="rounded-xl border border-amber-200 bg-amber-50 px-4 py-4 text-amber-900">
          <p className="text-lg font-semibold">{result.reservation}</p>
          <p className="mt-1 text-sm">
            Your room is held{until ? ` until ${until}` : ""}. Pay{" "}
            <b>{money(result.pay_amount ?? result.advance_due)}</b> now to confirm.
            {result.payment_policy ? ` ${result.payment_policy}.` : ""}
          </p>
        </div>
        <a
          href={result.pay_url!}
          className="flex w-full items-center justify-center rounded-lg bg-brand-600 px-4 py-3 text-base font-semibold text-white hover:bg-brand-700"
        >
          Pay {money(result.pay_amount ?? result.advance_due)} securely
        </a>
        <p className="text-center text-xs text-zinc-500">
          UPI, cards and netbanking. We've also sent the link to your phone.
        </p>
      </div>
    )

  const owesLater = result.advance_due > 0 && result.status !== "Confirmed"
  return (
    <div className="space-y-3">
      <div className="rounded-xl border border-emerald-200 bg-emerald-50 px-4 py-4 text-emerald-800">
        <p className="text-lg font-semibold">{result.reservation}</p>
        <p className="mt-1 text-sm">
          Total {money(result.amount_after_tax)}
          {owesLater
            ? `. An advance of ${money(result.advance_due)} is due to confirm; the hotel will contact you to collect it.`
            : " - payable at the hotel. We've saved your number; the front desk will reach out before arrival."}
        </p>
      </div>
      {result.pay_error && (
        <p className="text-xs text-zinc-500">{result.pay_error}</p>
      )}
    </div>
  )
}

/** Shown when Razorpay sends the guest back to /book after paying. The
 *  query string is only a hint for the message; the booking itself is
 *  confirmed by the signed webhook, never by this redirect. */
export function PaymentReturnNote({ params }: { params: URLSearchParams }) {
  if (params.get("payment") !== "done") return null
  const res = params.get("reservation")
  const paid = (params.get("razorpay_payment_link_status") || "paid") === "paid"
  return (
    <div
      className={`mx-auto mb-6 max-w-3xl rounded-xl border px-4 py-3 text-sm ${
        paid
          ? "border-emerald-200 bg-emerald-50 text-emerald-800"
          : "border-amber-200 bg-amber-50 text-amber-900"
      }`}
    >
      {paid
        ? `Payment received for booking ${res ?? ""}. Your confirmation will arrive by message shortly.`
        : `Payment for booking ${res ?? ""} was not completed. Your room stays held for a short while; use the link we sent to try again.`}
    </div>
  )
}
