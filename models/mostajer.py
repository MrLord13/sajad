from odoo import fields, models, api


class SajadMostajer(models.Model):
    _name = 'sajad.mostajer'
    _description = 'مستاجر'

    name = fields.Char()
