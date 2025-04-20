# -*- coding: utf-8 -*-

from odoo import fields, models


class PosPaymentMethodKey(models.Model):
    """To create a new model and add new fields for defining shortcut keys
     related to payment methods"""
    _name = 'pos.payment.method.key'
    _description = 'Pos Payment Method Key'

    payment_method_id = fields.Many2one('pos.payment.method',
                                        String='Payment Method',
                                        help='This field represents the payment'
                                             'method used for transactions in '
                                             'the Point of Sale module. '
                                             'It allows users to select from '
                                             'predefined payment methods such '
                                             'as cash, credit card, '
                                             'or gift card when processing '
                                             'payments at the point of sale.')
    keyboard_shortcut_id = fields.Many2one('pos.keyboard.shortcut',
                                           string='Keyboard Shortcuts',
                                           help='This field associates a '
                                                'keyboard shortcut with a '
                                                'specific action or function in'
                                                'the Point of Sale interface. '
                                                'It allows users to quickly '
                                                'perform common tasks by '
                                                'pressing designated keys.')
    key_code = fields.Char(string='Key Code', help='This field stores the code '
                                                   'representing the key '
                                                   'or key combination'
                                                   ' assigned '
                                                   'to the keyboard shortcut. '
                                                   'It is '
                                                   'used to identify the '
                                                   'keystroke needed to '
                                                   'trigger the associated '
                                                   'action or function in '
                                                   'the Point of Sale '
                                                   'interface.')


    def _load_pos_data(self, data):
        config_id = self.env['pos.config'].browse(data['pos.config']['data'][0]['id'])
        fields = ["payment_method_id","keyboard_shortcut_id", "key_code"]
        domain = [('keyboard_shortcut_id', '=',
                            config_id.select_shortcut_id.id)]
        return {
                'fields': fields,
                'data': self.search_read(domain, fields, load=False) if domain is not False else [],
            }