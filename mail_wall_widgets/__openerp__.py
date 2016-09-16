# -*- coding: utf-8 -*-
{
    'name': 'Extra Widgets for mail wall',
    'version': '1.0.0',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'GPL-3',
    'category': 'Custom',
    'website': 'https://yelizariev.github.io',
    'description': """

Tested on odoo 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d
    """,
    'depends': ['mail', 'gamification'],
    'data': [
        'views.xml',
        # 'data.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/main.xml'],
    'installable': True,
}
