from fabtex_pro.utils.selling.sales_invoice import sales_invoice_customization
from fabtex_pro.utils.company.company import company_customization
from fabtex_pro.utils.selling.customer import customer_customization
from fabtex_pro.utils.buying.purchase_invoice import purchase_invoice_customization

def after_install():
    company_customization()
    customer_customization()
    sales_invoice_customization()
    purchase_invoice_customization()