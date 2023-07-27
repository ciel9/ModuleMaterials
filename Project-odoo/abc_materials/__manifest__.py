# -*- coding: utf-8 -*-
{
    'name': "Supplier-Materials",

    'summary': """
       web supply of goods from suppliers """,

    'description': """
         In addition, clients must also be able to:
         Seeing all the materials that have been made, the client must also be able to filter
         based on MaterialType,Updating one material,Delete one material.
    """,

    'author': "Yohana Cindy Elsanjaya",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Material',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/supplier_list_template.xml',
        'views/supplier_materials.xml'
        ,

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}