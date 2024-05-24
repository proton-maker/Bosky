from odoo import models, fields, api

class Cart(models.Model):
    _name = 'bosky_store.cart'
    _description = 'Shopping Cart'

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    cart_line_ids = fields.One2many('bosky_store.cart.line', 'cart_id', string='Cart Lines')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    payment_status = fields.Selection([('pending', 'Pending'), ('paid', 'Paid')], string='Payment Status', default='pending')

    @api.depends('cart_line_ids.subtotal')
    def _compute_total_amount(self):
        for cart in self:
            cart.total_amount = sum(line.subtotal for line in cart.cart_line_ids)

    def action_pay(self):
        self.ensure_one()
        order_vals = {
            'customer_name': self.customer_id.name,
            'order_date': fields.Datetime.now(),
            'product_ids': [(6, 0, self.cart_line_ids.mapped('product_id').ids)],
            'total_amount': self.total_amount,
            'payment_status': 'paid',
            'email': self.customer_id.email,
            'partner_id': self.customer_id.id,
            'quantity': sum(self.cart_line_ids.mapped('quantity')),
        }
        order = self.env['bosky_store.order'].create(order_vals)
        self.payment_status = 'paid'
        return order

class CartLine(models.Model):
    _name = 'bosky_store.cart.line'
    _description = 'Shopping Cart Line'

    cart_id = fields.Many2one('bosky_store.cart', string='Cart', required=True)
    product_id = fields.Many2one('bosky_store.product', string='Product', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    price = fields.Float(related='product_id.final_price', string='Price', readonly=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price
