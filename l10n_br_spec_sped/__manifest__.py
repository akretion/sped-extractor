# -*- coding: utf-8 -*-
# Copyright 2018 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'L10n Br Spec Sped',
    'description': """
        Tabelas do SPED (ECD, ECF, EFD e FCI), geridas a partir da lib python-sped""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'www.akretion.com',
    'depends': ['base'],
    'data': [
        'views/ecd.xml',
        'views/ecf.xml',
        'views/efd_icms_ipi.xml',
        'views/efd_pis_cofins.xml',
#        'views/fci.xml',
    ],
    'demo': [
    ],
}
