/** @odoo-module */
/** @odoo-module */
import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

export class ErrorPopup extends Component {
    static template = "pos_keyboard_shortcut.ErrorPopup";
    static props = {
        title: { type: String, optional: true },
        body: { type: String, optional: true },
        cancelText: { type: String, optional: true },
        close: { type: Function },
    };

    static defaultProps = {
        cancelText: _t("Close"),
        title: _t("WARNING"),
    };

    setup() {
        this.dialog = useService("dialog");
    }

}