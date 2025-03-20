# -*- coding: utf-8 -*-

from odoo import models, fields, api

class jugador(models.Model):
    _name = 'zelda.jugador'
    _description = 'jugador'

    name = fields.Char(string="Name")
    rupies = fields.Integer()
    health = fields.Integer()
    objects = fields.One2many('zelda.objetos', "player_id")

class personajes(models.Model):
    _name = 'zelda.personajes'
    _description = 'Personajes'

    name = fields.Char(string="Name")

class enemigos(models.Model):
    _name = 'zelda.enemigos'
    _description = 'Enemigos'

    name = fields.Char(string="Name")
    strength = fields.Integer()

class objetos(models.Model):
    _name = 'zelda.objetos'
    _description = 'Objetos'

    name = fields.Char(string="Name")
    quantity = fields.Integer()
    #type = fields.Selection(bombas, flehcas)
    player_id = fields.Many2one('zelda.jugador', string="Name")

class pueblos(models.Model):
    _name = 'zelda.pueblos'
    _description = 'Pueblos'

    name = fields.Char(string="Name")

class mazmorras(models.Model):
    _name = 'zelda.mazmorras'
    _description = 'Mazmorras'

    name = fields.Char(string="Name")