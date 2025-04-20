# -*- coding: utf-8 -*-
from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    enable_keyboard_shortcuts = fields.Boolean(
        string='Keyboard shortcuts',
        help='Enable the feature for keyboard shortcuts '
             'using on the point of sale')
    select_shortcut_id = fields.Many2one(
        'pos.keyboard.shortcut',
        string='Choose Shortcut', help='To select pos keyboard shortcut'
    )
