# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Modulo Extendido para Comercio local Colombiano',
    'version' : '0.1',
    'category': 'Accounting',
    'summary' : 'Modulo Extendido para Comercio local Colombiano',
    'description' : """
Extendido Comercio Local Colombiano
==================================
Con este modulo se busca agrupar todas las funcionalidades muy especificas
del comercio local colombiano.

Caracteristicas Implementadas
-------------
* Añadir Iva automáticamente en facturas cuando se selecciona en el POS esta opción

""",
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
    'license': 'LGPL-3',
}
