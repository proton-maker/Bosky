from odoo import models, fields

class Category(models.Model):
    _name = 'bosky_store.category'
    _description = 'Category'

    name = fields.Char(string='Category Name', required=True)
    product_ids = fields.One2many('bosky_store.product', 'category_id', string='Products')
