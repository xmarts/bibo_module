# -*- coding: utf-8 -*-
{
    'name': "Ticket de empleados BIBO",

    'summary': """
        Generación y asignacion de tickets para los empleados de BIBO""",

    'description': """
        Genera tickets de manera seriada para las ordenes de trabajo para luego estos ser asignados a un empleado.
    """,

    'author': "Xmarts",
    'website': "https://xmarts.com",

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
