/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
//patch the store and load the models
patch(PosStore.prototype, {
    async setup(loadedData) {
        await super.setup(...arguments);

        this.keyboard_shortcuts = this.data.models['pos.keyboard.shortcut'].getAll();
        this.payment_method_key = this.data.models['pos.payment.method.key'].getAll();
    },
});
