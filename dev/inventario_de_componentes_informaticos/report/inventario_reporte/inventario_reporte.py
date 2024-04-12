# Copyright (c) 2024, Alejandro Hernandez and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname":"name",
			"label":"ID",
			"fieldtype":"Data",
			"width":220
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
		{
			"fieldname":"ram_marca",
			"label":"Marca de RAM",
			"fieldtype":"Data",
			"width":200,
		},
	]
	
	#data = [{"datos":"Prueba"},{"datos":"Info"},{"datos":"probando"}]

	data1= frappe.get_all(
		"Inventario", 
		fields=[
			"name",
			"creation",
			"num_equipo",
			"num_serie",
			"inv_usuario.usuario",
			"inv_ubicacion.ubicacion",
			"pc_marca.marca",
			"pc_modelo.modelo",
			"tipo.tipo",
			"proce_marca",
			"proce_modelo.modelo",
			"proce_velocidad.velocidad",
			"table_ram.ram_marca.marca",
			],
		)
	
	data3=frappe.get_all("Memorias RAM",fields=["name","ram_marca.marca","ram_modelo.capacidad","ram_tipo","ram_velocidad.velocidad"])
	# filters=[['creation', 'between',[filters.from_date,filters.to_date]]]
 
	# var1 = frappe.db.get_value('Memorias RAM', '03eaf6b52a', ['ram_marca.marca',"ram_modelo.capacidad"])
	# var2 = frappe.db.get_value('Memorias RAM', '09776a0943', ['ram_marca.marca',"ram_modelo.capacidad"])
	
	data2=frappe.get_all("Memorias RAM",fields=["ram_marca","ram_modelo"])

	data={**data1,**data2}

	# inv= frappe.get_all('Inventario', filters=[['creation', 'between',['2024-04-02','2024-04-04']]] )
 
	# array1=frappe.get_all("Memorias RAM",fields=["ram_marca.marca","ram_modelo.capacidad"])

	# array2=frappe.get_all("Memorias RAM",fields=["ram_tipo","ram_velocidad.velocidad"])

	# array1={**array1, **array2} array={}

	# array1.extend(array2)
 
	# array1.append
 
	# array1[0 : 2] = [''.join(array1[0 : 2])]     array1[0:2] = [''.join(array1[0:2])]
 
	# array1[0] += ''.join(array1[1:2])
 
 	# array1.insert(array2)
  



	return columns, data

