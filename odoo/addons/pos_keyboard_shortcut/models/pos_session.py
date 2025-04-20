# -*- coding: utf-8 -*-

from odoo import models


class PosSession(models.Model):
    """inherited the pos session and loaded models to pos"""
    _inherit = 'pos.session'

    def _load_pos_data_models(self, config_id):
        """load the models to pos"""
        res = super()._load_pos_data_models(config_id)
        res.append('pos.keyboard.shortcut')
        res.append('pos.payment.method.key')
        return res

    def _loader_params_pos_keyboard_shortcut(self):
        """To load pos keyboard shortcut fields in pos"""
        return {
            'search_params': {
                'fields': [],
                'domain': [('id', '=', self.config_id.select_shortcut_id.id)]
            },
        }

    def _get_pos_ui_pos_keyboard_shortcut(self, params):
        """set the get function for return the fields values"""
        return self.env['pos.keyboard.shortcut'].search_read(
            **params['search_params'])

    def _loader_params_pos_payment_method_key(self):
        """To load pos payment method key fields in pos"""
        return {
            'search_params': {
                'fields': [],
                'domain': [('keyboard_shortcut_id', '=',
                            self.config_id.select_shortcut_id.id)]
            },
        }

    def _get_pos_ui_pos_payment_method_key(self, params):
        """set the get function for return the fields values"""
        return self.env['pos.payment.method.key'].search_read(
            **params['search_params'])
