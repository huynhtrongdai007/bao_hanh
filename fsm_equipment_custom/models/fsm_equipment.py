# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class FsmEquipmentCustom(models.Model):
    _inherit = 'fsm.equipment'

    x_project = fields.Many2one(
        'project.project',
        string='Project Name',
    )
    x_quantity = fields.Char(
        string='Quantity',
    )
    x_manufacturer = fields.Char(
        string='Manufacturer',
    )
    x_product_code = fields.Char(
        related='product_id.default_code',
        string='Product Code',
        store=True,
    )
    x_note = fields.Text(
        string='Notes',
    )
    x_warranty_display = fields.Char(
        string='Warranty Duration',
        compute='_compute_warranty_display',
    )

    @api.depends('product_id.warranty', 'product_id.warranty_type')
    def _compute_warranty_display(self):
        type_label = {'week': _('week(s)'), 'month': _('month(s)'), 'year': _('year(s)')}
        for rec in self:
            if rec.product_warranty:
                label = type_label.get(rec.product_warranty_type, _('day(s)'))
                rec.x_warranty_display = f"{rec.product_warranty} {label}"
            else:
                rec.x_warranty_display = False
