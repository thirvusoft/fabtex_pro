from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def delivery_note_customization():
	print("Updating Customization For Delivery Note")
	custom_fields()
	property_setter()

def custom_fields():

	new_fields = {"Delivery Note":[
		{
			"fieldname" : "ts_vessel_flight_no",
			"label" : "Vessel/Flight/Vehicle No.",
			"fieldtype" : "Data",
			"insert_after" : "lr_no"
		},
		
		{
			"fieldname" : "ts_gst_details_section_break",
			"label" : "GST Details",
			"fieldtype" : "Section Break",
			"collapsible" : 1,
			"insert_after" : "lr_date"
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
			"fieldname" : "ts_other_references1",
			"label" : "Other References",
			"fieldtype" : "Data",
			"insert_after" : "ts_other_references"
		},
		{
			"fieldname" : "ts_other_references2",
			"label" : "Other References",
			"fieldtype" : "Data",
			"insert_after" : "ts_other_references1"
		},
		{
			"fieldname" : "ts_despatch_document_no",
			"label" : "Despatch Document No.",
			"fieldtype" : "Data",
			"insert_after" : "ts_other_references2"
		},
		{
			"fieldname" : "ts_despatch_through",
			"label" : "Despatch Through",
			"fieldtype" : "Data",
			"insert_after" : "ts_despatch_document_no"
		},
		{
			"fieldname" : "ts_g_r_no_",
			"label" : "G.R No.",
			"fieldtype" : "Data",
			"insert_after" : "column_break_88"
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

	make_property_setter("Delivery Note", "section_break1", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "sales_team_section_break", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "printing_details", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "driver", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "lr_no", "label", "Transport Receipt No.", "Data")
	make_property_setter("Delivery Note", "vehicle_no", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "distance", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "transporter_name", "read_only", 0, "Check")
	make_property_setter("Delivery Note", "mode_of_transport", "default", "", "Small Text")
	make_property_setter("Delivery Note", "print_without_amount", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "group_same_items", "hidden", 1, "Check")
	make_property_setter("Delivery Note", "more_info", "hidden", 1, "Check")