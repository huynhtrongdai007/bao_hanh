# -*- coding: utf-8 -*-
from odoo import fields, models, api


class FSMOrder(models.Model):
    _inherit = 'fsm.order'

    x_is_warranty = fields.Boolean(
        string='Đơn bảo hành',
        default=False,
        index=True,
    )
    x_warranty_end_date = fields.Date(
        string='Ngày hết hạn bảo hành',
        related='equipment_id.warranty_end_date',
        store=True,
        readonly=True,
    )
