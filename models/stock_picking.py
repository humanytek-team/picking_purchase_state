# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    purchase_state = fields.Selection(
        [
            ('draft', 'Draft PO'),
            ('sent', 'RFQ Sent'),
            ('to approve', 'To Approve'),
            ('purchase', 'Purchase Order'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
            ('expired', 'Expired'),
            ],
        related='move_lines.purchase_line_id.order_id.state', store=True)
