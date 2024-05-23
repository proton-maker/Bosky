{
    'name': 'Bosky Store',
    'version': '1.0',
    'summary': 'A simple online store module for Odoo',
    'description': 'This module adds basic online store functionalities to Odoo.',
    'author': 'Rizky Alfi',
    'category': 'Sales',
    'website': 'http://bosmudasky.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/category_view.xml',
        'views/order_view.xml',
        'views/report_view.xml',
        'data/data.xml',
        'data/order_sequence.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'bosky_store/static/description/favicon.png',
        ],
    },
    'images': ['static/description/favicon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
