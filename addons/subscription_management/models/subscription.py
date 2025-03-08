from odoo import models, fields

class Subscription(models.Model):
    _name = 'subscription.management'
    _description = 'Gestión de Suscripciones'

    name = fields.Char(string='Nombre de la Suscripción', required=True)
    customer_id = fields.Many2one('res.partner', string='Cliente')
    start_date = fields.Date(string='Fecha de Inicio')
    end_date = fields.Date(string='Fecha de Fin')
    state = fields.Selection([
        ('active', 'Activo'),
        ('inactive', 'Inactivo'),
        ('canceled', 'Cancelado'),
    ], string='Estado', default='active')
    payment_method = fields.Char(string='Método de Pago')
    amount = fields.Float(string='Monto')