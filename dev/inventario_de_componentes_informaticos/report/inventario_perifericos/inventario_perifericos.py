# Copyright (c) 2024, Alejandro Hernandez and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns= [
		{
			"fieldname":"name",
			"label":"ID",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"parent",
			"label":"Parent",
			"fieldtype":"Data",
			"width":150
		},
		# {
		# 	"fieldname":"creation",
		# 	"label":"Fecha de Creacion",
		# 	"fieldtype":"Date",
		# 	"width":180
		# },
		{
			"fieldname":"periferico_pc",
			"label":"Tipo de Periferico",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"per_marca",
			"label":"Marca del Periferico",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"per_modelo",
			"label":"Modelo del Periferico",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"per_num_inv",
			"label":"Numero de Inventario",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"per_num_serie",
			"label":"Numero de Serie",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"per_tamano_pantalla",
			"label":"Tamaño de la pantalla (Pulgadas)",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"tipo_peri",
			"label":"Tipo de Periferico",
			"fieldtype":"Data",
			"width":150
		},
		
	]
	data = frappe.get_all("Perifericos Pc",fields=[
		"name",
		"parent",
		# "creation",
		"periferico_pc.periferico_pc",
		"per_marca.per_marca",
		"per_modelo.per_modelo",
		"per_num_inv",
		"per_num_serie",
		"per_tamano_pantalla.per_tamano_pantalla",
		"tipo_peri.tipo_peri",
		
		],
		filters=[['creation', 'between',[filters.from_date,filters.to_date]]]
		)
	return columns, data