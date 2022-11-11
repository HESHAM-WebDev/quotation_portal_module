# -*- coding: utf-8 -*-
{
    'name': "quotation web portal",

    'summary': """
        help to create quotation from portal""",

    'description': """
        help to create quotation from portal
    """,

    'author': "Hesham Magdy",
    'website': "https://github.com/HESHAM-WebDev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'web portal',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "website"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/web_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,

}
