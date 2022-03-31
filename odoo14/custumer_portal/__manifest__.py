# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Portal Customizado',
    'version': '14.0.1',
    'category': 'Sales/Sales',
    'summary': 'Sales Custom Portal',
    'description': """
This module contains modification for client sales portal
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_portal.xml',
    ],
    'license': 'LGPL-3',
}
