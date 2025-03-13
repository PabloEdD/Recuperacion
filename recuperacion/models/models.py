# -*- coding: utf-8 -*-

from odoo import models, fields, api


class recuperacion(models.Model):
    _name = 'recuperacion.recuperacion'
    _description = 'recuperacion.recuperacion'

    name = fields.Char()
