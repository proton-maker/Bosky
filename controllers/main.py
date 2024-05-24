from odoo import http
from odoo.http import request

class BoskyStore(http.Controller):

    @http.route(['/shop'], type='http', auth='public', website=True)
    def shop(self, **kwargs):
        products = request.env['bosky_store.product'].search([])
        return request.render('bosky_store.shop_page', {'products': products})

    @http.route(['/shop/product/<model("bosky_store.product"):product>'], type='http', auth='public', website=True)
    def product(self, product, **kwargs):
        return request.render('bosky_store.product_page', {'product': product})

    @http.route(['/shop/cart'], type='http', auth='public', website=True)
    def cart(self, **kwargs):
        cart = request.env['bosky_store.cart'].search([('customer_id', '=', request.env.user.partner_id.id)], limit=1)
        if not cart:
            cart = request.env['bosky_store.cart'].create({'customer_id': request.env.user.partner_id.id})
        return request.render('bosky_store.cart_page', {'cart': cart})

    @http.route(['/shop/cart/add/<model("bosky_store.product"):product>'], type='http', auth='public', website=True)
    def add_to_cart(self, product, **kwargs):
        cart = request.env['bosky_store.cart'].search([('customer_id', '=', request.env.user.partner_id.id)], limit=1)
        if not cart:
            cart = request.env['bosky_store.cart'].create({'customer_id': request.env.user.partner_id.id})
        cart_line = request.env['bosky_store.cart.line'].search([('cart_id', '=', cart.id), ('product_id', '=', product.id)], limit=1)
        if cart_line:
            cart_line.quantity += 1
        else:
            request.env['bosky_store.cart.line'].create({'cart_id': cart.id, 'product_id': product.id, 'quantity': 1})
        return request.redirect('/shop/cart')

    @http.route(['/shop/checkout'], type='http', auth='public', website=True)
    def checkout(self, **kwargs):
        cart = request.env['bosky_store.cart'].search([('customer_id', '=', request.env.user.partner_id.id)], limit=1)
        if cart:
            cart.action_pay()
        return request.redirect('/shop')
