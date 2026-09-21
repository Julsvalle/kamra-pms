# Online payments (Razorpay)

Kamra takes money online through **each property's own Razorpay
account**: payment links for bills at the desk, and the advance a guest
pays when they book on your website. Money goes straight to the
property's bank account. Kamra never holds it.

## What guests see

With **Settings → Booking page → Payments** set to *Advance percent*,
*Registration fee* or *Full online*, a guest who books on `/book` is
shown **Pay now to confirm**. Their room is held for the hold window
(default 2 hours). When the payment lands, the booking confirms itself
and the advance appears on the folio. No one at the desk has to do
anything.

If the hold runs out before the guest pays, the room goes back on sale.
A payment that arrives after that is **not** applied to a room that may
be gone: it shows in the Activity Log as a late advance so a person can
rebook the guest or refund.

## Set it up

1. **Get a Razorpay account.** No account yet? Use the *Create one free*
   link under **Settings → Payments**. Approval usually takes a day or two.
2. In Razorpay: **Account & Settings → API Keys** → generate a key.
3. In Kamra: **Settings → Payments** → tick *Enabled*, untick *Test mode*,
   paste the **Key ID** and **Key secret**.
4. In Razorpay: **Webhooks → Add** → the URL shown under Settings →
   Payments (`https://<your-site>/api/method/kamra.payments.razorpay_webhook`),
   event **`payment_link.paid`**, and a secret you invent.
5. In Kamra: paste that same secret as **Webhook secret** and save.

::: warning The webhook secret is required for live payments
Kamra refuses unsigned payment notifications once test mode is off, so
no one can mark a bill paid by calling the webhook themselves. Without
the secret, payments still reach your bank but are not posted to folios
automatically.
:::

## Test mode

*Test mode* creates placeholder links and accepts unsigned
notifications, so a demo can walk the whole flow without real money.
Never leave it on for a live property.

## Several properties

Each property has its own Payment Gateway Settings. A group can settle
every property into a different bank account, or reuse one Razorpay
account with the same keys.
