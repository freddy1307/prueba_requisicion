# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api, _


class Quotitation(models.Model):
    _name = 'gi.quotation'
    _description = 'Example quotation'

    name = fields.Char(string="Folio", default="New quotation")
    date = fields.Date(string="Date", required=True)
    partner = fields.Many2one(comodel_name="res.partner", string="Client", required=True)
    payment_term_id = fields.Many2one(comodel_name="account.payment.term", string="Payment term", required=True)
    line_ids = fields.One2many(comodel_name='gi.quotation.line', inverse_name="line_id", string="Lines")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('gi.quotation') or _('New')
        return super(Quotitation, self).create(vals)


class QuotationLine(models.Model):
    _name = 'gi.quotation.line'
    _description = 'Line quotation'

    number = fields.Integer(compute='get_number', store=True)
    product_id = fields.Many2one(comodel_name="product.product", string="Product", required=True )
    qty = fields.Integer(string="Qty", required=True)
    price_list = fields.Float(string="Price list", required=True)
    total_line = fields.Float(string="Total line", compute="calc_total")
    line_id = fields.Many2one(comodel_name='gi.quotation', string="Line")

    @api.depends('line_id')
    def get_number(self):
        for lines in self.mapped('line_id'):
            number = 1
            for line in lines.line_ids:
                line.number = number
                number += 1

    @api.onchange('qty','price_list')
    @api.depends('qty','price_list')
    def calc_total(self):
        for rec in self:
            if rec.qty > 0 and rec.price_list > 0:
                rec.total_line = rec.qty * rec.price_list




