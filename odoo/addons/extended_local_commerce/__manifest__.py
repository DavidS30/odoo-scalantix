# -*- coding: utf-8 -*-
################################################################################
# ============> SCALANTIX MODULE <================
# Developer: David Salas (CEO)
# Company: Scalantix
# Website: https://scalantix.com
# Description: This module control the extended functionality of the
#              Local Colombian Commerce
# License: AGPL-3
################################################################################
{
    'name' : 'Extended Local Commerce',
    'author' : 'Scalantix',
    'website' : 'https://scalantix.com',
    'maintainer' : 'Scalantix',
    'version' : '0.1',
    'category': 'Accounting',
    'summary' : 'Modulo Extendido para Comercio local Colombiano',
    'description' : """Extendido Comercio Local Colombiano.
                    Con este modulo se busca agrupar todas las funcionalidades muy especificas
                    del comercio local colombiano.""",
    'depends': [
        'account',
        'point_of_sale'
    ],
    'data': [
        'views/pos_session_sales_details.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'assets': {
        'point_of_sale._assets_pos': [
            'extended_local_commerce/static/src/pos/*',
            'extended_local_commerce/static/src/pos/css/*',
        ],
    },
    'license': 'AGPL-3',
}
