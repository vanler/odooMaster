# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class MassMailingConfiguration(osv.TransientModel):
    _name = 'mass.mailing.config.settings'
    _inherit = 'res.config.settings'

    _columns = {
        'group_mass_mailing_campaign': fields.boolean(
            'Manage Mass Mailing using Campaign',
            implied_group='mass_mailing.group_mass_mailing_campaign',
            help="""Manage mass mailign using Campaigns"""),
    }
