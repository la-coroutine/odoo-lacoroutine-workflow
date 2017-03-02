# -*- coding: utf-8 -*-
{ 
   'name': 'La Coroutine Workflow', 
   'version': '1.0.2', 
   'summary': 'La Coroutine internal workflow',
   'description': """
La Coroutine workflow for orders
======================================================================

A cron job that automatically process orders and generate invoices.""",
   'category': 'Accounting & Finance', 
   'author': 'Alkivi (alkivi.fr)',
   'website': 'http://www.lacoroutine.org',
   'depends' : ['base', 'account'],
   'data': [ 
       'security/ir.model.access.csv',
       'views/lacoroutine.xml',
   ], 
   'installable': True,
   'application': True,
} 
