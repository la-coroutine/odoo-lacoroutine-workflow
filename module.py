# -*- coding: utf-8 -*-

import logging

from openerp import api, fields, models, _

log = logging.getLogger(__name__)

class lacoroutine_workflow(models.TransientModel):
    _name = 'lacoroutine.workflow'
    _description = 'La Coroutine Workflow'

    @api.multi
    def do_cron(self):
        '''
        Take all order in 'A Facturer' state
        Generate invoice
        Send invoice to customer
        Mark invoice as open
        '''
        log.info('Lauching La Coroutine Cron')

        # Select all orders that are in manual state
        search_args = [('state', '=', 'manual')]
        sale_orders = self.env['sale.order'].search(search_args)

        if not sale_orders:
            log.info('No sale order to process')
            return

        # Now for all orders
        for sale_order in sale_orders:
            log.debug('Processing sale.order {0}'.format(sale_order.id))

            # Make invoice
            result = sale_order.manual_invoice()
            # {'view_mode': 'form', 'nodestroy': True, 'name': u'Factures clients', 'context': "{'type':'out_invoice'}", 'view_type': 'form', 'res_model': 'account.invoice', 'view_id': [(469,)], 'type': 'ir.actions.act_window', 'res_id': 958, 'target': 'current'}

            # Now load invoice, mark as open and send email
            invoice_id = result['res_id']
            log.info('Invoice {0} generated'.format(invoice_id))
            invoice = self.env['account.invoice'].browse(invoice_id)
            
            # Make as open
            invoice.signal_workflow('invoice_open')

            # Send email
            template_id = 15
            self.pool.get('email.template').send_mail(self.env.cr, self.env.uid, template_id, invoice.id, True)



        return None
