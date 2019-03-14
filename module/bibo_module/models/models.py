# -*- coding: utf-8 -*-
from odoo import models, fields, api, _, tools
from openerp.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime, date, time, timedelta

class TicketNomina( models.Model ):
	_name = 'ticket.nomina'
	_rec_name = 'bar_code'
	
	id_prod = fields.Many2one( 'mrp.production','Codigo' )
	#tic_emp_id = fields.Many2one( 'ticket.employee', 'Empleado')
	tic_emp = fields.Many2one( 'hr.employee' , 'Empleado')

	bar_code = fields.Char( string = 'Codigo de barras' )
	name_ope = fields.Char( string = 'Nombre de operación' )
	ref_prod = fields.Many2one('product.template' , string = 'Producto' , related='id_prod.product_id.product_tmpl_id')
	date_rea = fields.Date( string = 'Fecha de creación' )
	date_lec = fields.Date( string = 'Fecha de lectura' )
	can_prod = fields.Integer( string = 'Cantidad de producto' )
	cost_tot = fields.Float( string = 'Costo total' )
	hand_ope = fields.Char( string = 'Mano de obra' )

class Modules(models.Model):
	_name = 'tk.modules'
	
	name_mod = fields.Char( string = 'Nombre del modulo' )
	_rec_name = 'name_mod'

class AddTicketEmployee(models.TransientModel):
	_name = 'ticket.employee'

	name = fields.Char(string="Asignacion", readonly=True, required=True, copy=False, default='Nuevo')
	employee = fields.Many2one( 'hr.employee' , string = 'Empleado' )
	busc_bar = fields.Char( string = 'Codigo de barras' )
	#rel_tick = fields.One2many( 'ticket.nomina','tic_emp_id' )

	#Crea un numero consecutivo a cada asignacion de ticket camp "name" 
	"""@api.model
	def create(self, vals):
		if vals.get('name', 'New') == 'New':
			vals['name'] = self.env['ir.sequence'].next_by_code('ticket.employee') or 'New'
		result = super(AddTicketEmployee, self).create(vals)
		return result"""

	@api.multi
	def search_ticket(self):
		invoice = ''
		if self.busc_bar:
			if self.employee:
				res = self.env['ticket.nomina'].search([('bar_code', '=', self.busc_bar)], limit=1)
				if res:
					if res.tic_emp.id == False:
						res.tic_emp = self.employee.id
						res.date_lec = fields.Date.today()
					else:
						raise UserError('El ticket ya tiene asignado un empleado')
				else:
					raise UserError('Sin resultados')
			else:
				raise UserError('Selecciona un empleado para continuar')
		else:
			raise UserError('Ingresa algo de en la barra de busqueda')

class AddCampModules(models.Model):
	_inherit = 'mrp.production'

	mod_prod = fields.Many2one( 'tk.modules' , string = 'Modulo' )

	prod_id = fields.One2many('ticket.nomina', 'id_prod' , 'Codigo de produccion')

	@api.multi
	@api.depends('move_raw_ids')
	def imp_ticket(self, code):
		if self.move_raw_ids:
			camp_date = fields.Date.today()
			cost_tota = self.product_qty * self.product_id.standard_price
			inv_obj = self.env['ticket.nomina']
			self.ensure_one()
			invoice = ''
			i=0
			for xn in self.move_raw_ids:
				i+=1
				val = 0
				if i > 9:
					val = str(i)
				else:
					val = '0' + str(i)
				if xn.product_id.hand_work_prod:
					invoice = inv_obj.create({
							'id_prod'  : self.id,
							'bar_code' : self.name + val, 
							'name_ope' : self.name,
							'hand_ope' : xn.product_id.name,
							'ref_prod' : self.product_id.product_tmpl_id,
							'date_rea' : camp_date,
							'can_prod' : self.product_qty,
							'cost_tot' : cost_tota
						})
		else:
			raise UserError('Sin datos')
		if invoice != '':
			return invoice
		else:
			raise UserError('No hay elementos marcados como mano de obra')

class AddCampHandWork(models.Model):
	_inherit = 'product.template'

	hand_work = fields.Boolean( string = 'Mano de obra' )

class AddCampHandWorkProd(models.Model):
	_inherit = 'product.product'

	hand_work_prod = fields.Boolean( string = 'Mano de obra', related='product_tmpl_id.hand_work' )
