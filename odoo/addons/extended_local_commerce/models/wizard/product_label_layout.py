from odoo import fields, models

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(selection_add=[
        ('extended_dymo', 'Dymo 3x1')
    ], ondelete={'extended_dymo': 'set default'}, default='extended_dymo')

    def _prepare_report_data(self):
        xml_id, data = super()._prepare_report_data()
        if self.print_format == 'extended_dymo':
            xml_id = 'extended_local_commerce.report_product_template_label_dymo_3x1'
        return xml_id, data