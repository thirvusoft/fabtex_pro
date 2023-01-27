from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def purchase_invoice_customization():
	print("Updating Customization For Purchase Invoice")
	custom_fields()
	property_setter()

def custom_fields():

	new_fields = {"Purchase Invoice":[
		{
			"fieldname": "ts_purchase_invoice_group",
			"label": "Purchase Invoice Group",
			"fieldtype": "Link",
			"options" : "Purchase Invoice Group",
			"insert_after": "supplier",
			"reqd" : 1
		},
	]}
	create_custom_fields(new_fields)

def property_setter():
	pass
