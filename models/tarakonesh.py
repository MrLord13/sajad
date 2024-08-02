from odoo import fields, models, api


class SajadTarakonesh(models.Model):
    _name = 'sajad.tarakonesh'
    _description = 'تراکنش'

    name = fields.Char()
