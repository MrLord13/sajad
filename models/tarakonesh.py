from odoo import fields, models, api


class SajadTarakonesh(models.Model):
    _name = 'sajad.tarakonesh'
    _description = 'تراکنش'

    name = fields.Char(string='عنوان تراکنش')
    con_mostajer = fields.Many2one('sajad.mostajer', string='مستاجر')
    con_month = fields.Many2one('sajad.month', string='دوره')
    con_sandogh = fields.Many2one('sajad.sandogh', string='صندوق')
    noe_tarakonesh = fields.Selection([
        ('pardakht', 'پرداخت'),
        ('bardasht', 'برداشت'),
    ], string="نوع تراکنش")
    elat_tarakonesh = fields.Char(string='علت تراکنش')
    mablagh = fields.Char(string='مبلغ')
    tarikh_tarakonesh = fields.Datetime(string='تاریخ تراکنش')
    peyvast = fields.Binary(string='پیوست تراکنش')
    tozihat = fields.Text('توضیحات تکمیلی')

