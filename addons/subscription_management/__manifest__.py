# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Suscripciones',
    'version': '1.0',
    'summary': 'Módulo para gestionar suscripciones y pagos recurrentes',
    'description': 'Permite a los clientes gestionar sus suscripciones y pagos recurrentes.',
    'author': 'David Salas - Scalantix',
    'depends': ['base', 'sale', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/subscription_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}