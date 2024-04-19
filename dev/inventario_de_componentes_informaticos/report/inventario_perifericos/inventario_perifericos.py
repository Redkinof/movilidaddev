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
			"fieldname":"tipo_perif\u00e9rico1",
			"label":"Tipo de Periferico",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"marca",
			"label":"Marca Monitor",
			"fieldtype":"Data",
			"width":220
		},
		
		{
			"fieldname":"modelo",
			"label":"Modelo Monitor",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"tamano",
			"label":"Tamaño Monitor",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"num_monitor",
			"label":"Numero de Inventario",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"num_serie",
			"label":"Numero de Serie",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"tipo",
			"label":"Tipo de monitor",
			"fieldtype":"Data",
			"width":220
		},
		
	]
	data = frappe.get_all("Perifericos",fields=[
		"name",
		"parent",
		"tipo_perif\u00e9rico1",
		"monitor_marca.marca",
		"monitor_modelo.modelo",
		"monitor_tamano.tamano",
		"num_monitor",
		"num_serie",
		"monitor_tipo.tipo",
		
		])
	return columns, data