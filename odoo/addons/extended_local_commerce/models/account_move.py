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
                        line[2]['tax_ids'] = [(6, 0, [iva_tax.id])]  # Se le asigna el IVA

        return super().create(vals_list)