// Copyright (c) 2024, Alejandro Hernandez and contributors
// For license information, please see license.txt

frappe.ui.form.on("Reporte_Servicio", {
	refresh(frm) {
        var newD = new Date();
        frm.set_value("fecha_de_peticion",newD);
        frm.set_df_property('fecha_de_peticion', 'read_only', 1)
	},
});
