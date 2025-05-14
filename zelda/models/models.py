# -*- coding: utf-8 -*-

from odoo import models, fields, api

class jugador(models.Model):
    _inherit = 'res.partner'
    _description = 'jugador'

    name = fields.Char(string="Name")
    rupies = fields.Integer()
    health = fields.Integer()
    progress = fields.Integer()
    objects = fields.One2many('zelda.objetos', "player_id")
    is_player = fields.Boolean()

    #def _get_objects(self):
        #for a in self:
            #a.objects = a.arrows.objects

class personajes(models.Model):
    _name = 'zelda.personajes'
    _description = 'Personajes'

    name = fields.Char(string="Name")
    town = fields.Many2many('zelda.pueblos')

class enemigos(models.Model):
    _name = 'zelda.enemigos'
    _description = 'Enemigos'

    name = fields.Char(string="Name")
    strength = fields.Integer()

class inventario(models.Model):
    _name = 'zelda.inventario'
    _description = 'algo'

class objetos(models.Model):
    _name = 'zelda.objetos'
    _description = 'Objetos'

    name = fields.Char(string="Name")
    player_id = fields.Many2one('res.partner')

class flechas(models.Model):
    _name = 'zelda.flechas'
    _description = 'Flechas'


class pueblos(models.Model):
    _name = 'zelda.pueblos'
    _description = 'Pueblos'

    name = fields.Char(string="Name")
    characters = fields.Many2many('zelda.personajes')

class mazmorras(models.Model):
    _name = 'zelda.mazmorras'
    _description = 'Mazmorras'

    name = fields.Char(string="Name")