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
			"fieldname":"modelo",
			"label":"Modelo",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"tamano",
			"label":"Tamaño",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"tipo",
			"label":"Tipo",
			"fieldtype":"Data",
			"width":220
		},
	]
	data = frappe.get_all("Discos de almacenamiento",fields=["name","parent","disco_marca.marca","disco_modelo.modelo","disco_tamano.tamano","tipo"])
	return columns, data