from odoo import fields, models


class EventEvent(models.Model):
    _inherit = 'event.event'
    _description = 'Lunch Menus'

    def action_send_registration_remainder(self):
        buffalo_location_id = self.env['hr.work.location'].browse(4)
        # Buffalo location ID can be dynamically fetched or hardcoded as needed.

        for event in self:
            all_users = self.env['res.users'].search([
                ('work_location_id', '=', buffalo_location_id.id)
            ])
            registered_users = event.registration_ids.mapped('partner_id.user_id')
            users_to_notify = all_users - registered_users

            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            
            event.message_post(
                body=f"""
                    <p>Hello,</p>
                    <p>Please register for the lunch event: {event.name}.</p>
                    <p><a href="{base_url}{event.website_url}">Click here to register</a></p>
                """,
                body_is_html=True,
                subject="Lunch Registration Reminder",
                message_type='email',
                partner_ids=users_to_notify.mapped('partner_id.id'),
            )