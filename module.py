# -*- coding: utf-8 -*-

import logging

from openerp import pooler, tools
from openerp import SUPERUSER_ID
from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
from openerp.addons import account
import openerp.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class lacoroutine_workflow(osv.osv_memory):
    _name = 'lacoroutine.workflow'

    def do_cron(self, cr, uid, ids, context=None):
        '''
        Take all order in 'A Facturer' state
        Generate invoice
        Send invoice to customer
        Mark invoice as open
        '''
        return None
