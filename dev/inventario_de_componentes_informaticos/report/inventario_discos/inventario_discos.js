// Copyright (c) 2024, Alejandro Hernandez and contributors
// For license information, please see license.txt

frappe.query_reports["Inventario Discos"] = {
	"filters": [
		{
			fieldname: "from_date",
			label: __("De la Fecha"),
			fieldtype: "Date",
			// default: frappe.datetime.add_days(frappe.datetime.now_date(true), -40), 
            default: frappe.datetime.get_year_start,
		},
		{
			fieldname: "to_date",
			label: __("A la Fecha"),
			fieldtype: "Date",
			default: frappe.datetime.now_date(true),
		},
	]
};
