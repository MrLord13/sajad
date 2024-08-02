from odoo import fields, models, api


class SajadSandogh(models.Model):
    _name = 'sajad.sandogh'
    _description = 'صندوق'

    name = fields.Char(string='صندوق')
    mojodi_kol = fields.Char(string='موجودی کل')
    mojodi_kart = fields.Char(string='موجودی کارت')
    con_tarakonesh = fields.One2many('sajad.tarakonesh', 'con_sandogh', string='تراکنش')

