from odoo import models, fields, api

class Order(models.Model):
    _name = 'bosky_store.order'
    _description = 'Order'

    customer_name = fields.Char(string='Customer Name', required=True)
    order_date = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    product_ids = fields.Many2many('bosky_store.product', string='Ordered Products')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount')
    payment_status = fields.Selection([('pending', 'Pending'), ('paid', 'Paid')], string='Payment Status', default='pending')
    email = fields.Char(string='Customer Email')

    @api.depends('product_ids')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(product.final_price for product in order.product_ids)

    def send_email_notification(self):
        template_id = self.env.ref('bosky_store.order_email_template').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
