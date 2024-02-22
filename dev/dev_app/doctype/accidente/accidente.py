# Copyright (c) 2023, Alejandro Hernandez and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Accidente(Document):
	pass

@frappe.whitelist()
def get_Contadores(papa, dano):
	vehiculos = frappe.db.count('Vehiculos accidente', {'parent': papa})
	lesionados = frappe.db.count('Peaton o ciclista', {'lesionado': '1', 'parent': papa})
	hospitalizados = frappe.db.count('Peaton o ciclista', {'hospitalizacion': '1', 'parent': papa})
	fallecidos = frappe.db.count('Peaton o ciclista', {'fallecido': '1', 'parent': papa})
	if dano == 1:
		lesionados = hospitalizados = fallecidos = 0	
	return [lesionados,hospitalizados,fallecidos, vehiculos]
