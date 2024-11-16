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
        const isDesktop = window.innerWidth >= 768;
        useEffect(() => this._updateMenuAppsIcon());
    },
    _updateMenuAppsIcon() {
        if (this.menuButtonRef && this.menuButtonRef.el && this.menuIconRef && this.menuIconRef.el) {
        this.menuButtonRef.el.addEventListener("mouseenter", () => {
            setTimeout(() => {
                this.menuIconRef.el.classList.remove("oi-apps");
                this.menuIconRef.el.classList.add("oi-arrow-left");
            }, 300);
          });
          
          // Evento al quitar el mouse
          this.menuButtonRef.el.addEventListener("mouseleave", () => {
            this.menuIconRef.el.classList.remove("oi-arrow-left"); // Quita la clase nueva
            this.menuIconRef.el.classList.add("oi-apps"); // Vuelve a la clase original
          });
        }
    }
});

patch(NavBar, {
    components: {
        ...NavBar.components,
        AppsMenu,
    },
});
