// Copyright (c) 2024, Alejandro Hernandez and contributors
// For license information, please see license.txt

frappe.ui.form.on("ANTIGUEDAD DE CHOFERES", {
   refresh(frm) {
        var nowDate = new Date(); 
        var date = nowDate.getFullYear()+'/'+(nowDate.getMonth()+1)+'/'+nowDate.getDate();
        frm.set_value("fecha_de_registro",date);
        frm.set_df_property('fecha_de_registro', 'read_only', 1)
   },
   fecha_inicio_de_registro(frm){
        var noD = new Date();
        var newyear = noD.getFullYear() - frm.fecha_inicio_de_registro.getFullYear();
        frm.set_value("ano_antiguedad",newyear);
        frm.set_df_property('ano_antiguedad', 'read_only', 1)
    }
});
