from odoo import models, fields, api

class Product(models.Model):
    _name = 'bosky_store.product'
    _description = 'Product'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    discount = fields.Float(string='Discount (%)')
    final_price = fields.Float(string='Final Price', compute='_compute_final_price', store=True)
    category_id = fields.Many2one('bosky_store.category', string='Category')
    stock = fields.Integer(string='Stock', default=0)
    sku = fields.Char(string='SKU', required=True)
    image = fields.Binary(string='Product Image')

    @api.depends('price', 'discount')
    def _compute_final_price(self):
        for product in self:
            product.final_price = product.price * (1 - (product.discount / 100))
