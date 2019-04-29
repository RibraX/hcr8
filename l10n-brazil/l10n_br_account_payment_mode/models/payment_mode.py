# -*- coding: utf-8 -*-
# Copyright (C) 2012-Today - KMEE (<http://kmee.com.br>).
#  @author Luis Felipe Miléo - mileo@kmee.com.br
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PaymentMode(models.Model):
    _inherit = 'payment.mode'

    type_sale_payment = fields.Selection(
        [('01', u'01 - Dinheiro'),
         ('02', u'02 - Cheque'),
         ('03', u'03 - Cartão de Crédito'),
         ('04', u'04 - Cartão de Débito'),
         ('05', u'05 - Crédito Loja'),
         ('10', u'10 - Vale Alimentação'),
         ('11', u'11 - Vale Refeição'),
         ('12', u'12 - Vale Presente'),
         ('13', u'13 - Vale Combustível'),
         ('15', u'15 - Boleto Bancário'),
         ('90', u'90= Sem pagamento'),
         ('99', u'99=Outros')
         ],
        string='Tipo SPED', required=True, default='15')

    type_payment = fields.Selection(
        [('00', u'0 - Pagamento à Vista'),
         ('99', u'1 - Pagamento à Prazo')],
        string='Tipo SPED', required=True, default='0')

    internal_sequence_id = fields.Many2one('ir.sequence', u'Sequência')
    instrucoes = fields.Text(u'Instruções de cobrança')
    invoice_print = fields.Boolean(
        u'Gerar relatorio na conclusão da fatura?')

    _sql_constraints = [
        ('internal_sequence_id_unique',
         'unique(internal_sequence_id)',
         u'Sequência já usada! Crie uma sequência unica para cada modo')
    ]


class PaymentModeType(models.Model):
    _inherit = 'payment.mode.type'
    _description = 'Payment Mode Type'

    payment_order_type = fields.Selection(
        selection_add=[
            ('cobranca', u'Cobrança'),
        ])


class PaymentOrder(models.Model):
    _inherit = 'payment.order'

    payment_order_type = fields.Selection(
        selection_add=[
            ('cobranca', u'Cobrança'),
        ])
