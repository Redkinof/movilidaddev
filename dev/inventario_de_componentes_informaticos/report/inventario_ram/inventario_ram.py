# Copyright (c) 2024, Alejandro Hernandez and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns= [
		{
			"fieldname":"name",
			"label":"ID",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"parent",
			"label":"Parent",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"marca",
			"label":"Marca",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"capacidad",
			"label":"Capacidad",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"ram_tipo",
			"label":"Tipo de Ram",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"velocidad",
			"label":"Velocidad",
			"fieldtype":"Data",
			"width":220
		},
	]
	data = frappe.get_all("Memorias RAM",fields=["name","parent","ram_marca.marca","ram_modelo.capacidad","ram_tipo","ram_velocidad.velocidad"],
		filters=[['creation', 'between',[filters.from_date,filters.to_date]]])
	return columns, data
