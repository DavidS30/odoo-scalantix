from odoo import http
from odoo.http import request

class SubscriptionController(http.Controller):
    
    @http.route('/my/subscriptions', type='http', auth='user', website=True)
    def subscription_dashboard(self):
        # Obtener las suscripciones del usuario actual
        subscriptions = request.env['subscription.management'].search([('customer_id', '=', request.env.user.partner_id.id)])
        return request.render('subscription_management.dashboard_template', {
            'subscriptions': subscriptions,
        })