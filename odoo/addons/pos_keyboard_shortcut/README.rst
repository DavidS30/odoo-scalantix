===========================================================
Odoo POS Keyboard Shortcut Module
===========================================================

**Author**: David Salas, CEO of Scalantix
**All Rights Reserved**: Scalantix

Overview
--------

The **Odoo POS Keyboard Shortcut** module enhances the Point of Sale (POS) system by introducing customizable keyboard shortcuts for faster and more efficient operations. This module is designed to improve the user experience by allowing users to perform common actions using keyboard combinations, reducing reliance on mouse interactions.

Features
--------

- **Customizable Keyboard Shortcuts**:
  - Enable or disable keyboard shortcuts from the POS configuration.
  - Define specific key combinations for various actions.

- **Supported Actions**:
  - Print receipt (`Ctrl + P` by default).
  - Create a new order (`Ctrl + N` by default).
  - Send receipt via email (`Ctrl + E` by default).
  - Navigate back to the product screen (`Ctrl + B` by default).
  - Validate an order (`Ctrl + V` by default).
  - Add payment methods using predefined shortcuts.

- **Context-Aware Behavior**:
  - Shortcuts are disabled when the user is typing in input fields, textareas, or select elements to avoid interference.

Installation
------------

1. Copy the module folder `pos_keyboard_shortcut` into your Odoo `addons` directory.
2. Restart the Odoo server:
   ```bash
   ./odoo-bin -c /path/to/your/odoo.conf -u pos_keyboard_shortcut