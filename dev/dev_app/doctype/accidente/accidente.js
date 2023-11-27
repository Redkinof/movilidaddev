// Copyright (c) 2023, Alejandro Hernandez and contributors
// For license information, please see license.txt

frappe.ui.form.on("ACCIDENTE", {
	refresh(frm) {
        frm.get_field("latitud_y_longitud").map.setView([21.485202, -104.877471],13);
	},
});
