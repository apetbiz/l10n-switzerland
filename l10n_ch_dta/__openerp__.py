# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi. Copyright Camptocamp SA
#    Ported to v8.0 by Agile Business Group <http://www.agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{'name': 'Switzerland - Bank Payment File (DTA)',
 'summary': 'Electronic payment file for Swiss bank (DTA)',
 'version': '9.0.1.0.1',
 'author': "Camptocamp,Odoo Community Association (OCA)",
 'category': 'Localization',
 'website': 'http://www.camptocamp.com',
 'license': 'AGPL-3',
 'depends': ['base', 'l10n_ch_base_bank',
             'l10n_ch_payment_register',
             'document'],
 'data': ["wizard/create_dta_view.xml",
          ],
 'demo': ['../account/test/account_minimal_test.xml',
          "demo/dta_demo.xml"],
 'test': ["test/l10n_ch_dta.yml"],
 'auto_install': False,
 'installable': True,
 'images': []
 }
