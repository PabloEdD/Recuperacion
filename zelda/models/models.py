# -*- coding: utf-8 -*-

from odoo import models, fields, api

class jugador(models.Model):
    _name = 'zelda.jugador'
    _description = 'jugador'

    name = fields.Char(string="Name")
    rupies = fields.Integer()
    health = fields.Integer()
    progress = fields.Integer()
    inventory = fields.One2many('zelda.inventario', "player_id")
    objects = fields.Many2many('zelda.objetos', compute="_get_objects")

    def _get_objects(self):
        for a in self:
            a.objects = a.inventory.objects

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
    _description = 'Inventario'

    name = fields.Char(string="Name")
    player_id = fields.Many2one('zelda.jugador')
    objects = fields.Many2one('zelda.objetos')


class objetos(models.Model):
    _name = 'zelda.objetos'
    _description = 'Objetos'

    name = fields.Char(string="Name")
    type = fields.Selection([('1','Bombas'),('2','Flechas')], )
    quantity = fields.Integer()


class flechas(models.Model):
    _name = 'zelda.flechas'
    _description = 'Flechas'

    name = fields.Char(string="Name")
    type = fields.Selection([('1', 'Normal'), ('2', 'Fire'), ('3', 'Ice'), ('4', 'Electricity'), ('5', 'Ligth')], )
    quantity = fields.Integer

class pueblos(models.Model):
    _name = 'zelda.pueblos'
    _description = 'Pueblos'

    name = fields.Char(string="Name")
    characters = fields.Many2many('zelda.personajes')

class mazmorras(models.Model):
    _name = 'zelda.mazmorras'
    _description = 'Mazmorras'

    name = fields.Char(string="Name")