# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from openerp.osv import fields, osv
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)


class sale_configuration(osv.TransientModel):
    _inherit = 'sale.config.settings'

    _columns = {
        'timesheet': fields.boolean('Prepare invoices based on timesheets',
            help='For modifying account analytic view to show important data to project manager of services companies.'
                 'You can also view the report of account analytic summary user-wise as well as month wise.\n'
                 '-This installs the module sale_contract.'),
        'module_sale_contract': fields.boolean('Use contracts management',
            help='Allows to define your customer contracts conditions: invoicing '
                 'method (fixed price, on timesheet, advance invoice), the exact pricing '
                 '(650€/day for a developer), the duration (one year support contract).\n'
                 'You will be able to follow the progress of the contract and invoice automatically.\n'
                 '-It installs the sale_contract module.'),
        'group_sale_pricelist':fields.boolean("Use pricelists to adapt your price per customers",
            implied_group='product.group_sale_pricelist',
            help="""Allows to manage different prices based on rules per category of customers.
Example: 10% for retailers, promotion of 5 EUR on this product, etc."""),
        'group_uom':fields.boolean("Allow using different units of measure",
            implied_group='product.group_uom',
            help="""Allows you to select and maintain different units of measure for products."""),
        'group_discount_per_so_line': fields.boolean("Allow setting a discount on the sales order lines",
            implied_group='sale.group_discount_per_so_line',
            help="Allows you to apply some discount per sales order line."),
        'group_display_incoterm':fields.boolean("Display incoterms on the printed sale orders and invoices reports",
            implied_group='sale.group_display_incoterm',
            help="The printed reports will display the incoterms for the sale orders and the related invoices"),
        'module_warning': fields.boolean("Allow configuring alerts by customer or products",
            help='Allow to configure notification on products and trigger them when a user wants to sell a given product or a given customer.\n'
                 'Example: Product: this product is deprecated, do not purchase more than 5.\n'
                 'Vendor: don\'t forget to ask for an express delivery.'),
        'module_sale_margin': fields.boolean("Display margins on sales orders",
            help='This adds the \'Margin\' on sales order.\n'
                 'This gives the profitability by calculating the difference between the Unit Price and Cost Price.\n'
                 '-This installs the module sale_margin.'),
        'module_sale_layout': fields.boolean("Allow to categorize sale order lines",
            help='Allows to create categories to structure lines in pdf reports.\n'
                 '-This installs the module sale_layout.'),
        'module_website_quote': fields.boolean("Allow online quotations and templates",
            help='This adds the online quotation'),
        'module_sale_journal': fields.boolean("Allow batch invoicing of delivery orders through journals",
            help='Allows you to categorize your sales and deliveries (picking lists) between different journals, '
                 'and perform batch operations on journals.\n'
                 '-This installs the module sale_journal.'),
        'module_analytic_user_function': fields.boolean("One employee can have different roles per contract",
            help='Allows you to define what is the default function of a specific user on a given account.\n'
                 'This is mostly used when a user encodes his timesheet. The values are retrieved and the fields are auto-filled. '
                 'But the possibility to change these values is still available.\n'
                 '-This installs the module analytic_user_function.'),
        'module_project': fields.boolean("Project"),
        'module_sale_stock': fields.boolean("Trigger delivery orders automatically from sales orders",
            help='Allows you to Make Quotation, Sale Order using different Order policy and Manage Related Stock.\n'
                 '-This installs the module sale_stock.'),
        'group_sale_delivery_address': fields.boolean("Allow a different address for delivery and invoicing ",
            implied_group='sale.group_delivery_invoice_address',
            help="Allows you to specify different delivery and invoice addresses on a sales order."),
    }

    def set_sale_defaults(self, cr, uid, ids, context=None):
        return {}

    def onchange_task_work(self, cr, uid, ids, task_work, context=None):
        if not task_work:
            return {'value': {}}
        return {'value': {
            'module_project_timesheet': task_work,
            'module_sale_service': task_work,
        }}

    def onchange_timesheet(self, cr, uid, ids, timesheet, context=None):
        return {'value': {
            'timesheet': timesheet,
            'module_sale_contract': timesheet,
        }}

class account_config_settings(osv.osv_memory):
    _inherit = 'account.config.settings'
    _columns = {
        'group_analytic_account_for_sales': fields.boolean('Analytic accounting for sales',
            implied_group='sale.group_analytic_accounting',
            help="Allows you to specify an analytic account on sales orders."),
    }
