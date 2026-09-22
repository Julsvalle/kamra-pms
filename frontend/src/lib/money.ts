/*  Currency and tax vocabulary, from the property's localization pack. Loaded
    once per session; Costa Rica defaults prevent stale INR during first paint.
    The last resolved locale is kept in localStorage so screens render with
    the right symbol immediately on reload, before the network answers. */

import { call, getCurrentProperty } from "./api"

interface Locale {
  currency_symbol: string
  locale: string
  currency: string
  tax_label: string
  tax_id_label: string
  tax_rates: number[]
}

let cache: Locale = {
  currency_symbol: "₡",
  locale: "es-CR",
  currency: "CRC",
  tax_label: "IVA",
  tax_id_label: "Cédula jurídica",
  tax_rates: [0, 13],
}

try {
  const saved = JSON.parse(localStorage.getItem("kamra_locale") || "")
  if (saved?.currency === "CRC" && saved.currency_symbol) cache = { ...cache, ...saved }
} catch {
  /* use the Costa Rica demo defaults until the pack resolves */
}

function remember() {
  try {
    localStorage.setItem("kamra_locale", JSON.stringify(cache))
  } catch {
    /* private mode */
  }
}

export function loadLocale(): Promise<Locale> {
  return call<Locale>("kamra.api.property_locale", {
    property: getCurrentProperty(),
  })
    .then((l) => {
      cache = { ...cache, ...l }
      remember()
      return cache
    })
    .catch(() => cache)
}

/** Public pages carry `ui_locale` in their payload - adopt it directly. */
export function adoptUiLocale(ui?: Partial<Locale> | null) {
  if (!ui) return
  cache = {
    ...cache,
    // "" is a valid symbol (generic pack shows bare numbers)
    currency_symbol: ui.currency_symbol ?? cache.currency_symbol,
    locale: ui.locale || cache.locale,
    currency: ui.currency || cache.currency,
    tax_label: ui.tax_label || cache.tax_label,
    tax_id_label: ui.tax_id_label || cache.tax_id_label,
    tax_rates: ui.tax_rates || cache.tax_rates,
  }
  remember()
}

export const locale = () => cache
/** The property's currency symbol, e.g. "₹" or "Rp". */
export const cur = () => cache.currency_symbol
/** The number-formatting locale, e.g. "en-IN" (lakhs) or "id-ID". */
export const moneyLocale = () => cache.locale
export const fmtMoney = (n: unknown) =>
  cache.currency_symbol +
  Number(n ?? 0).toLocaleString(cache.locale, { maximumFractionDigits: 2 })
export const taxRates = () => cache.tax_rates
export const taxLabel = () => cache.tax_label
