from odoo import fields, models


class EventTemplateTicket(models.Model):
    _inherit = 'event.type.ticket'

    def _default_product_id(self):
        return self.env.ref('event_product.product_product_event', raise_if_not_found=False)

    # remove domain of product_id
    product_id = fields.Many2one('product.product', domain=[], string='Product', required=True, default=_default_product_id)
