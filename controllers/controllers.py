# -*- coding: utf-8 -*-
# from odoo import http


# class CrmLeadNotification(http.Controller):
#     @http.route('/crm_lead_notification/crm_lead_notification/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_lead_notification/crm_lead_notification/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_lead_notification.listing', {
#             'root': '/crm_lead_notification/crm_lead_notification',
#             'objects': http.request.env['crm_lead_notification.crm_lead_notification'].search([]),
#         })

#     @http.route('/crm_lead_notification/crm_lead_notification/objects/<model("crm_lead_notification.crm_lead_notification"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_lead_notification.object', {
#             'object': obj
#         })
