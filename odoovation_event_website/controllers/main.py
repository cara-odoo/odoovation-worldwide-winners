import werkzeug

from odoo import http, _
from odoo.http import request

from odoo.addons.website_event.controllers.main import WebsiteEventController

class WebsiteLunchEventController(WebsiteEventController):
    @http.route(['/event/<model("event.event"):event>/registration_lunch/new'], type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def registration_new_lunch(self, event, **post):
        tickets = event.sudo().event_ticket_ids.filtered(lambda t: str(t.id) in post.values())
        registrations = request.env['event.registration']
        for ticket in tickets:
            ticket.seats_taken += 1
            registrations += request.env['event.registration'].sudo().create({
                'name': request.env.user.name,
                'email': request.env.user.email,
                'event_id': event.id,
                'event_ticket_id': ticket.id
            })
        
        return request.redirect(('/event/%s/registration/success?' % event.id) + werkzeug.urls.url_encode({'registration_ids': ",".join([str(id) for id in registrations.ids])}))
