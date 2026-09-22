"""Create the Costa Rica sales demo on a fresh Kamra-only site.

Run with:
    bench --site <site> execute kamra.scripts.seed_cr_demo.execute

The routine is idempotent. It deliberately disables the public playground
reset, keeps Kamra in English, and uses CRC for every hotel-facing amount.
ERPNext is neither required nor installed by this script.
"""

import frappe


def execute():
	from kamra.scripts.configure_cr import execute as configure_cr
	from kamra.scripts.seed_demo import execute as seed_demo

	if not frappe.db.exists("Property", "Hotel Central San José"):
		# seed_demo also fills the restaurant, banquets, operations and demo
		# users. configure_cr immediately converts that catalogue to Costa Rica.
		seed_demo()

	result = configure_cr()
	result["seed"] = "kamra_cr_demo"
	return result
