from odoo import models, fields, api

class Product(models.Model):
    _name = 'online_store.product'
    _description = 'Product'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    discount = fields.Float(string='Discount (%)')  # Field diskon
    final_price = fields.Float(string='Final Price', compute='_compute_final_price')  # Harga akhir setelah diskon
    category_id = fields.Many2one('online_store.category', string='Category')

    @api.depends('price', 'discount')
    def _compute_final_price(self):
        for product in self:
            product.final_price = product.price - (product.price * (product.discount / 100))
