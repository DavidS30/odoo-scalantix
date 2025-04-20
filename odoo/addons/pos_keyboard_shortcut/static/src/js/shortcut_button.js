/** @odoo-module */
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { ShortcutPopup } from "./shortcut_popup";
import { ErrorPopup } from "./error_popup";
import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";

patch(ControlButtons.prototype, {
    setup() {
        super.setup();
    },

    async clickButtonCustom() {
        console.log("Custom button clicked | Rey David Testeando");
        if (this.pos.config.enable_keyboard_shortcuts) {
            this.dialog.add(ShortcutPopup, {
                title: _t("Keyboard Shortcuts"),
            });
        } else {
            await this.showPopup(ErrorPopup, {
                title: _t("Warning"),
            });
        }
    },
    async showPopup(PopupComponent, props) {
        return new Promise((resolve) => {
            this.dialog.add(PopupComponent, {
                ...props,
                close: () => resolve(false),
            });
        });
    }
});
