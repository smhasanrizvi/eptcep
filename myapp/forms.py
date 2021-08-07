from django import forms
from .models import *
from django.db import models

class TubularTower(forms.ModelForm):
    class Meta:
        model = Tower
        fields = ('tower_height', 'frequency','temperature_effect','spacing_between_conductors', 'conductor_type','line_type','conductor_length','conductor_crosssectional_area','cable_configuration','power_transmitted_in_MVA','sending_end_voltage_in_KV' )

