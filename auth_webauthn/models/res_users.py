# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.addons.base.models.res_users import check_identity


class ResUsers(models.Model):
    _inherit = 'res.users'

    webauthn_key_ids = fields.One2many('webauthn.key', 'user_id', string='Webauthn keys')

    @check_identity
    def action_create_webauthn_key(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Create Webauthn Key',
            'res_model': 'webauthn.key',
            'view_mode': 'form',
            'target': 'new',
            'view_id': self.env.ref('auth_webauthn.webauthn_key_view_form_create').id,
        }
