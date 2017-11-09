# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Purchase status in picking',
    'summary': 'Shows purchase status in the picking (receipts) order',
    'version': '9.0.0.1.0',
    'category': 'Stock',
    'author': 'Humanytek',
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'depends': ['stock', 'purchase'],
    'data': [
        'views/stock_picking_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
