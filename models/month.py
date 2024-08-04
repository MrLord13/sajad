from odoo import fields, models, api


class SajadMonth(models.Model):
    _name = 'sajad.month'
    _description = 'دوره / ماه'

    name = fields.Char(string='نام دوره')
    con_tarakonesh = fields.One2many('sajad.tarakonesh', 'con_month', string='تراکنش')
    tarikh_shoro = fields.Date(string='تاریخ شروع')
    tarikh_payan = fields.Date(string='تاریخ پایان')
    month = fields.Selection([
        ('farvardin', 'فروردین'),
        ('ordibehesht', 'اردیبهشت'),
        ('khordad', 'خرداد'),
        ('tir', 'تیر'),
        ('mordad', 'مرداد'),
        ('shahrivar', 'شهریور'),
        ('mehr', 'مهر'),
        ('aban', 'آبان'),
        ('azar', 'آذر'),
        ('dey', 'دی'),
        ('bahman', 'بهمن'),
        ('esfand', 'اسفند'),
    ], string="ماه")
    year = fields.Char(string='سال')
    con_sandogh = fields.Many2one('sajad.sandogh', string='صندوق')
    miangin_dore = fields.Char(string='میانگین حساب دوره', compute='_compute_miangin_dore')

    @api.depends('con_tarakonesh')
    def _compute_miangin_dore(self):
        for rec in self:
            miangin_dore = 0
            for tarakonesh in rec.con_tarakonesh:
                if tarakonesh.noe_tarakonesh == 'variz':
                    miangin_dore += int(tarakonesh.mablagh)
                else:
                    miangin_dore -= int(tarakonesh.mablagh)
            rec.miangin_dore = miangin_dore
