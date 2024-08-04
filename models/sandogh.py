from odoo import fields, models, api


class SajadSandogh(models.Model):
    _name = 'sajad.sandogh'
    _description = 'صندوق'

    name = fields.Char(string='صندوق')
    mojodi_kol = fields.Char(string='موجودی کل', compute='compute_tarakoneshha')
    mojodi_kart = fields.Char(string='موجودی کارت')
    con_month = fields.One2many('sajad.month', 'con_sandogh', string='تراکنش')

    def compute_tarakoneshha(self):
        """
        محاسبه تمامی تراکنش ها و انتقال هایی که به کارت تجارت شده است
        """
        mojodi_kol = 0
        for record in self.con_month:
            print(record.miangin_dore)
            mojodi_kol += int(record.miangin_dore)
        self.mojodi_kol = mojodi_kol