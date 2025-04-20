/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

patch(PaymentScreen.prototype, {
    setup() {
        super.setup();
        this._onKeyDown = this._onKeyDown.bind(this); // Aseguramos el contexto
        this.payment_screen_shortcuts();
    },
    payment_screen_shortcuts() {
        if (this.pos.config.enable_keyboard_shortcuts) {
            document.addEventListener('keydown', this._onKeyDown);
        }
    },
    _onKeyDown(event) {
        event.preventDefault();
        if (event.ctrlKey && event.key === this.pos.keyboard_shortcuts[0].select_invoice.toLowerCase()) {
            const InvoiceButton = document.querySelector('.js_invoice');
            InvoiceButton?.click();
        }
        if (event.ctrlKey && event.key === this.pos.keyboard_shortcuts[0].back_screen.toLowerCase()) {
            this.pos.onClickBackButton();
            this.removeEventKeyDown();
        }
        if (this.pos.payment_method_key) {
            this.pos.payment_method_key.forEach((payment_method) => {
                if (event.ctrlKey && event.key === payment_method.key_code.toLowerCase()) {
                    this.addNewPaymentLine(payment_method.payment_method_id)
                }
            });
        }
        if (event.ctrlKey && event.key === this.pos.keyboard_shortcuts[0].validate_order.toLowerCase()) {
            this.validateOrder();
            this.removeEventKeyDown();
        }
    },
    removeEventKeyDown() {
        document.removeEventListener('keydown', this._onKeyDown);
    },
});
