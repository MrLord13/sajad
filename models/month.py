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
