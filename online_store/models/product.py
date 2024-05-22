from odoo import models, fields

class Product(models.Model):
    _name = 'online_store.product'
    _description = 'Product'

    name = fields.Char(string='Product Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    category_id = fields.Many2one('online_store.category', string='Category')
