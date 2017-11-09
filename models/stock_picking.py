# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models, _

PURCHASE_STATES = [
    ('draft', _('Draft PO')),
    ('sent', _('RFQ Sent')),
    ('to approve', _('To Approve')),
    ('purchase', _('Purchase Order')),
    ('done', _('Done')),
    ('cancel', _('Cancelled')),
    ('expired', _('Expired')),
    ]


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    purchase_state = fields.Char(
        compute='_get_purchase_state', string='Purchase status', store=True)

    @api.depends('purchase_id')
    def _get_purchase_state(self):
        """Computes value of field purchase_state"""
        
        for record in self:
            if record.purchase_id:
                record.purchase_state = str()
                for po_state in PURCHASE_STATES:
                    if po_state[0] == record.purchase_id.state:
                        record.purchase_state = po_state[1]
