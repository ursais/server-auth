# Copyright 2015 LasLabs Inc.
# Copyright 2018 Modoolar <info@modoolar.com>.
# Copyright 2019 initOS GmbH
# Copyright 2020 Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "Password Security",
    "summary": "Allow admin to set password security requirements.",
    "version": "13.0.0.1.0",
    "author": "LasLabs, "
    "Kaushal Prajapati, "
    "Tecnativa, "
    "initOS GmbH, "
    "Open Source Integrators,"
    "Odoo Community Association (OCA)",
    "category": "Base",
    "depends": [
        "auth_signup",
        "auth_password_policy_signup",
    ],
    "external_dependencies": {
        "python": ["zxcvbn"],
    },
    "website": "https://github.com/OCA/server-auth",
    "license": "LGPL-3",
    "data": [
        "views/password_security.xml",
        "views/res_config_settings_views.xml",
        "security/ir.model.access.csv",
        "security/res_users_pass_history.xml",
        "views/res_company_view.xml",
    ],
    "demo": [
        "demo/res_users.xml",
    ],
    "installable": True,
}
