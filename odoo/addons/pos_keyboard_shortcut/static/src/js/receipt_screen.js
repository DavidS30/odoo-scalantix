/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
patch(ReceiptScreen.prototype, {
    setup() {
        super.setup();
        this._onKeyDown = this._onKeyDown.bind(this); // Aseguramos el contexto
        this.keyAllowed = true;
        this.receipt_screen_shortcuts();
    },

    receipt_screen_shortcuts() {
        if (this.pos.config.enable_keyboard_shortcuts && this.keyAllowed) {
            owl.useExternalListener(document, 'keydown', this._onKeyDown);
            this.keyAllowed = false;
        }
    },
    _onKeyDown(event) {
        const tagName = event.target.tagName.toLowerCase();
        if (tagName === 'input' || tagName === 'textarea' || tagName === 'select') {
            return;
        }
        event.preventDefault();
        if (event.ctrlKey && event.key === this.pos.keyboard_shortcuts[0].print_receipt.toLowerCase()) {
            this.pos.printReceipt();
        }
        if (event.ctrlKey && event.key === this.pos.keyboard_shortcuts[0].new_order.toLowerCase()) {
            this.orderDone();
            this.removeEventKeyDown();
        }
        if (event.ctrlKey && event.key === this.pos.keyboard_shortcuts[0].sent_email.toLowerCase()) {
            this.actionSendReceiptOnEmail();
        }
    },
    removeEventKeyDown() {
        document.removeEventListener('keydown', this._onKeyDown);
        this.keyAllowed = true;
    },
});
