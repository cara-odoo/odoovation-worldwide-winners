{
    "name": "Odoovation WW - Events",
    "description": """
        - To do
    """,
    "category": "Custom Development",
    "version": "1.1.0",
    "author": "Odoo Development Services",
    "maintainer": "Odoo Development Services",
    "website": "https://www.odoo.com",
    "license": "OPL-1",
    "depends": ["website_sale","website_event","stock","hr"],
    "data": [
        'security/ir.model.access.csv',
        'views/event_event_views.xml',
        'views/hr_employee_views.xml'
    ],
}
