# -*- coding: utf-8 -*-
{
    'name': 'Mail relocation',
    'version': '1.0.4',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'GPL-3',
    "category": "Discuss",
    'website': 'https://twitter.com/yelizariev',
    'price': 100.00,
    'currency': 'EUR',
    'depends': ['mail', 'web_polymorphic_field'],
    'images': ['images/inbox.png'],
    'data': [
        'mail_move_message_views.xml',
        'data/mail_move_message_data.xml',
    ],
    'qweb': [
        'static/src/xml/mail_move_message_main.xml',
    ],
    'installable': True
}
