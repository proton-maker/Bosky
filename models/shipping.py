from odoo import models, fields

class Shipping(models.Model):
    _name = 'bosky_store.shipping'
    _description = 'Shipping'

    order_id = fields.Many2one('bosky_store.order', string='Order', required=True)
    address = fields.Text(string='Shipping Address', required=True)
    shipping_method = fields.Selection([
        ('standard', 'Standard Shipping'),
        ('express', 'Express Shipping')
    ], string='Shipping Method', default='standard')
    shipping_cost = fields.Float(string='Shipping Cost')
    tracking_number = fields.Char(string='Tracking Number')
