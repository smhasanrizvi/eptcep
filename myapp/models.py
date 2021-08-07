# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tower(models.Model):
    name = models.CharField(max_length=300,default='')
    picture = models.CharField(max_length=10000,default='')
    short_description = models.CharField(max_length=2000,default='',blank=True)
    complete_description = models.CharField(max_length=2000,default='',blank=True)    
    tower_height = models.CharField(max_length=200,default='',blank=True) 
    frequency = models.CharField(max_length=200,default='',blank=True) 
    resistance = models.CharField(max_length=200,default='',blank=True)
    skin_depth = models.CharField(max_length=200,default='',blank=True)
    temperature_effect = models.CharField(max_length=200,default='',blank=True)
    spacing_between_bundled_conductors = models.CharField(max_length=200,default='',blank=True)
    spacing_between_conductors = models.CharField(max_length=200,default='',blank=True)
    current_carrying_capacity = models.CharField(max_length=200,default='',blank=True)
    inductance_of_transmission_lines = models.CharField(max_length=200,default='',blank=True)
    capacitance = models.CharField(max_length=200,default='',blank=True)
    capacitive_reactance = models.CharField(max_length=200,default='',blank=True)
    conductor_choices = (
        ('Partridge','Partridge'),
        ('Ostrich','Ostrich'),
        ('Merlin','Merlin'),
        ('Pelican','Pelican'),
        ('Drake','Drake'),
        ('Pheasant','Pheasant'),
    )
    conductor_type = models.CharField(max_length=200,choices = conductor_choices,default='',blank=True)
    conductor_length = models.CharField(max_length=200,default='',blank=True)
    conductor_crosssectional_area = models.CharField(max_length=200,default='',blank=True)
    
    span = models.CharField(max_length=200,default='',blank=True)
    commulative_line_loading = models.CharField(max_length=200,default='',blank=True)
    choices = (
        ('horizontal','horizontal'),
        ('vertical','vertical'),
    )
    cable_configuration = models.CharField(max_length=200,choices = choices,default='',blank=True)
    power_transmitted_in_MVA = models.CharField(max_length=200,default='',blank=True)
    power_received_at_load_in_MVA = models.CharField(max_length=200,default='',blank=True)
    efficiency = models.CharField(max_length=200,default='',blank=True)
    sending_end_voltage_in_KV = models.CharField(max_length=200,default='',blank=True)
    receiving_end_voltage_in_KV = models.CharField(max_length=200,default='',blank=True)
    voltage_regulation = models.CharField(max_length=200,default='',blank=True)
    corona_losses = models.CharField(max_length=200,default='',blank=True)
    line_choices = (
        ('SINGLE CIRCUIT UNBUNDLED','SINGLE CIRCUIT UNBUNDLED'),
        ('DOUBLE CIRCUIT UNBUNDLED','DOUBLE CIRCUIT UNBUNDLED'),
        ('DOUBLE CIRCUIT BUNDLED (3C)','DOUBLE CIRCUIT BUNDLED (3C)'),
        ('DOUBLE CIRCUIT BUNDLED (4C)','DOUBLE CIRCUIT BUNDLED (4C)'),
    )
    line_type = models.CharField(max_length=200,choices=line_choices,default='',blank=True)
    insulator_choices = (
        ('Pin type','Pin type'),
        ('Suspension type','Suspension type'),
        ('Strain type','Strain type'),
        
    )
    insulator_type = models.CharField(max_length=200,choices=insulator_choices,default='',blank=True)
    
    def __str__(self):
        return self.name
