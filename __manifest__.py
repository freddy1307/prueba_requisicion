# -*- coding: utf-8 -*-
{
    'name': "Requisicion de producto",

    'summary': """
        Modulo de prueba para odoo, asemejanza de una requisicion de productos.""",

    'description': """

    """,

    'author': "Luis Alfredo Valencia Diaz",
    'website': "",

    # Categories can be used to filter modules in modules listing
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/moduloprueba_main.xml'
    ]
}
