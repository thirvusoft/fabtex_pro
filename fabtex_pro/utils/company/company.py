from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

def company_customization():
	print("Updating Customization For Company")
	custom_fields()
	property_setter()

def custom_fields():
    new_fields = {"Company":[
        {
            "fieldname": "vat_tin",
            "label": "VAT TIN",
            "fieldtype": "Data",
            "insert_after": "pan_details",
        },
        {
            "fieldname": "cst_no",
            "label": "CST No",
            "fieldtype": "Data",
            "insert_after": "vat_tin",
        },
    ]}
    create_custom_fields(new_fields)

def property_setter():
    pass