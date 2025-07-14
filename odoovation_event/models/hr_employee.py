from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    dietary_restriction_ids = fields.Many2many(
        'dietary.restriction',
        string='Dietary Restrictions',
        help='List of dietary restrictions for the user, e.g., Vegetarian, Vegan, Gluten-Free.'
    )