// Copyright (c) 2023, Alejandro Hernandez and contributors
// For license information, please see license.txt
var campos = [
	'nombre',
	'delegacion',
	'nopatrulla',
	'identificacion_agente',
	'fecha_y_hora',
	'municipio',
	'localidad',
	'libramiento_de_tepic',
	'calle_y_no',
	'colonia',
	'entre_calle',
	'peaton',
	'bicicleta',
	'autobus',
	'combi',
	'taxi',
	'camion_de_carga',
	'automovil_particular',
	'motocicleta',
	'vehiculos',
	'peaton_o_ciclista',
	'narrativa_de_los_hechos',
	'tipo_de_accidente',
	'otro_accidente',
	'causa',
	'otra_causa',
	'clase',
	'rh',
	'delito',
	'valoracion_de_danos',
	'total_de_vehiculos_participantes',
	'lesionados',
	'fallecidos',
	'hospitalizados',
	'solo_danos',
	'latitud_y_longitud',
	'nombre_responsable',
	'area',
	'no_de_unidad',
	'identificacion_respondiente',
	'firmas_section',
	'agente_de_movilidad',
];

frappe.ui.form.on("ACCIDENTE", {
	// onload(frm){
	// 	frm.toggle_enable(campos, frm.doc.workflow_state === 'Revision');
	// 	if (frm.doc.workflow_state === 'Revision'){
	// 		frm.set_df_property('comandante_en_turno', 'reqd', 1)
	// 	}
	// 	if (frm.doc.workflow_state === 'Espera Pago'){
	// 		// frm.toggle_enable(campos, frm.doc.workflow_state === 'Espera Pago');
	// 		frm.set_df_property('comandante_en_turno', 'read_only', 1)
	// 	}
	// 	// if (frm.doc.workflow_state === 'Pagado'){
	// 	// 	frm.toggle_enable(campos, frm.doc.workflow_state === 'Pagado'); 
	// 	// }
	// },
	refresh(frm) {
		/*frm.toggle_enable(campos, frm.doc.workflow_state === 'Revision');
		if (frm.doc.workflow_state === 'Revision'){
			// frm.set_df_property('comandante_en_turno', 'reqd', 1)
		}
		if (frm.doc.workflow_state === 'Espera Pago'){
			frm.set_df_property('comandante_en_turno', 'read_only', 1)
		}*/

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
			args: {papa: frm.doc.name, dano:frm.doc.solo_danos},
			freeze: false,
			freeze_message: "Espera porfavor",
			callback: function(r){
				if(frm.doc.solo_danos != 1){
					frm.set_value("lesionados",r.message[0] + "");
					frm.set_value("hospitalizados",r.message[1] + "");
					frm.set_value("fallecidos",r.message[2] + "");
				}else{
					frm.set_value("lesionados","0");
					frm.set_value("hospitalizados","0");
					frm.set_value("fallecidos","0");
				}
				frm.set_value("total_de_vehiculos_participantes",r.message[3] + "");
			}
		});
	},
	before_save(frm){
		frappe.call({
			method: "dev.dev_app.doctype.accidente.accidente.get_Contadores",
			args: {papa: frm.doc.name, dano:frm.doc.solo_danos},
			freeze: false,
			freeze_message: "Espera porfavor",
			callback: function(r){
				if(frm.doc.solo_danos != 1){
					frm.set_value("lesionados",r.message[0] + "");
					frm.set_value("hospitalizados",r.message[1] + "");
					frm.set_value("fallecidos",r.message[2] + "");
				}else{
					frm.set_value("lesionados","0");
					frm.set_value("hospitalizados","0");
					frm.set_value("fallecidos","0");
				}
				frm.set_value("total_de_vehiculos_participantes",r.message[3] + "");
			}
		});
	},
	solo_danos(frm){
		if(frm.doc.solo_danos == 1){
			frm.set_value("lesionados","0");
			frm.set_value("hospitalizados","0");
			frm.set_value("fallecidos","0");
		}
	},
	cal(){

	}

});
