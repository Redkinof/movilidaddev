// Copyright (c) 2023, Alejandro Hernandez and contributors
// For license information, please see license.txt

frappe.query_reports["Reporte Accidentes"] = {
	"filters": [
		{
            "fieldname": "fecha_y_hora",
            "label": __("FECHA Y HORA"),
            "fieldtype": "Datetime",
			"default": "",
        },
        {
            "fieldname": "localidad",
            "label": __("LOCALIDAD"),
            "fieldtype": "Select",
			"options": "Tepic",
        }
	]
};
