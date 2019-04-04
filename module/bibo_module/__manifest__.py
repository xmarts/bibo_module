# -*- coding: utf-8 -*-
{
    'name': "bibo_module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Xmarts",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Production',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp','hr','account_accountant', 'account','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/form_ticket.xml',
        'reports/layout.xml',
        'reports/imp_tickets.xml',
        'reports/order.xml',
        'reports/sale_report_templates.xml',
        'reports/account_report_invoice.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'installable' : True
}