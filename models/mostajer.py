from odoo import fields, models, api


class SajadMostajer(models.Model):
    _name = 'sajad.mostajer'
    _description = 'مستاجر'

    name = fields.Char(string='نام واحد')
    con_tarakonesh = fields.One2many('sajad.tarakonesh', 'con_mostajer', string='تراکنش')
    nam = fields.Char(string='نام')
    nam_khanevadegi = fields.Char(string='نام خانوادگی')
    parking = fields.Boolean(string='پارکینگ')
    phone1 = fields.Char(string='شماره تماس 1')
    phone2 = fields.Char(string='شماره تماس 2')
    metraj = fields.Selection([
        ('shast', 'واحد 60 متری'),
        ('chehel', 'واحد 40 متری'),
    ], string="متراژ")
    shomare_kart = fields.Char(string='شماره کارت')
    tozihat = fields.Text('توضیحات تکمیلی')
    full_name = fields.Char(string='نام و نام خانوادگی', compute='_compute_namayesh_kamel_nam', index=True, store=True)

    @api.depends('nam', 'nam_khanevadegi')
    def _compute_namayesh_kamel_nam(self):
        """
        نمایش نام و نام خانوادگی به صورت کامل
        """
        for rec in self:
            if rec.nam and rec.nam_khanevadegi:
                rec.full_name = rec.nam + ' ' + rec.nam_khanevadegi
            else:
                rec.full_name = ' '
