# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Inherited the settings and add new fields"""
    _inherit = 'res.config.settings'

    pos_enable_keyboard_shortcuts = fields.Boolean(
        string='Enable keyboard shortcuts',
        help='Choose Keyboard Shortcut for the POS Session',
        related='pos_config_id.enable_keyboard_shortcuts',
        readonly=False
        )
    pos_select_shortcut_id = fields.Many2one(
        'pos.keyboard.shortcut',
        string='Choose Shortcut',
        related='pos_config_id.select_shortcut_id',
        readonly=False,
        help='To select pos keyboard shortcut'
    )
