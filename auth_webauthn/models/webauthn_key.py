# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

from werkzeug.urls import url_parse
import webauthn
from webauthn.registration.generate_registration_options import default_supported_pub_key_algs


class WebauthnKey(models.Model):
    _name = 'webauthn.key'
    _description = 'Webauthn key'

    name = fields.Char('Name', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True, default=lambda x: x.env.user.id)

    def action_create_webauthn_key(self, registration=None):
        self.ensure_one()
        if registration is None:
            raise UserError(_('No registration data provided'))

    @api.model
    def generate_registration_options(self):
        rp_name = self.env['ir.config_parameter'].sudo().get_param('webauthn.rp_name', 'Odoo')
        options = webauthn.generate_registration_options(
            rp_id=url_parse(self.get_base_url()).host,
            rp_name=rp_name,
            user_id=self.env.user.login.encode('utf-8'),
            user_name=self.env.user.name,
            supported_pub_key_algs=default_supported_pub_key_algs,
        )
        return webauthn.options_to_json(options)
