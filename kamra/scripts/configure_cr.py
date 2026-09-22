"""Localize the demo site for Costa Rica.

Run inside the Frappe container with:
PYTHONPATH=/workspace bench --site pms.localhost execute scripts.configure_cr.execute
"""

import frappe
from frappe.utils import add_days, nowdate


PROPERTIES = {
	"Kamra Demo Palace": {
		"name": "Hotel Central San José",
		"legal_name": "Hotel Central San José S.A.",
		"phone": "+506 2222-1000",
		"email": "reservas@hotelcentral.demo",
		"address_line": "Avenida Central, Barrio Amón",
		"city": "San José",
		"state": "San José",
		"pincode": "10101",
		"latitude": 9.9384,
		"longitude": -84.0786,
		"page_slug": "hotel-central-san-jose",
		"showcase_description": "A practical city hotel demo in the heart of San José, Costa Rica.",
		"driving_directions": "From Juan Santamaría International Airport, take General Cañas toward central San José.",
	},
	"Kamra Beach Homestay": {
		"name": "Hotel Playa Tamarindo",
		"legal_name": "Hotel Playa Tamarindo S.A.",
		"phone": "+506 2653-1000",
		"email": "reservas@playatamarindo.demo",
		"address_line": "200 m east of Tamarindo Beach",
		"city": "Tamarindo",
		"state": "Guanacaste",
		"pincode": "50309",
		"latitude": 10.2993,
		"longitude": -85.8371,
		"page_slug": "hotel-playa-tamarindo",
		"showcase_description": "A relaxed Costa Rican beach hotel demo near Playa Tamarindo.",
		"driving_directions": "From Liberia, follow Route 21 and Route 155 toward Tamarindo.",
	},
	"Kamra Lakeside Villa": {
		"name": "Hotel Lago Arenal",
		"legal_name": "Hotel Lago Arenal S.A.",
		"phone": "+506 2694-1000",
		"email": "reservas@lagoarenal.demo",
		"address_line": "Lake Arenal waterfront road",
		"city": "Nuevo Arenal",
		"state": "Guanacaste",
		"pincode": "50807",
		"latitude": 10.5469,
		"longitude": -84.8927,
		"page_slug": "hotel-lago-arenal",
		"showcase_description": "A quiet Costa Rican lake hotel demo with views of Lake Arenal.",
		"driving_directions": "From La Fortuna, follow Route 142 around Lake Arenal toward Nuevo Arenal.",
	},
}


GUESTS = {
	"G-00001": ("Carlos", "Vargas", "+506 7001-1001", "San José"),
	"G-00002": ("María", "Rodríguez", "+506 7001-1002", "Heredia"),
	"G-00003": ("Andrés", "Jiménez", "+506 7001-1003", "Alajuela"),
	"G-00004": ("Sofía", "Mora", "+506 7001-1004", "Cartago"),
	"G-00005": ("Daniel", "Chaves", "+506 7001-1005", "San José"),
	"G-00006": ("Valeria", "Solano", "+506 7001-1006", "Liberia"),
	"G-00007": ("José", "Araya", "+506 7001-1007", "Puntarenas"),
	"G-00008": ("Laura", "Castro", "+506 7001-1008", "Heredia"),
	"G-00009": ("Diego", "Ramírez", "+506 7001-1009", "Escazú"),
	"G-00010": ("Natalia", "Quesada", "+506 7001-1010", "Santa Ana"),
}


DEMO_USER_NAMES = {
	"admin@kamra.local": ("Administración", "Hotel Central"),
	"gm@kamra.local": ("Gabriela", "Mora"),
	"frontdesk@kamra.local": ("Diego", "Ramírez"),
	"revenue@kamra.local": ("Daniela", "Campos"),
	"finance@kamra.local": ("Mauricio", "Brenes"),
	"hk@kamra.local": ("Rosa", "Alvarado"),
}


LOCAL_GUESTS = [
	("Carlos", "Vargas", "San José"),
	("María", "Rodríguez", "Heredia"),
	("Andrés", "Jiménez", "Alajuela"),
	("Sofía", "Mora", "Cartago"),
	("Daniel", "Chaves", "San José"),
	("Valeria", "Solano", "Liberia"),
	("José", "Araya", "Puntarenas"),
	("Laura", "Castro", "Heredia"),
	("Diego", "Ramírez", "Escazú"),
	("Natalia", "Quesada", "Santa Ana"),
	("Ana", "Madrigal", "San José"),
	("Marco", "Cordero", "Alajuela"),
	("Fernanda", "Rojas", "Curridabat"),
	("Esteban", "Alfaro", "Cartago"),
	("Lucía", "Villalobos", "Heredia"),
	("Mauricio", "Brenes", "San Ramón"),
	("Gabriela", "Zúñiga", "Liberia"),
	("Pablo", "Montero", "Jacó"),
	("Daniela", "Campos", "Grecia"),
	("Felipe", "Salazar", "Turrialba"),
]


EXPERIENCE_UPDATES = {
	"Sunrise Safari": (
		"Irazú Volcano Sunrise Tour", 32000,
		"Early transfer to Irazú Volcano with a local guide, breakfast and viewpoints.",
	),
	"Candlelight Romantic Dinner": (
		"Tropical Garden Dinner", 42000,
		"Private garden table with a Costa Rican tasting menu and acoustic music.",
	),
	"Ayurvedic Spa Ritual": (
		"Coffee & Cacao Spa Ritual", 38000,
		"A relaxing treatment inspired by Costa Rican coffee and cacao.",
	),
	"Couple's Spa Retreat": (
		"Couple's Rainforest Spa Retreat", 68000,
		"Side-by-side massage, tropical fruit and locally inspired aromatherapy.",
	),
	"Heritage City Walk": (
		"Historic San José Walking Tour", 18000,
		"Guided walk through Barrio Amón, the National Theatre and Central Market.",
	),
	"Cooking Class with the Chef": (
		"Costa Rican Cooking Class", 28000,
		"Hands-on class featuring gallo pinto, tortillas and seasonal local produce.",
	),
	"Sunset Lake Cruise": (
		"Arenal Sunset Boat Tour", 36000,
		"Sunset cruise on Lake Arenal with local snacks and non-alcoholic drinks.",
	),
	"Airport Transfer (Sedan)": (
		"SJO Airport Transfer", 24000,
		"Private transfer to or from Juan Santamaría International Airport.",
	),
	"Yoga at Dawn": (
		"Sunrise Yoga in the Garden", 12000,
		"Guided morning yoga followed by fresh tropical fruit.",
	),
	"In-Room Floral Turndown": (
		"Tropical Floral Turndown", 26000,
		"Locally sourced tropical flowers and a Costa Rican chocolate welcome amenity.",
	),
}


VENUE_UPDATES = {
	"Grand Ballroom": ("Salón Nacional", 400, 850000),
	"Garden Lawn": ("Jardín Guaria", 250, 475000),
	"Riverside Deck": ("Terraza Arenal", 120, 320000),
	"Boardroom": ("Sala Poás", 20, 95000),
}


MENU_UPDATES = {
	"Silver Veg Buffet": ("Costa Rican Vegetarian Buffet", 18000, "Costa Rican"),
	"Gold Non-Veg Buffet": ("Premium Costa Rican Buffet", 26500, "Costa Rican"),
	"Corporate Working Lunch": ("San José Executive Lunch", 14500, "Costa Rican"),
	"Hi-Tea Package": ("Coffee Break Tico", 7500, "Costa Rican"),
	"Sangeet Cocktail Snacks": ("Tropical Cocktail Bites", 19000, "Costa Rican"),
}


COURSE_DISH_UPDATES = {
	"Aam panna, Jal jeera": "Agua de sapo, fresh cas juice",
	"Paneer tikka, Hara bhara kebab, Corn seekh": "Ceviche de palmito, patacones, corn fritters",
	"Dal makhani, Paneer butter masala, Veg biryani, Mix veg": "Black bean stew, palmito in tomato sauce, arroz con vegetales, picadillo",
	"Naan, Tandoori roti, Jeera rice": "Corn tortillas, artisan bread, cilantro rice",
	"Chaat counter": "Patacones live station",
	"Gulab jamun, Rasmalai, Ice cream": "Tres leches, coconut flan, local ice cream",
	"Paneer tikka, Mushroom galouti": "Ceviche de palmito, stuffed mushrooms",
	"Murgh malai tikka, Fish amritsari, Mutton seekh": "Coffee-rubbed chicken, Pacific fish ceviche, beef skewers",
	"Butter chicken, Rogan josh, Dal makhani, Subz miloni": "Chicken in Lizano-style sauce, braised beef, black bean stew, vegetable picadillo",
	"Tandoor counter, Pasta counter": "Tortilla station, pasta station",
	"Shahi tukda, Kesar phirni, Ice cream": "Coffee flan, rice pudding, local ice cream",
	"Cream of tomato, Sweetcorn": "Roasted tomato, sweet corn",
	"Grilled chicken with herb rice, Penne arrabbiata": "Grilled chicken with cilantro rice, penne arrabbiata",
	"Brownie with vanilla": "Chocolate brownie with vanilla ice cream",
	"Samosa, Veg sandwich, Cocktail idli": "Mini empanadas, vegetable sandwich, cheese tortillas",
	"Mysore pak, Cookies": "Coconut bites, coffee cookies",
	"Masala chai, Filter coffee": "Herbal tea, Tarrazú coffee",
	"Chicken satay, Paneer bruschetta, Mini vada pav": "Chicken skewers, palmito bruschetta, mini patacones",
	"Kebab counter, Pani puri shots": "Skewer station, tropical ceviche shots",
}


DISH_UPDATES = {
	"Paneer Tikka": "Ceviche de Palmito",
	"Hara Bhara Kebab": "Patacones with Bean Dip",
	"Murgh Malai Tikka": "Coffee-Rubbed Chicken Skewer",
	"Fish Amritsari": "Pacific Fish Ceviche",
	"Cream of Tomato Soup": "Roasted Tomato Soup",
	"Sweetcorn Soup": "Sweet Corn Soup",
	"Dal Makhani": "Black Bean Stew",
	"Paneer Butter Masala": "Palmito in Tomato Sauce",
	"Butter Chicken": "Chicken in Lizano-style Sauce",
	"Subz Miloni": "Seasonal Vegetable Picadillo",
	"Veg Biryani": "Arroz con Vegetales",
	"Jeera Rice": "Cilantro Rice",
	"Gulab Jamun": "Tres Leches Cake",
	"Rasmalai": "Coconut Flan",
	"Chaat Counter": "Patacones Live Station",
	"Welcome Drink - Aam Panna": "Welcome Drink - Agua de Sapo",
}


MENU_ITEM_UPDATES = {
	"Masala Dosa": ("Gallo Pinto Breakfast", "Breakfast", 5200),
	"Butter Chicken": ("Casado with Chicken", "Costa Rican", 6500),
	"Paneer Tikka": ("Ceviche de Palmito", "Starters", 4800),
	"Veg Biryani": ("Arroz con Vegetales", "Costa Rican", 5200),
	"Gulab Jamun": ("Tres Leches Cake", "Desserts", 3500),
	"Cold Coffee": ("Costa Rican Cold Brew", "Beverages", 2800),
	"Fresh Lime Soda": ("Limonada con Hierbabuena", "Beverages", 2500),
	"Kingfisher Beer": ("Imperial Beer", "Local Beer", 2200),
}


INGREDIENT_UPDATES = {
	"Paneer": ("Palmito", 4200, "Produce"),
	"Chicken": ("Chicken", 3800, "Meat"),
	"Butter": ("Butter", 5200, "Dairy"),
	"Cream": ("Natilla", 3600, "Dairy"),
	"Tomato": ("Tomato", 1600, "Produce"),
	"Onion": ("Onion", 1200, "Produce"),
	"Basmati Rice": ("Costa Rican Rice", 1250, "Dry Goods"),
	"Mixed Vegetables": ("Seasonal Vegetables", 2400, "Produce"),
	"Dosa Batter": ("Corn Masa", 1800, "Dry Goods"),
	"Potato": ("Potato", 1100, "Produce"),
	"Gulab Jamun Mix": ("Tres Leches Mix", 3600, "Dry Goods"),
	"Sugar": ("Sugar", 950, "Dry Goods"),
	"Milk": ("Milk", 1200, "Dairy"),
	"Coffee Powder": ("Tarrazú Coffee", 7800, "Dry Goods"),
	"Lime": ("Mandarin Lime", 180, "Bar"),
	"Soda": ("Sparkling Water", 850, "Bar"),
	"Kingfisher Bottle": ("Imperial Beer Bottle", 1200, "Bar"),
	"Cooking Oil": ("Vegetable Oil", 2100, "Dry Goods"),
	"Garam Masala": ("Culantro & Spices", 6500, "Dry Goods"),
}


ROOM_RATES = {
	("Hotel Central San José", "STD"): 45000,
	("Hotel Central San José", "DLX"): 65000,
	("Hotel Central San José", "STE"): 95000,
	("Hotel Playa Tamarindo", "GFNA"): 35000,
	("Hotel Playa Tamarindo", "GFNB"): 42000,
	("Hotel Playa Tamarindo", "TFAC"): 55000,
	("Hotel Playa Tamarindo", "UF2R"): 85000,
	("Hotel Lago Arenal", "STD"): 60000,
	("Hotel Lago Arenal", "VILLA"): 220000,
}


def _rename_prefixed_records(doctype, old_property, new_property):
	for old_name in frappe.get_all(
		doctype,
		filters={"property": new_property, "name": ["like", f"{old_property}-%"]},
		pluck="name",
	):
		new_name = new_property + old_name[len(old_property) :]
		if not frappe.db.exists(doctype, new_name):
			frappe.rename_doc(doctype, old_name, new_name, force=True)


def _configure_properties():
	for old_name, values in PROPERTIES.items():
		new_name = values["name"]
		if frappe.db.exists("Property", old_name) and not frappe.db.exists("Property", new_name):
			frappe.rename_doc("Property", old_name, new_name, force=True)

		if not frappe.db.exists("Property", new_name):
			continue

		for doctype in ("Room Type", "Room"):
			_rename_prefixed_records(doctype, old_name, new_name)

		doc = frappe.get_doc("Property", new_name)
		for field, value in values.items():
			if field != "name":
				setattr(doc, field, value)
		doc.property_name = new_name
		doc.country = "Costa Rica"
		doc.timezone = "America/Costa_Rica"
		doc.currency = "CRC"
		doc.locale = "es-CR"
		doc.gstin = ""
		doc.gst_mode = "Fixed"
		doc.gst_rate_low = 13
		doc.gst_rate_high = 13
		doc.rates_include_tax = 1
		doc.security_deposit_amount = 50000
		doc.business_date = nowdate()
		doc.booking_engine_enabled = 1
		doc.booking_payment_mode = "Pay at hotel"
		doc.free_cancel_days = 2
		doc.cancellation_fee = "First Night"
		doc.no_show_charge = "First Night"
		if new_name == "Hotel Central San José":
			doc.website = "https://hotelcentral.demo"
			doc.star_category = "Boutique"
			doc.property_amenities = (
				"Wi-Fi, breakfast, restaurant, bar, meeting rooms, airport transfers"
			)
			doc.house_rules = (
				"Check-in 14:00, check-out 11:00. Quiet hours 22:00-07:00. "
				"A valid ID is required for every adult guest."
			)
			doc.pets_policy = "Small pets are welcome in selected rooms with prior notice."
			doc.children_policy = "Children under 6 stay free when sharing with adults."
			doc.extra_bed_policy = "Rollaway bed ₡12,000 per night, subject to availability."
			doc.meta_title = "Hotel Central San José - Costa Rica demo hotel"
			doc.meta_description = (
				"Boutique city hotel demo in Barrio Amón with rooms, restaurant and events."
			)
		doc.save(ignore_permissions=True)

	for room_type in frappe.get_all(
		"Room Type", fields=["name", "property", "room_type_code"]
	):
		price = ROOM_RATES.get((room_type.property, room_type.room_type_code))
		if price is None:
			continue
		doc = frappe.get_doc("Room Type", room_type.name)
		doc.base_price = price
		doc.extra_adult_price = round(price * 0.25)
		doc.extra_bed_price = round(price * 0.20)
		doc.child_price = round(price * 0.12)
		doc.tax_percent = 13
		doc.save(ignore_permissions=True)


def _configure_guests():
	guests = frappe.get_all("Guest", pluck="name", order_by="creation asc")
	for index, name in enumerate(guests):
		if index < len(LOCAL_GUESTS):
			first, last, city = LOCAL_GUESTS[index]
		else:
			first, last, city = "Guest", f"Costa Rica {index + 1}", "San José"
		doc = frappe.get_doc("Guest", name)
		doc.first_name = first
		doc.last_name = last
		doc.full_name = f"{first} {last}"
		doc.phone = f"+506 70{index + 1:02d} {1000 + index:04d}"
		doc.email = f"guest{index + 1:02d}@example.cr"
		doc.nationality = "Costa Rican"
		doc.city = city
		doc.save(ignore_permissions=True)

	for reservation in frappe.get_all("Reservation", fields=["name", "guest"]):
		doc = frappe.get_doc("Reservation", reservation.name)
		if reservation.guest:
			doc.guest_name = frappe.db.get_value("Guest", reservation.guest, "full_name")
		# Reprice only reservations whose folios have no posted activity.
		folio = frappe.db.get_value("Folio", {"reservation": reservation.name}, "name")
		if not folio or not (
			frappe.db.count("Folio Charge", {"parent": folio})
			or frappe.db.count("Folio Payment", {"parent": folio})
		):
			doc.apply_pricing()
			doc.db_update()


def _configure_system():
	installed_apps = set(frappe.get_installed_apps())
	system_settings = frappe.get_doc("System Settings")
	# The cloud demo is Kamra-only and keeps its product UI in English. The
	# combined local ERP demo remains Spanish, as originally requested.
	system_settings.language = "es" if "erpnext" in installed_apps else "en"
	system_settings.country = "Costa Rica"
	system_settings.time_zone = "America/Costa_Rica"
	system_settings.date_format = "dd-mm-yyyy"
	system_settings.number_format = "#.###,##"
	system_settings.first_day_of_the_week = "Monday"
	system_settings.save(ignore_permissions=True)

	if "erpnext" in installed_apps:
		global_defaults = frappe.get_doc("Global Defaults")
		company_name = "Hotel Demo PMS"
		company_exists = frappe.db.exists("Company", company_name)
		global_defaults.default_company = company_name if company_exists else ""
		global_defaults.country = "Costa Rica"
		global_defaults.default_currency = "CRC"
		global_defaults.save(ignore_permissions=True)

		if company_exists:
			frappe.db.set_value(
				"Company",
				company_name,
				{"country": "Costa Rica", "default_currency": "CRC"},
			)

	frappe.db.sql(
		"""UPDATE `tabUser`
		SET language = %(language)s
		WHERE enabled = 1 AND COALESCE(language, '') != %(language)s""",
		{"language": "es" if "erpnext" in installed_apps else "en"},
	)


def _rename_titled_doc(doctype, title_field, old_title, new_title):
	name = frappe.db.get_value(
		doctype, {"property": "Hotel Central San José", title_field: old_title}, "name"
	)
	if not name:
		return frappe.db.get_value(
			doctype, {"property": "Hotel Central San José", title_field: new_title}, "name"
		)
	frappe.db.set_value(doctype, name, title_field, new_title)
	if doctype in ("Experience", "Venue", "POS Outlet"):
		desired = f"Hotel Central San José-{new_title}"
		if name != desired and not frappe.db.exists(doctype, desired):
			name = frappe.rename_doc(doctype, name, desired, force=True)
	return name


def _configure_showcase():
	property_name = "Hotel Central San José"
	for old, (new, price, description) in EXPERIENCE_UPDATES.items():
		name = _rename_titled_doc("Experience", "experience_name", old, new)
		if name:
			frappe.db.set_value("Experience", name, {
				"price": price, "gst_rate": 13, "description": description,
			})

	for old, (new, capacity, price) in VENUE_UPDATES.items():
		name = _rename_titled_doc("Venue", "venue_name", old, new)
		if name:
			frappe.db.set_value("Venue", name, {
				"capacity": capacity, "base_price": price, "gst_rate": 13,
				"amenities": "Wi-Fi, audiovisual support, local catering and event staff.",
			})

	for old, (new, rate, cuisine) in MENU_UPDATES.items():
		name = frappe.db.get_value(
			"Banquet Menu", {"property": property_name, "menu_name": old}, "name"
		) or frappe.db.get_value(
			"Banquet Menu", {"property": property_name, "menu_name": new}, "name"
		)
		if name:
			frappe.db.set_value("Banquet Menu", name, {
				"menu_name": new, "rate_per_pax": rate, "cuisine": cuisine,
				"gst_rate": 13,
			})
	for row in frappe.get_all(
		"Banquet Menu Course", filters={"parenttype": "Banquet Menu"},
		fields=["name", "dishes"],
	):
		if row.dishes in COURSE_DISH_UPDATES:
			frappe.db.set_value(
				"Banquet Menu Course", row.name, "dishes", COURSE_DISH_UPDATES[row.dishes]
			)

	for old, new in DISH_UPDATES.items():
		name = frappe.db.get_value(
			"Banquet Dish", {"property": property_name, "dish_name": old}, "name"
		) or frappe.db.get_value(
			"Banquet Dish", {"property": property_name, "dish_name": new}, "name"
		)
		if name:
			frappe.db.set_value("Banquet Dish", name, "dish_name", new)

	for row in frappe.get_all(
		"Banquet Service Item", filters={"property": property_name}, pluck="name"
	):
		frappe.db.set_value("Banquet Service Item", row, {
			"gst_rate": 13, "cost_gst_rate": 13,
		})
	bar = frappe.db.get_value(
		"Banquet Service Item",
		{"property": property_name, "item_name": ["like", "Bar service%"]},
		"name",
	)
	if bar:
		frappe.db.set_value("Banquet Service Item", bar, {
			"item_name": "Local bar service (on consumption)",
			"description": "Costa Rican beer, wine and spirits billed on consumption.",
		})

	for old, new in (("The Terrace Restaurant", "Restaurante Sabores Ticos"),
	                 ("Poolside Bar", "Bar Pura Vida")):
		name = _rename_titled_doc("POS Outlet", "outlet_name", old, new)
		if name:
			frappe.db.set_value("POS Outlet", name, "gst_rate", 13)

	for old, (new, category, price) in MENU_ITEM_UPDATES.items():
		name = frappe.db.get_value(
			"Menu Item", {"property": property_name, "item_name": old}, "name"
		) or frappe.db.get_value(
			"Menu Item", {"property": property_name, "item_name": new}, "name"
		)
		if name:
			frappe.db.set_value("Menu Item", name, {
				"item_name": new, "category": category, "price": price,
			})

	for old, (new, cost, category) in INGREDIENT_UPDATES.items():
		name = frappe.db.get_value(
			"Ingredient", {"property": property_name, "ingredient_name": old}, "name"
		) or frappe.db.get_value(
			"Ingredient", {"property": property_name, "ingredient_name": new}, "name"
		)
		if name:
			frappe.db.set_value("Ingredient", name, {
				"ingredient_name": new, "cost_per_unit": cost,
				"category": category, "gst_rate": 13,
			})

	for row in frappe.get_all(
		"Laundry Rate", filters={"property": property_name},
		fields=["name", "item_name", "service_type"],
	):
		item = {"Kurta": "Blouse", "Saree": "Evening Dress"}.get(
			row.item_name, row.item_name
		)
		base = {"Wash & Iron": 2500, "Dry Clean": 4500, "Iron Only": 1500}.get(
			row.service_type, 2500
		)
		if item in ("Suit (2 pc)", "Blazer", "Evening Dress"):
			base += 2000
		frappe.db.set_value("Laundry Rate", row.name, {
			"item_name": item, "rate": base, "express_rate": round(base * 1.5),
		})

	_configure_events_and_operations()


def _configure_events_and_operations():
	property_name = "Hotel Central San José"
	events = [
		("Sharma-Verma Reception", "Valverde-Rojas Wedding Reception", "Andrea Valverde", "+506 7010 2001", "Wedding reception with a Costa Rican buffet, tropical floral stage and local DJ."),
		("Acme Leadership Offsite", "Grupo Tico Leadership Retreat", "Mariana Solís", "+506 7010 2002", "Two-day leadership retreat with U-shape seating, lunch and projector."),
		(None, "Pacific Sunset Wedding Enquiry", "Carlos Herrera", "+506 7010 2003", "Outdoor wedding enquiry with tropical cocktail bites and DJ."),
		(None, "Arenal Family Celebration", "Elena Mora", "+506 7010 2004", "Family celebration with a view of the gardens."),
	]
	rows = frappe.get_all(
		"Venue Booking", filters={"property": property_name},
		fields=["name", "event_name"], order_by="creation asc",
	)
	for index, row in enumerate(rows[:len(events)]):
		old, event_name, customer, phone, requirements = events[index]
		if old and row.event_name not in (old, event_name):
			continue
		values = {
			"event_name": event_name, "customer_name": customer,
			"billing_name": customer, "customer_phone": phone,
			"gstin": "3-101-123456", "place_of_supply": "Costa Rica",
			"requirements": requirements,
		}
		if index == 1:
			values["customer_email"] = "eventos@grupotico.example.cr"
		if index >= 2:
			values["event_type"] = "Wedding" if index == 2 else "Anniversary"
		frappe.db.set_value("Venue Booking", row.name, values)

	for receipt in frappe.get_all(
		"Banquet Receipt", filters={"parenttype": "Venue Booking"},
		fields=["name", "reference"],
	):
		if (receipt.reference or "").startswith("UTR"):
			frappe.db.set_value(
				"Banquet Receipt", receipt.name, "reference", "SINPE-CR-9911002233"
			)

	local_table_guests = [
		("Gabriela Zúñiga", "+506 7010 3001"),
		("Mauricio Brenes", "+506 7010 3002"),
	]
	for index, row in enumerate(frappe.get_all(
		"POS Table Reservation", filters={"property": property_name},
		pluck="name", order_by="creation asc",
	)):
		guest, phone = local_table_guests[index % len(local_table_guests)]
		frappe.db.set_value("POS Table Reservation", row, {
			"guest_name": guest, "phone": phone,
		})

	ticket_subjects = [
		"Extra towels requested for the second floor",
		"Air conditioning check in room 301",
		"SJO airport transfer at 6 AM",
		"Late checkout requested",
		"Crib requested for a family stay",
		"Wi-Fi signal check on the third floor",
		"Birthday cake for table F2 tonight",
		"Quiet-hours complaint in second-floor corridor",
		"Iron and board requested",
		"Universal travel adapter requested",
	]
	for index, row in enumerate(frappe.get_all(
		"Service Ticket", filters={"property": property_name},
		pluck="name", order_by="creation asc",
	)):
		if index < len(ticket_subjects):
			frappe.db.set_value("Service Ticket", row, "subject", ticket_subjects[index])

	for index, row in enumerate(frappe.get_all(
		"Shift Handover", filters={"property": property_name},
		pluck="name", order_by="shift_date asc, creation asc",
	)):
		opening = 100000 if index < 2 else 75000
		collected = (328500, 412000, 186500)[index % 3]
		payouts = (18500, 24000, 9500)[index % 3]
		frappe.db.set_value("Shift Handover", row, {
			"opening_cash": opening, "cash_collected": collected,
			"payouts": payouts, "closing_cash": opening + collected - payouts,
			"handover_notes": "Costa Rica demo shift with CRC cash reconciliation.",
		})

	for row in frappe.get_all(
		"Channel Provider Connection", filters={"property": property_name}, pluck="name"
	):
		frappe.db.set_value("Channel Provider Connection", row, {
			"phone_number": "+506 2222 1000", "meta_language": "es_CR",
			"notes": "Demo connection for a Costa Rican hotel. Add real Meta credentials before enabling.",
		})
	for index, row in enumerate(frappe.get_all(
		"WhatsApp Message", filters={"property": property_name},
		pluck="name", order_by="creation asc",
	)):
		messages = [
			"Reserva confirmada en Hotel Central San José.",
			"Complete su pre-registro antes de llegar: https://hotelcentral.demo/checkin/demo",
			"¡Hola! ¿Sería posible salir a las 2 p. m. el domingo?",
			"Claro, le confirmamos el late checkout hasta las 2 p. m.",
		]
		frappe.db.set_value("WhatsApp Message", row, {
			"content": messages[index % len(messages)],
			"to_number": "+506 7010 4001", "from_number": "+506 2222 1000",
		})


def _add_demo_charge(folio, charge_type, description, amount):
	if any(row.description == description for row in folio.charges):
		return
	folio.append("charges", {
		"posting_date": nowdate(), "charge_type": charge_type,
		"description": description, "qty": 1, "rate": amount,
		"amount": amount, "gst_rate": 13,
	})
	from kamra.folio import _recalculate
	_recalculate(folio)
	folio.save(ignore_permissions=True)
	row = folio.charges[-1]
	if not frappe.db.exists("Folio Ledger Entry", {
		"source_doctype": "Folio Charge", "source_name": row.name,
	}):
		from kamra.ledger import record_charge_ledger
		record_charge_ledger(folio, row.as_dict())


def _seed_financial_demo():
	property_name = "Hotel Central San José"
	if not frappe.db.exists("Property", property_name):
		return
	from kamra.cashier import open_session, post_petty_cash
	from kamra.folio import close_folio, open_folio
	from kamra.api import add_folio_payment

	session = open_session(property_name, opening_float=100000, terminal="Front Desk Demo")
	reservations = frappe.get_all(
		"Reservation",
		filters={"property": property_name, "status": ["in", ["Checked In", "Confirmed"]]},
		pluck="name", order_by="check_in_date asc, creation asc", limit=3,
	)
	stories = [
		(("Room", "Demo room revenue - Standard stay", 45000),
		 ("Food & Beverage", "Dinner at Restaurante Sabores Ticos", 12500),
		 "Card", "DEMO-VISA-4242", "full"),
		(("Room", "Demo room revenue - Deluxe stay", 65000),
		 ("Laundry", "Guest laundry service", 4500),
		 "Bank Transfer", "SINPE-DEMO-1002", 40000),
		(("Room", "Demo room revenue - Suite stay", 95000),
		 ("Minibar", "Local minibar selection", 8500),
		 "OTA Prepaid", "OTA-DEMO-1003", 95000),
	]
	for reservation_name, story in zip(reservations, stories):
		reservation = frappe.get_doc("Reservation", reservation_name)
		folio_name = open_folio(reservation)
		folio = frappe.get_doc("Folio", folio_name)
		if folio.status == "Closed":
			continue
		for charge_type, description, amount in story[:2]:
			_add_demo_charge(folio, charge_type, description, amount)
			folio.reload()
		mode, reference, payment_amount = story[2:]
		if not frappe.db.exists("Folio Payment", {"parent": folio.name, "reference": reference}):
			amount = float(folio.balance) if payment_amount == "full" else float(payment_amount)
			add_folio_payment(folio.name, mode, amount, reference=reference)
			folio.reload()
		if payment_amount == "full" and round(float(folio.balance or 0), 2) == 0:
			close_folio(folio.name)

	if not frappe.db.exists("Petty Cash Voucher", {
		"property": property_name, "payee": "Abastecedor Central",
	}):
		post_petty_cash(
			property_name, 12500, "Abastecedor Central", "Supplies",
			"Coffee, fruit and front-desk supplies for the demo shift.",
		)

	_seed_pos_orders(session.get("name") if isinstance(session, dict) else None)
	if not frappe.db.exists("Night Audit Run", {
		"property": property_name, "business_date": add_days(nowdate(), -1),
	}):
		frappe.get_doc({
			"doctype": "Night Audit Run", "property": property_name,
			"business_date": add_days(nowdate(), -1), "status": "Completed",
			"room_charges_posted": 8, "amount_posted": 420000,
			"no_shows_flagged": 1, "folios_opened": 5,
			"log": "Demo audit completed in CRC. Room revenue, tax and open balances reconciled.",
		}).insert(ignore_permissions=True)


def _seed_pos_orders(session=None):
	property_name = "Hotel Central San José"
	from kamra.pos import create_order, deliver_order, pay_order

	def item(name):
		return frappe.db.get_value(
			"Menu Item", {"property": property_name, "item_name": name}, "name"
		)

	restaurant = frappe.db.get_value(
		"POS Outlet", {"property": property_name, "outlet_name": "Restaurante Sabores Ticos"}, "name"
	)
	bar = frappe.db.get_value(
		"POS Outlet", {"property": property_name, "outlet_name": "Bar Pura Vida"}, "name"
	)
	if restaurant and not frappe.db.exists("POS Order", {"notes": "CR-DEMO-LUNCH"}):
		order = create_order(
			restaurant,
			[{"menu_item": item("Casado with Chicken"), "qty": 2},
			 {"menu_item": item("Tres Leches Cake"), "qty": 1}],
			property=property_name, table_no="T2", guests=2,
			customer_name="Walk-in demo", notes="CR-DEMO-LUNCH",
		)["order"]
		pay_order(order, "Cash")
	if bar and not frappe.db.exists("POS Order", {"notes": "CR-DEMO-BAR"}):
		order = create_order(
			bar, [{"menu_item": item("Imperial Beer"), "qty": 2}],
			property=property_name, order_type="Takeaway",
			customer_name="Walk-in demo", customer_phone="+506 7010 5001",
			notes="CR-DEMO-BAR",
		)["order"]
		pay_order(order, "Card")

	in_house = frappe.db.get_value(
		"Reservation", {"property": property_name, "status": "Checked In"},
		["name", "room"], as_dict=True,
	)
	if restaurant and in_house and not frappe.db.exists(
		"POS Order", {"notes": "CR-DEMO-ROOM-SERVICE"}
	):
		order = create_order(
			restaurant, [{"menu_item": item("Gallo Pinto Breakfast"), "qty": 2}],
			property=property_name, room=in_house.room,
			reservation=in_house.name, order_type="Room Service",
			notes="CR-DEMO-ROOM-SERVICE",
		)["order"]
		deliver_order(order)


def execute():
	# This is a persistent local demo, not Kamra's public shared playground.
	# Keep both flags so the UI is accurate and the scheduler cannot wipe it.
	frappe.db.set_default("kamra_demo_mode", "0")
	frappe.db.set_default("kamra_disable_demo_reset", "1")
	_configure_system()
	for email, (first_name, last_name) in DEMO_USER_NAMES.items():
		if frappe.db.exists("User", email):
			frappe.db.set_value(
				"User", email,
				{"first_name": first_name, "last_name": last_name},
				update_modified=False,
			)
	_configure_properties()
	_configure_guests()
	_configure_showcase()
	_seed_financial_demo()
	frappe.clear_cache()
	frappe.db.commit()  # nosemgrep: frappe-manual-commit -- idempotent deployment seed persists its completed demo transaction
	return {
		"language": "es" if "erpnext" in frappe.get_installed_apps() else "en",
		"currency": "CRC",
		"demo_reset_disabled": frappe.db.get_default("kamra_disable_demo_reset"),
		"erpnext_installed": "erpnext" in frappe.get_installed_apps(),
		"properties": frappe.get_all(
			"Property", fields=["name", "city", "state", "country", "currency", "locale"]
		),
		"restaurant_outlets": frappe.get_all(
			"POS Outlet", fields=["outlet_name", "outlet_type", "gst_rate"]
		),
		"financial_demo": {
			"folios": frappe.db.count("Folio"),
			"ledger_entries": frappe.db.count("Folio Ledger Entry"),
			"cashier_sessions": frappe.db.count("Cashier Session"),
			"pos_orders": frappe.db.count("POS Order"),
		},
	}
