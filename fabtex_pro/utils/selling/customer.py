from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def customer_customization():
	print("Updating Customization For Customer")
	custom_fields()
	property_setter()

def custom_fields():
    pass

def property_setter():
    make_property_setter("Customer", "tax_category", "reqd", 1, "Check")