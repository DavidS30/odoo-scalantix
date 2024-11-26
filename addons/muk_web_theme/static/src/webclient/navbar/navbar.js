/** @odoo-module */

import { patch } from '@web/core/utils/patch';
import { useService } from '@web/core/utils/hooks';

import { NavBar } from '@web/webclient/navbar/navbar';
import { AppsMenu } from "@muk_web_theme/webclient/appsmenu/appsmenu";
import { useEffect, useRef } from "@odoo/owl";


patch(NavBar.prototype, {
	setup() {
        super.setup();
        this.appMenuService = useService('app_menu');
        this.menuButtonRef = useRef('menu_button');
        this.menuIconRef = useRef('menu_icon');
        this.dropdownRef = useRef('dropdown_items');
        this.typeArrowIcon = "oi-arrow-left";
        useEffect(() => this._updateMenuAppsIcon(), () => []);
        this.action = this.action.bind(this);
    },

    _updateMenuAppsIcon() {
        if (this.menuButtonRef && this.menuButtonRef.el && this.menuIconRef && this.menuIconRef.el) {
        this.menuButtonRef.el.addEventListener("mouseenter", () => {
            setTimeout(() => {
                this.menuIconRef.el.classList.remove("oi-apps");
                this.menuIconRef.el.classList.add(this.typeArrowIcon);
            }, 300);
          });
          
          this.menuButtonRef.el.addEventListener("mouseleave", () => {
            this.menuIconRef.el.classList.remove("oi-arrow-right"); // Quita la clase nueva
            this.menuIconRef.el.classList.remove("oi-arrow-left"); // Quita la clase nueva
            this.menuIconRef.el.classList.add("oi-apps"); // Vuelve a la clase original
          });

          this.menuButtonRef.el.addEventListener("click", () => {
            if (this.typeArrowIcon === "oi-arrow-left") {
              this.typeArrowIcon = "oi-arrow-right";
            }else{
              this.typeArrowIcon = "oi-arrow-left";
            }
          });

        }
    },

    action(app){
      app.action();
      this.typeArrowIcon = "oi-arrow-left";
    }
});

patch(NavBar, {
    components: {
        ...NavBar.components,
        AppsMenu,
    },
});
