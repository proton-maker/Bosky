from odoo import models, fields, api

class SalesReport(models.TransientModel):
    _name = 'bosky_store.sales_report'
    _description = 'Sales Report'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    total_sales = fields.Float(string='Total Sales', compute='_compute_total_sales')
    top_products = fields.Char(string='Top Products', compute='_compute_top_products')

    @api.depends('start_date', 'end_date')
    def _compute_total_sales(self):
        for report in self:
            orders = self.env['bosky_store.order'].search([('order_date', '>=', report.start_date), ('order_date', '<=', report.end_date)])
            report.total_sales = sum(order.total_amount for order in orders)

    @api.depends('start_date', 'end_date')
    def _compute_top_products(self):
        for report in self:
            orders = self.env['bosky_store.order'].search([('order_date', '>=', report.start_date), ('order_date', '<=', report.end_date)])
            product_sales = {}
            for order in orders:
                for product in order.product_ids:
                    if product.name not in product_sales:
                        product_sales[product.name] = 0
                    product_sales[product.name] += 1
            top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:5]
            report.top_products = ', '.join([f'{name} ({count})' for name, count in top_products])
