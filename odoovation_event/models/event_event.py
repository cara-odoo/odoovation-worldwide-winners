from odoo import fields, models


class EventEvent(models.Model):
    _inherit = 'event.event'
    _description = 'Lunch Menus'

    @property
    def users_to_notify(self):
        location = self.env['hr.work.location'].search([('name', 'ilike', 'Odoo Buffalo')], limit=1)
        all_users = self.env['res.users'].search([
            ('work_location_id', '=', location.id)
        ])
        registered_users = self.registration_ids.mapped('partner_id.user_id')
        return all_users - registered_users

    def action_send_registration_remainder(self):
        odoo_bot_id = self.env['res.users'].sudo().search([('login', '=', '__system__')], limit=1)
        
        for event in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            for user in event.users_to_notify:
                self.env['mail.mail'].sudo().create({
                    'subject': f"Lunch Registration Reminder: {event.name}",
                    'email_to': user.email,
                    'email_from': odoo_bot_id.email,
                    'body_html': f"""
                        <p>Hello {user.name},</p>
                        <p>Please register for the lunch event: {event.name}.</p>
                        <p><a href="{base_url}{event.website_url}">Click here to register</a></p>
                    """,
                    'auto_delete': False,
                }).send()