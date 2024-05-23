from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Order(models.Model):
    _name = 'bosky_store.order'
    _description = 'Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    customer_name = fields.Char(string='Customer Name', required=True)
    order_date = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    product_ids = fields.Many2many('bosky_store.product', string='Ordered Products')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount')
    payment_status = fields.Selection([('pending', 'Pending'), ('paid', 'Paid')], string='Payment Status', default='pending')
    email = fields.Char(string='Customer Email')
    name = fields.Char(string="Order Reference", required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    partner_id = fields.Many2one('res.partner', string="Customer", required=True)

    @api.depends('product_ids')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(product.final_price for product in order.product_ids)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('bosky_store.order') or 'New'
        record = super(Order, self).create(vals)
        template = self.env.ref('bosky_store.order_email_template')
        self.env['mail.template'].browse(template.id).send_mail(record.id, force_send=True)
        return record

    def send_email_notification(self):
        template_id = self.env.ref('bosky_store.order_email_template').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
