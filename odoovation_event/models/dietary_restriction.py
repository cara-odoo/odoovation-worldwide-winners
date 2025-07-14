from odoo import fields, models


class DietaryRestriction(models.Model):
    _name = 'dietary.restriction'
    _description = 'Dietary Restriction'

    name = fields.Char(
        string='Name',
        required=True,
        help='Name of the dietary restriction, e.g., Vegetarian, Vegan, Gluten-Free.'
    )

    description = fields.Text(
        string='Description',
        help='Detailed description of the dietary restriction.'
    )


    