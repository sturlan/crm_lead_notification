# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crm_lead_notification(models.Model):
#     _name = 'crm_lead_notification.crm_lead_notification'
#     _description = 'crm_lead_notification.crm_lead_notification'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
