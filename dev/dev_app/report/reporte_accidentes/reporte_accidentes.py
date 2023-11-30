# Copyright (c) 2023, Alejandro Hernandez and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint


def execute(filters=None):
	if not filters: filters = {}

	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_("No se encontro ni un dato"))
		return columns, cs_data

	for d in cs_data:
		row = frappe._dict({
				"fecha_y_hora": d.fecha_y_hora,
				"localidad": d.localidad,
			})
		data.append(row)
	return columns, data 

def get_columns():
	return [
		{
			"fieldname": "fecha_y_hora",
			"label": _("FECHA Y HORA"),
			"fieldtype": "Datetime",
			"width": "200",
		},
		{
			"fieldname": "localidad",
			"label": _("LOCALIDAD"),
			"fieldtype": "Select",
			"width": "120",
		}
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype="ACCIDENTE",
		fields=["fecha_y_hora","localidad"],
		filters=conditions,
		order_by="fecha_y_hora desc"
	)
	# data =  frappe.db.get_all('ACCIDENTE', ["fecha_y_hora","localidad"], filters = conditions)
	return data

def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
	return conditions