from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def sales_invoice_customization():
	print("Updating Customization For Sales Invoice")
	custom_fields()
	property_setter()

def custom_fields():
	# Core Fields
	#  Start
	si_ewaybill_fields = {"Sales Invoice":[
			{
				"fieldname": "transporter_info",
				"label": "Transporter Info",
				"fieldtype": "Section Break",
				"insert_after": "terms",
				"collapsible": 1,
				"collapsible_depends_on": "transporter",
				"print_hide": 1,
			},
			{
				"fieldname": "transporter",
				"label": "Transporter",
				"fieldtype": "Link",
				"insert_after": "transporter_info",
				"options": "Supplier",
				"print_hide": 1,
			},
			{
				"fieldname": "gst_transporter_id",
				"label": "GST Transporter ID",
				"fieldtype": "Data",
				"insert_after": "transporter",
				"fetch_from": "transporter.gst_transporter_id",
				"print_hide": 1,
				"translatable": 0,
				"length": 20,
			},
			{
				"fieldname": "driver",
				"label": "Driver",
				"fieldtype": "Link",
				"insert_after": "gst_transporter_id",
				"options": "Driver",
				"print_hide": 1,
			},
			{
				"fieldname": "lr_no",
				"label": "Transport Receipt No",
				"fieldtype": "Data",
				"insert_after": "driver",
				"print_hide": 1,
				"translatable": 0,
				"length": 30,
			},
			{
				"fieldname": "vehicle_no",
				"label": "Despatch through",
				"fieldtype": "Data",
				"insert_after": "lr_no",
				"print_hide": 1,
				"translatable": 0,
				"length": 10,
				"hidden":1
			},
			{
				"fieldname": "distance",
				"label": "Distance (in km)",
				"fieldtype": "Float",
				"insert_after": "vehicle_no",
				"print_hide": 1,
				"hidden":1
			},
			{	"fieldname": "transporter_col_break",
				"fieldtype": "Column Break", 
				"insert_after": "distance"
			},
			{
				"fieldname": "transporter_name",
				"label": "Transporter Name",
				"fieldtype": "Small Text",
				"insert_after": "transporter_col_break",
				"fetch_from": "transporter.name",
				"read_only": 1,
				"print_hide": 1,
				"translatable": 0,
			},
			{
				"fieldname": "mode_of_transport",
				"label": "Mode of Transport",
				"fieldtype": "Select",
				"options": "\nRoad\nAir\nRail\nShip",
				"insert_after": "transporter_name",
				"print_hide": 1,
				"translatable": 0,
				"length": 5,
			},
			{
				"fieldname": "driver_name",
				"label": "Driver Name",
				"fieldtype": "Data",
				"insert_after": "mode_of_transport",
				"fetch_from": "driver.full_name",
				"print_hide": 1,
				"translatable": 0,
			},
			{
				"fieldname": "lr_date",
				"label": "Transport Receipt Date",
				"fieldtype": "Date",
				"insert_after": "driver_name",
				"default": "Today",
				"print_hide": 1,
			},
			{
				"fieldname": "gst_vehicle_type",
				"label": "GST Vehicle Type",
				"fieldtype": "Select",
				"options": "Regular\nOver Dimensional Cargo (ODC)",
				"depends_on": 'eval:(doc.mode_of_transport === "Road")',
				"default": "Regular",
				"insert_after": "lr_date",
				"print_hide": 1,
				"translatable": 0,
				"length": 30,
			},
			{
				"fieldname": "ewaybill",
				"label": "E-Way Bill No.",
				"fieldtype": "Data",
				"allow_on_submit": 0,
				"insert_after": "einvoice_section",
				"translatable": 0,
				"length": 20,
			},
			{
				"fieldname" : "export_type",
				"label" : "Export Type",
				"fieldtype" : "Select",
				"insert_after" : "ewaybill",
				"print_hide" : 1,
				"depends_on" : 'eval:in_list(["SEZ", "Overseas", "Deemed Export"], doc.gst_category)',
				"options" : "\nWith Payment of Tax\nWithout Payment of Tax",
				"fetch_from" : "customer.export_type",
				"fetch_if_empty" :  1,
				"length" : 25,
			},
		]}
	create_custom_fields(si_ewaybill_fields)
	# End
	new_fields = {"Sales Invoice":[
		{
			"fieldname": "ts_sales_invoice_group",
			"label": "Sales Invoice Group",
			"fieldtype": "Link",
			"options" : "Sales Invoice Group",
			"insert_after": "customer_name",
			"reqd" : 1
		},
		{
			"fieldname" : "ts_others",
			"label" : "Others",
			"fieldtype" : "Section Break",
			"collapsible" : 1,
			"insert_after" : "language"
		},
		{
			"fieldname" : "ts_suppliers_ref",
			"label" : "Suppliers Ref",
			"fieldtype" : "Data",
			"insert_after" : "ts_others"
		},
		{
			"fieldname" : "ts_other_references",
			"label" : "Other References",
			"fieldtype" : "Data",
			"insert_after" : "ts_suppliers_ref"
		},
		{
			"fieldname" : "ts_despatch_document_no",
			"label" : "Despatch Document No.",
			"fieldtype" : "Data",
			"insert_after" : "ts_other_references"
		},
		{
			"fieldname" : "ts_despatch_through",
			"label" : "Despatch Through",
			"fieldtype" : "Data",
			"insert_after" : "ts_despatch_document_no"
		},
		{
			"fieldname" : "ts_vessel_flight_no",
			"label" : "Vessel/Flight No.",
			"fieldtype" : "Data",
			"insert_after" : "ts_despatch_through"
		},
		{
			"fieldname" : "ts_column_break",
			"fieldtype" : "Column Break",
			"insert_after" : "ts_vessel_flight_no"
		},
		{
			"fieldname" : "ts_g_r_no_",
			"label" : "G.R No.",
			"fieldtype" : "Data",
			"insert_after" : "ts_column_break"
		},
		{
			"fieldname" : "ts_gr_no_date",
			"label" : "GR Date",
			"fieldtype" : "Date",
			"insert_after" : "ts_g_r_no_"
		},
		{
			"fieldname" : "ts_city_port_of_loading",
			"label" : "City/Port of Loading",
			"fieldtype" : "Data",
			"insert_after" : "ts_gr_no_date"
		},
		{
			"fieldname" : "ts_city_port_of_discharge",
			"label" : "City/Port of Discharge",
			"fieldtype" : "Data",
			"insert_after" : "ts_city_port_of_loading"
		},
		{
			"fieldname" : "ts_place_of_receipt_by_shipper",
			"label" : "Place of Receipt by Shipper",
			"fieldtype" : "Data",
			"insert_after" : "ts_city_port_of_discharge"
		},
	]}
	create_custom_fields(new_fields)

def property_setter():
	pass
	make_property_setter("Sales Invoice", "einvoice_section", "hidden", 0, "Check")
	make_property_setter("Sales Invoice", "einvoice_section", "collapsible", 1, "Check")
	make_property_setter("Sales Invoice", "transporter_name", "read_only", 0, "Check")
	make_property_setter("Sales Invoice", "transporter_name", "fieldtype", "Data", "Data")
	make_property_setter("Sales Invoice", "edit_printing_settings", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "time_sheet_list", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "loyalty_points_redemption", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "accounting_dimensions_section", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "section_break2", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "subscription_section", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "sales_team_section_break", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "letter_head", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "group_same_items", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "select_print_heading", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "is_pos", "hidden", 1, "Check")
	make_property_setter("Sales Invoice", "driver", "hidden", 1, "Check")