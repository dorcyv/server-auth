# -*- coding: utf-8 -*-
{
    "name": "Webauthn Login",
    "summary": "tools",
    "version": "16.0.0.0.0",
    "category": "Tools",
    "website": "https://github.com/OCA/server-auth",
    "author": "Valérian DORCY, Odoo Community Association (OCA)",
    "maintainers": ["Valérian DORCY"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "web",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/ir_rule.xml",
        "views/res_users_views.xml",
        "views/webauthn_key_views.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "auth_webauthn/static/src/views/webauthn_key_form_view.js"
        ]
    }
}
