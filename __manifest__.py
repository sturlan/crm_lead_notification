# -*- coding: utf-8 -*-
{
    'name': "crm_lead_notification",

    'summary': """
        User notification for new CRM leads""",

    'description': """
        Send user notification to sales team members when a new CRM lead is created
    """,

    'author': "Servisi RAM d.o.o.",
    'website': "http://www.servisiram.hr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
