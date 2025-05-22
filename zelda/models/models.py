# -*- coding: utf-8 -*-

from odoo import models, fields, api

import random

class jugador(models.Model):
    _inherit = 'res.partner'
    _description = 'jugador'

    name = fields.Char(string="Name")
    rupies = fields.Integer()
    health = fields.Integer()
    progress = fields.Integer()
    inventory = fields.One2many('zelda.inventario', "player_id")
    objects = fields.Many2many('zelda.objetos', compute="_get_objects")
    is_player = fields.Boolean()

    def _get_objects(self):
        for a in self:
            a.objects = a.inventory.objects

    def create_object(self):
        for j in self:
            item = self.env['zelda.objetos'].create({
                "name": "Bombas",
                "type": "1",
                "quantity": random.randint(1, 99)
            })

            self.env['zelda.inventario'].create({
                "name": f"Item de {j.name}",
                "player_id": j.id,
                "objects": item.id
            })

    @api.model
    def add_object(self):
        for j in self.search([('is_player', '=', True)]):
            for o in j.objects:
                if o.quantity is not None :
                    o.quantity = o.quantity + random.randint(1, 4)


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
    player_id = fields.Many2one('res.partner')
    objects = fields.Many2one('zelda.objetos')

class objetos(models.Model):
    _name = 'zelda.objetos'
    _description = 'Objetos'

    name = fields.Char(string="Name")
    player_id = fields.Many2one('res.partner')
    type = fields.Selection([('1','Bombas'),('2','Flechas')], )
    quantity = fields.Integer()

class objetos_wizard(models.TransientModel):
    _name = 'zelda.objetos_wizard'
    _description = 'Objetos wizard'

    name = fields.Char(string="Name")
    player_id = fields.Many2one('res.partner', string="Player", default= lambda o: o._context.get("active_id"))
    type = fields.Selection([('1','Bombas'),('2','Flechas')], )
    quantity = fields.Integer()
    state = fields.Selection([
        ('objeto', "Object Selection"),
        ('inventario', "Inventory Selection"),
    ], default='objeto')

    def create_object(self):
        print(self)
        for o in self:
            item = self.env['zelda.objetos'].create({
                "name": o.name,
                "type": o.type,
                "quantity": o.quantity
            })

            self.env['zelda.inventario'].create({
                "name": f"{item.name} de {o.player_id.name}",
                "player_id": o.player_id.id,
                "objects": item.id

            })

    def next(self):
        self.state = 'inventario'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def previous(self):
        self.state = 'objeto'
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

class flechas(models.Model):
    _name = 'zelda.flechas'
    _description = 'Flechas'

    name = fields.Char(string="Name")
    type = fields.Selection([('1', 'Normal'), ('2', 'Fire'), ('3', 'Ice'), ('4', 'Electricity'), ('5', 'Ligth')], )
    player_id = fields.Many2one('res.partner')

class pueblos(models.Model):
    _name = 'zelda.pueblos'
    _description = 'Pueblos'

    name = fields.Char(string="Name")
    characters = fields.Many2many('zelda.personajes')

class mazmorras(models.Model):
    _name = 'zelda.mazmorras'
    _description = 'Mazmorras'

    name = fields.Char(string="Name")