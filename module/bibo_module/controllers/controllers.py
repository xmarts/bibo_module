# -*- coding: utf-8 -*-
from odoo import http

# class BiboModule(http.Controller):
#     @http.route('/bibo_module/bibo_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bibo_module/bibo_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bibo_module.listing', {
#             'root': '/bibo_module/bibo_module',
#             'objects': http.request.env['bibo_module.bibo_module'].search([]),
#         })

#     @http.route('/bibo_module/bibo_module/objects/<model("bibo_module.bibo_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bibo_module.object', {
#             'object': obj
#         })