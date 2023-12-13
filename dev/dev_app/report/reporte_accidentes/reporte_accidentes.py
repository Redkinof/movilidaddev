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
				"municipio": d.municipio,
				"localidad": d.localidad,
			})
		data.append(row)

	chart = get_chart_data(data)
	report_sumary = get_report_summary(data)
	return columns, data, None, chart, report_sumary

def get_columns():
	return [
		{
			"fieldname": "fecha_y_hora",
			"label": _("FECHA Y HORA"),
			"fieldtype": "Datetime",
			"width": "200",
		},
		{
			"fieldname": "municipio",
			"label": _("MUNICIPIO"),
			"fieldtype": "Data",
			"width": "120",
		},
		{
			"fieldname": "localidad",
			"label": _("LOCALIDAD"),
			"fieldtype": "Data",
			"width": "120",
		}
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype="ACCIDENTE",
		fields=["fecha_y_hora","municipio","localidad",],
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

def get_chart_data(data):
	if not data:
		return None
	
	labels = [
		'ACAPONETA',
		'AHUACATLÁN',
		'AMATLÁN DE C.',
		'COMPOSTELA',
		'HUAJICORI',
		'IXTLÁN DEL RÍO',
		'JALA',
		'XALISCO',
		'DEL NAYAR',
		'ROSAMORADA'
	]

	municipio_data = {
		'municipio = 001' : 0,
		'municipio = 002' : 0,
		'municipio = 003' : 0,
		'municipio = 004' : 0,
		'municipio = 005' : 0,
		'municipio = 006' : 0,
		'municipio = 007' : 0,
		'municipio = 008' : 0,
		'municipio = 009' : 0,
		'municipio = 010' : 0,
	}
	datasets = []

	for entry in data:
		if entry.municipio == '001':
			municipio_data['municipio = 001'] += 1
		if entry.municipio == '002':
			municipio_data['municipio = 002'] += 1
		if entry.municipio == '003':
			municipio_data['municipio = 003'] += 1
		if entry.municipio == '004':
			municipio_data['municipio = 004'] += 1
		if entry.municipio == '005':
			municipio_data['municipio = 005'] += 1
		if entry.municipio == '006':
			municipio_data['municipio = 006'] += 1
		if entry.municipio == '007':
			municipio_data['municipio = 007'] += 1
		if entry.municipio == '008':
			municipio_data['municipio = 008'] += 1
		if entry.municipio == '009':
			municipio_data['municipio = 009'] += 1
		if entry.municipio == '010':
			municipio_data['municipio = 010'] += 1
		

	datasets.append({
		'name': 'Municipio status',
		'values': [
			municipio_data.get('municipio = 001'),
			municipio_data.get('municipio = 002'),
			municipio_data.get('municipio = 003'),
			municipio_data.get('municipio = 004'),
			municipio_data.get('municipio = 005'),
			municipio_data.get('municipio = 006'),
			municipio_data.get('municipio = 007'),
			municipio_data.get('municipio = 008'),
			municipio_data.get('municipio = 009'),
			municipio_data.get('municipio = 010'),
			]
	})

	chart = {
		'data': {
			'labels' : labels,
			'datasets' : datasets
		},
		'type': 'pie',
		'height': 300,
	}

	return chart

def get_report_summary(data):
	if not data:
		return None
	
	municipio_acaponeta = 0

	for entry in data:
		if entry.municipio == '001':
			municipio_acaponeta += 1
		
	return[
		{
			'value' : municipio_acaponeta,
			'indicator' : 'Green',
			'label' : 'Municipio Acaponeta',
			'datatype' : 'Int',
		}
	]