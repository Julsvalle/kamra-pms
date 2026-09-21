# Kamra Connect

Optional services for **self-hosted** Kamra, run by the Kamra team. Kamra
works exactly the same without it; no PMS feature is ever locked behind
Connect. It sells things that cost money to run: storage, monitoring and
AI tokens.

Open **Settings → Kamra Connect**.

| | Free | Essentials | Pro |
|---|---|---|---|
| Security and update alerts for your version | ✓ | ✓ | ✓ |
| Uptime monitoring with email alerts | | ✓ | ✓ |
| Encrypted offsite backups | | 14 days | 30 days |
| Area benchmarks (occupancy, ADR) | | | ✓ |
| Kamra AI credits included | | | ✓ |

Prices are on [kamrapms.com/pricing](https://kamrapms.com/pricing/).
Every new install can try Pro free for 14 days.

## Register or link
- **Register free** with the owner's email: this install gets security
  and update advisories and appears in your Connect account.
- **I have a Connect key**: for installs set up by Kamra or a partner.

## What leaves your server
A check-in every hour carries the Kamra and Frappe versions, disk space
and whether the scheduler runs. It never carries guest data. With *Share
anonymous occupancy and ADR* ticked it also sends yesterday's occupancy
percentage and average rate, which are only ever shown as an average of
three or more properties.

## Backups
Every night at 02:30 Kamra takes a full site backup (database and files),
**encrypts it on your server** with your recovery key, and uploads the
ciphertext. Kamra cannot read your backups.

::: danger Keep the recovery key somewhere safe
Settings → Kamra Connect → *Show recovery key*. If the server is lost and
you do not have this key, no one, including Kamra, can restore your data.
:::

To restore: link the new server with the same Connect key, paste the
recovery key, press *Prepare restore* on a backup, then run the `bench
restore` command Settings shows. A restore replaces the site, so a person
runs it, never Kamra on its own.

## Kamra AI credits
*Use Kamra AI here* points this property's Kamra Agent at the Connect AI
gateway, so staff can use it without buying an API key. Pro includes a
monthly allowance; beyond it, usage is paid from your Connect wallet.
