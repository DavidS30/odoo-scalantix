from odoo import models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        """Añade automáticamente el IVA a cada línea de factura creada."""
        iva_tax = self.env['account.tax'].search([('type_tax_use', '=', 'sale')], limit=1)

        if iva_tax:
            for vals in vals_list:
                if 'invoice_line_ids' in vals:
                    for line in vals['invoice_line_ids']:
                        line_data = line[2]
                        tax_data = line_data.get('tax_ids')
                        if tax_data and not tax_data[0][2]:
                            total_tax_adjust = 1 + iva_tax.amount / 100
                            # Ajustar el precio unitario con redondeo
                            adjusted_price = round(line_data['price_unit'] / total_tax_adjust, 2)
                            # Recalcular el precio total con el IVA para verificar
                            recalculated_total = round(adjusted_price * total_tax_adjust, 2)
                            # Corregir cualquier diferencia para que coincida con el precio original
                            difference = line_data['price_unit'] - recalculated_total
                            if abs(difference) > 0.01:  # Si hay una diferencia significativa
                                adjusted_price += difference / total_tax_adjust
                            line_data['price_unit'] = round(adjusted_price, 2)
                            line_data['tax_ids'] = [(6, 0, [iva_tax.id])]  # Se le asigna el IVA

        return super().create(vals_list)