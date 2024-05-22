from odoo import models, fields, api

class Product(models.Model):
    _name = 'bosky_store.product'
    _description = 'Product'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    discount = fields.Float(string='Discount (%)')
    final_price = fields.Float(string='Final Price', compute='_compute_final_price')
    category_id = fields.Many2one('bosky_store.category', string='Category')

    @api.depends('price', 'discount')
    def _compute_final_price(self):
        for product in self:
            product.final_price = product.price - (product.price * (product.discount / 100))
