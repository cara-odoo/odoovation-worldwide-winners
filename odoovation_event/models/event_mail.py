from odoo import fields, models


class EventMail(models.Model):
    _inherit = 'event.mail'

    send_registration_reminder = fields.Boolean(
        string='Send Registration Remainder',
        help='If checked, a registration remainder will be sent to users who have not registered for the event.',
        default=False,
    )