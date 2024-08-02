from odoo import fields, models, api


class SajadMonth(models.Model):
    _name = 'sajad.month'
    _description = 'دوره / ماه'

    name = fields.Char()
