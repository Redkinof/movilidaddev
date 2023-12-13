// Copyright (c) 2023, Alejandro Hernandez and contributors
// For license information, please see license.txt

frappe.ui.form.on("ACCIDENTE", {
	refresh(frm) {
        frm.get_field("latitud_y_longitud").map.setView([21.485202, -104.877471],13);
		frm.fields_dict.localidad.get_query = function(doc) {
			return {
				filters: {
					municipio: doc.municipio
				}
			}
		}
		frappe.call({
			method: "dev.dev_app.doctype.accidente.accidente.get_Contadores",
			args: {papa: frm.doc.name},
			freeze: false,
			freeze_message: "Espera porfavor",
			callback: function(r){
				frm.set_value("lesionados",r.message[0] + "");
				frm.set_value("hospitalizados",r.message[1] + "");
				frm.set_value("fallecidos",r.message[2] + "");
			}
		});
	},
	before_save(frm){
		frappe.call({
			method: "dev.dev_app.doctype.accidente.accidente.get_Contadores",
			args: {papa: frm.doc.name},
			freeze: false,
			freeze_message: "Espera porfavor",
			callback: function(r){
				frm.set_value("lesionados",r.message[0] + "");
				frm.set_value("hospitalizados",r.message[1] + "");
				frm.set_value("fallecidos",r.message[2] + "");
				frm.set_value("total_de_vehiculos_participantes",r.message[3] + "");
			}
		});
	},
	after_save(frm){
		frappe.call({
			method: "dev.dev_app.doctype.accidente.accidente.get_Contadores",
			args: {papa: frm.doc.name},
			freeze: false,
			freeze_message: "Espera porfavor",
			callback: function(r){
				frm.set_value("lesionados",r.message[0] + "");
				frm.set_value("hospitalizados",r.message[1] + "");
				frm.set_value("fallecidos",r.message[2] + "");
				frm.set_value("total_de_vehiculos_participantes",r.message[3] + "");
			}
		});
	}
});
