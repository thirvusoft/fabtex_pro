// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.query_reports["Purchase Register"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		},
		// Customized By Thirvusoft
		// Start
		{
			"fieldname":"ts_purchase_invoice_group",
			"label": __("Purchase Invoice Group"),
			"fieldtype": "Link",
			"options": "Purchase Invoice Group"
		},
		// End
		{
			"fieldname":"supplier",
			"label": __("Supplier"),
			"fieldtype": "Link",
			"options": "Supplier"
		},
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company")
		},
		// Customized By Thirvusoft
		// Start
		// {
		// 	"fieldname":"mode_of_payment",
		// 	"label": __("Mode of Payment"),
		// 	"fieldtype": "Link",
		// 	"options": "Mode of Payment"
		// },
		// {
		// 	"fieldname":"cost_center",
		// 	"label": __("Cost Center"),
		// 	"fieldtype": "Link",
		// 	"options": "Cost Center"
		// },
		// {
		// 	"fieldname":"warehouse",
		// 	"label": __("Warehouse"),
		// 	"fieldtype": "Link",
		// 	"options": "Warehouse"
		// },
		// {
		// 	"fieldname":"item_group",
		// 	"label": __("Item Group"),
		// 	"fieldtype": "Link",
		// 	"options": "Item Group"
		// }
		// End
	]
}

erpnext.utils.add_dimensions('Purchase Register', 7);
