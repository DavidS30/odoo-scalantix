/** @odoo-module */
import { Component } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";



export class ShortcutPopup extends Component {
    static template = "pos_keyboard_shortcut.ShortcutPopup";
    static props = {
        title: { type: String, optional: true },
        cancelText: { type: String, optional: true },
        close: { type: Function }, // Inyectado por el servicio de diálogos
    };
    static defaultProps = {
        title: _t("Keyboard Shortcuts"),
        cancelText: _t("Close"),
    };

    cancel() {
        this.props.close();
    }
}