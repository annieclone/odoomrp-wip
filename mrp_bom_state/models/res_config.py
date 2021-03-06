# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in root directory
##############################################################################
from openerp import models, fields


class MrpConfigSettings(models.TransientModel):
    _inherit = 'mrp.config.settings'

    group_mrp_bom_state = fields.Boolean(
        string='Allow to re-edit BoMs',
        implied_group='mrp_bom_state.group_mrp_bom_state',
        help='The active state may be passed back to state draft')
