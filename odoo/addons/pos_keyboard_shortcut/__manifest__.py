# -*- coding: utf-8 -*-
################################################################################
# ============> SCALANTIX MODULE <================
# Developer: David Salas (CEO)
# Company: Scalantix
# Website: https://scalantix.com
# Description: This module adds keyboard shortcuts to the Point of Sale
#              (POS) system, allowing users to quickly process transactions
#              and navigate through the interface using keyboard keys.
# License: AGPL-3
################################################################################
{
    'name': 'POS Keyboard Shortcut',
    'version': '18.0.1.0.1',
    'summery': 'Module to add keyboard shortcuts in POS',
    'description': """Easily operate the Point of Sale (POS) system by
     utilizing POS keyboard shortcuts.""",
    'author': 'Scalantix',
    'company': 'Scalantix',
    'maintainer': 'Scalantix',
    'website': 'https://www.scalantix.com',
    "category": "point of sale",
    'depends': ['point_of_sale'],
    'data': ['security/ir.model.access.csv',
             'data/pos_keyboard_shortcut_sequence.xml',
             'views/res_config_settings_views.xml',
             'views/pos_keyboard_shortcut_views.xml',
             ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_keyboard_shortcut/static/src/js/*',
            'pos_keyboard_shortcut/static/src/xml/*',
        ],
    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
