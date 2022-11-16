from fabtex_pro.utils.selling.sales_invoice import sales_invoice_customization
from fabtex_pro.utils.company.company import company_customization

def after_install():
    company_customization()
    sales_invoice_customization()