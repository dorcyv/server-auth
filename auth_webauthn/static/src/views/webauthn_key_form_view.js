/** @odoo-module **/

import {FormController} from "@web/views/form/form_controller";
import {useService} from "@web/core/utils/hooks";
import {registry} from "@web/core/registry";
import {formView} from "@web/views/form/form_view";

export class WebauthnKeyController extends FormController {
    setup() {
        super.setup();
        this.orm = useService("orm");
    }

    async getCredentialOptions() {
        let credentialOptions = await this.orm.call("webauthn.key", "generate_registration_options");
        credentialOptions = JSON.parse(credentialOptions);
        credentialOptions.challenge = Uint8Array.from(credentialOptions.challenge, c => c.charCodeAt(0));
        credentialOptions.user.id = Uint8Array.from(credentialOptions.user.id, c => c.charCodeAt(0));

        return credentialOptions;
    }

    async beforeExecuteActionButton(clickParams) {
        const record = this.model.root;
        if (clickParams.name === "action_create_webauthn_key") {
            let credentialOptions = await this.getCredentialOptions();

            const credentialResponse = await navigator.credentials.create({
                publicKey: credentialOptions,
            });
            console.log(credentialResponse);
            clickParams.args = JSON.stringify([{"test": "toto"}]);
        }
        return super.beforeExecuteActionButton(...arguments);
    }
}

export const WebauthnKeyFormView = {
    ...formView,
    Controller: WebauthnKeyController,
};


registry.category("views").add("webauthn_key_form_view", WebauthnKeyFormView);
