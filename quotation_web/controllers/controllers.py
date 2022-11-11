from odoo import http
from odoo.http import request


class AddQuotation(http.Controller):
    @http.route('/add_quotation', auth='public', csrf=False, type='http', website='true')
    def add_quotation(self, **kw):
        customer_record = request.env['res.partner'].sudo().search([])
        price_list_record = request.env['product.pricelist'].sudo().search([])
        quotation_template_record = request.env['sale.order.template'].sudo().search([])
        payment_terms_record = request.env['account.payment.term'].sudo().search([])

        return http.request.render('quotation_web.add_quotation', {
            'customer_record': customer_record,
            'price_list_record': price_list_record,
            'quotation_template_record': quotation_template_record,
            'payment_terms_record': payment_terms_record,

        })

    @http.route('/create_quotation', auth='public', csrf=False, type='http', website=True, method=['POST'])
    def create_quotation(self, **kw):
        request.env['sale.order'].sudo().create({**kw,
                                                 'partner_id': (kw.get('partner_id')),
                                                 'partner_invoice_id': (kw.get('partner_invoice_id')),
                                                 'partner_shipping_id': (kw.get('partner_shipping_id')),
                                                 })
