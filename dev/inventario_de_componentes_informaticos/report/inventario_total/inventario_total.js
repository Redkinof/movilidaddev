// Copyright (c) 2024, Alejandro Hernandez and contributors
// For license information, please see license.txt

frappe.query_reports["Inventario Total"] = {
	"filters": [
        {
			fieldname: "from_date",
			label: __("De la Fecha"),
			fieldtype: "Date",
			default: frappe.datetime.add_days(frappe.datetime.now_date(true), -30),
		},
		{
			fieldname: "to_date",
			label: __("A la Fecha"),
			fieldtype: "Date",
			default: frappe.datetime.now_date(true),
		},
		// {
        //     fieldname: "creation",
        //     label: __("FECHA Y HORA"),
        //     fieldtype: "Datetime",
        // },
		// {
        //     fieldname: 'pc_modelo',
        //     label: __('pc modelo'),
        //     fieldtype: 'Link',
        //     options: 'Inv_Modelo_Equipo'
        // },
        // {
        //     fieldname: 'num_equipo',
        //     label: __('Equipo'),
        //     fieldtype: 'Data',
        // },
	]
};
