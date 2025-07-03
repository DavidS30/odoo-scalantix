from odoo import models, api

class SaleReportInherited(models.AbstractModel):
    _inherit = 'report.point_of_sale.report_saledetails'

    @api.model
    def get_sale_details(self, date_start=False, date_stop=False, config_ids=False, session_ids=False, **kwargs):
        # total neto without cashbox
        sale_details = super().get_sale_details(date_start, date_stop, config_ids, session_ids, **kwargs)
        payment_cash = [payment for payment in sale_details['payments'] if payment['name'].startswith('Efectivo') and payment.get('cash', False)]
        payment_cash = payment_cash[0] if payment_cash else None
        total_countent_cash = payment_cash['final_count'] if payment_cash else 0
        total_amount_cash_box = [move for move in payment_cash['cash_moves'] if move['name'] == 'Apertura de caja']
        total_amount_cash_box = total_amount_cash_box[0]['amount'] if total_amount_cash_box else 0
        total_without_cash_box = total_countent_cash - total_amount_cash_box
        sale_details['total_without_cash_box'] = total_without_cash_box

        # total outs of cashbox
        total_negative_moves = sum(move['amount'] for move in payment_cash['cash_moves'] if move['amount'] < 0)
        sale_details['total_negative_moves'] = total_negative_moves

        return sale_details