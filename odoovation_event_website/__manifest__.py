{
    'name': 'Odoovation Event Website',
    'summary': 'Odoovation Event Website',
    'sequence': 100,
    'license': 'OPL-1',
    'website': 'https://www.odoo.com',
    'version': '1.1',
    'author': 'Odoo Inc',
    'description': """
        Odoovation Event Website
    """,
    'category': 'Custom Development',

    'depends': ['website_event_sale'],
    'data': [
        'views/event_templates_page_registration.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}