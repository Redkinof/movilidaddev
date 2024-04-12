# Copyright (c) 2024, Alejandro Hernandez and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname":"name",
			"label":"ID",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"creation",
			"label":"Fecha de Creacion",
			"fieldtype":"Date",
			"width":180
		},
		{
			"fieldname":"num_equipo",
			"label":"Numero de Inventario Equipo",
			"fieldtype":"Data",
			"width":220
		},
		{
			"fieldname":"num_serie",
			"label":"Numero de Serie",
			"fieldtype":"Data",
			"width":150
		},
		{
			"fieldname":"usuario",
			"label":"Usuario",
			"fieldtype":"Data",
			"width":150,
		},
		{
			"fieldname":"puesto",
			"label":"Puesto",
			"fieldtype":"Data",
			"width":150,
		},
		{
			"fieldname":"ubicacion",
			"label":"Ubicacion",
			"fieldtype":"Data",
			"width":150,
		},
		{
			"fieldname":"marca",
			"label":"Marca del equipo",
			"fieldtype":"Data",
			"width":150,
		},
		{
			"fieldname":"modelo",
			"label":"Modelo del equipo",
			"fieldtype":"Data",
			"width":150,
		},
		{
			"fieldname":"tipo",
			"label":"Tipo del equipo",
			"fieldtype":"Data",
			"width":150,
		},
		{
			"fieldname":"proce_marca",
			"label":"Marca de Procesador",
			"fieldtype":"Select",
			"width":180,
		},
		{
			"fieldname":"modelo",
			"label":"Modelo de Procesador",
			"fieldtype":"Data",
			"width":180,
		},
		{
			"fieldname":"velocidad",
			"label":"Velocidad de Procesador",
			"fieldtype":"Data",
			"width":200,
		},
	]
	
	#data = [{"datos":"Prueba"},{"datos":"Info"},{"datos":"probando"}]

	data= frappe.get_all(
		"Inventario", 
		fields=[
			"name",
			"creation",
			"num_equipo",
			"num_serie",
			"inv_usuario.usuario",
			"inv_puesto.puesto",
			"inv_ubicacion.ubicacion",
			"pc_marca.marca",
			"pc_modelo.modelo",
			"tipo.tipo",
			"proce_marca",
			"proce_modelo.modelo",
			"proce_velocidad.velocidad"
			],
			filters=[['creation', 'between',[filters.from_date,filters.to_date]]]
		)

	# inv= frappe.get_all('Inventario', filters=[['creation', 'between',['2024-04-02','2024-04-04']]] )
 
	array1=frappe.get_all("Memorias RAM",fields=["ram_marca","ram_modelo"])

	array2=frappe.get_all("Memorias RAM",fields=["ram_tipo","ram_velocidad"])

	array1.extend(array2)

	array1.append(array2)


	return columns, data
