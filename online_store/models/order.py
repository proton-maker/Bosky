from odoo import models, fields

class Order(models.Model):
    _name = 'online_store.order'
    _description = 'Order'

    customer_name = fields.Char(string='Customer Name', required=True)
    order_date = fields.Datetime(string='Order Date', default=fields.Datetime.now)
    product_ids = fields.Many2many('online_store.product', string='Ordered Products')
