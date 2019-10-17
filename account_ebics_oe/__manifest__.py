# Copyright 2019 Noviat.
# License LGPL-3 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'account_ebics on Odoo Enterprise',
    'summary': "Deploy account_ebics module on Odoo Enterprise",
    'version': '12.0.1.0.0',
    'author': 'Noviat',
    'category': 'Hidden',
    'license': 'LGPL-3',
    'installable': True,
    'depends': [
        'account_ebics',
        'account_accountant',
    ],
    'data': [
        'views/account_ebics_menu.xml'
    ],
    'installable': True,
    'auto_install': True,
}
