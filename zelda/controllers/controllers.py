# -*- coding: utf-8 -*-
# from odoo import http


# class Zelda(http.Controller):
#     @http.route('/zelda/zelda', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zelda/zelda/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zelda.listing', {
#             'root': '/zelda/zelda',
#             'objects': http.request.env['zelda.zelda'].search([]),
#         })

#     @http.route('/zelda/zelda/objects/<model("zelda.zelda"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zelda.object', {
#             'object': obj
#         })

