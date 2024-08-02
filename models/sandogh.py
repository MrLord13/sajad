from odoo import fields, models, api


class SajadSandogh(models.Model):
    _name = 'sajad.sandogh'
    _description = 'صندوق'

    name = fields.Char()
