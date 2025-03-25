from odoo import models, fields, api


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
                        line_data = line[2];
                        tax_data = line[2]['tax_ids']
                        if tax_data and not tax_data[0][2]:
                            total_tax_adjust = 1 + iva_tax.amount/100;
                            line_data['price_unit'] = line_data['price_unit'] / total_tax_adjust # se ajusta precio inicial para todo con iva
                            line[2]['tax_ids'] = [(6, 0, [iva_tax.id])]  # Se le asigna el IVA

        return super().create(vals_list)