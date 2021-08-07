from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    towers = Tower.objects.all()
    return render(request, 'landing.html', context={'towers':towers})

import math 
def tower(request,id):
    tower = Tower.objects.get(id=id)
    if tower.conductor_type != 'Aluminum Conductor Steel Reinforced (ACSR)':
        print('yes')
        resistivity = 0.0000000265
        tower.resistance = (resistivity * float(tower.conductor_length))/float(tower.conductor_crosssectional_area)
        skin_depth = math.sqrt(resistivity/(3.134*int(tower.frequency)*(0.00000125)))
        diameter = 2*(math.sqrt(float(tower.conductor_crosssectional_area)/3.124))
        tower.resistance = (resistivity * float(tower.conductor_length))/(3.124*(diameter)*(skin_depth))
        tower.skin_depth = skin_depth
        temp_resistance = tower.resistance*((235+float(tower.temperature_effect))/(235+29))
        if tower.cable_configuration == 'horizontal':
            tower.current_carrying_capacity = '430'
        if tower.cable_configuration == 'vertical':
            tower.current_carrying_capacity = '389'
        # print(diameter)
        tower.spacing_between_bundled_conductors = 'Not Applicable'
        tower.inductance_of_transmission_lines = (0.00000125/2*3.142)*(0.25 + math.log(float(tower.spacing_between_conductors)/(diameter/2)))
        tower.capacitance = (0.0000000000555)/math.log((float(tower.spacing_between_conductors))/(diameter/2))
        tower.capacitive_reactance = (6600000/float(tower.frequency))*(math.log(float(tower.spacing_between_conductors)/float(diameter/2)))
        tower.efficiency = int((float(tower.power_received_at_load_in_MVA)/float(tower.power_transmitted_in_MVA))*100)
        tower.voltage_regulation = int(((float(tower.sending_end_voltage_in_KV)- float(tower.receiving_end_voltage_in_KV))/float(tower.receiving_end_voltage_in_KV))*100)
        print(tower.voltage_regulation)
        disruptive_voltage = 0.0374*math.log((float(tower.spacing_between_conductors))/float(diameter/2))
        tower.corona_losses = (0.0000244/1.225)*(float(tower.frequency) +25)*math.sqrt((diameter/2)/(float(tower.spacing_between_conductors)*1000))*math.pow((((float(tower.sending_end_voltage_in_KV)/math.sqrt(3))*1000)-disruptive_voltage),1)
        tower.power_received_at_load_in_MVA = float(tower.power_transmitted_in_MVA) - float(tower.corona_losses)/1000
        print(tower.power_received_at_load_in_MVA)
        form = TubularTower()
    return render(request, 'detailpage.html', context={'product':tower,'temp_resistance':temp_resistance,'form': form})

def tubular(request,id):
    tower = Tower.objects.get(id=id)
    print(request.POST.get('conductor_type'))
    if request.POST.get('conductor_type') != 'Aluminum Conductor Steel Reinforced (ACSR)':
        print('yes')
        resistivity = 0.0000000265
        tower.resistance = (resistivity * float(request.POST.get('conductor_length')))/float(request.POST.get('conductor_crosssectional_area'))
        skin_depth = math.sqrt(resistivity/(3.134*int(request.POST.get('frequency'))*(0.00000125)))
        diameter = 2*(math.sqrt(float(request.POST.get('conductor_crosssectional_area'))/3.124))
        tower.resistance = (resistivity * float(request.POST.get('conductor_length')))/(3.124*(diameter)*(skin_depth))
        tower.skin_depth = skin_depth
        temp_resistance = tower.resistance*((235+float(request.POST.get('temperature_effect')))/(235+29))
        if request.POST.get('cable_configuration') == 'horizontal':
            tower.current_carrying_capacity = '430'
        if request.POST.get('cable_configuration') == 'vertical':
            tower.current_carrying_capacity = '389'
        # print(diameter)
        tower.spacing_between_bundled_conductors = 'Not Applicable'
        tower.inductance_of_transmission_lines = (0.00000125/2*3.142)*(0.25 + math.log(float(request.POST.get('spacing_between_conductors'))/(diameter/2)))
        tower.capacitance = (0.0000000000555)/math.log((float(request.POST.get('spacing_between_conductors')))/(diameter/2))
        tower.capacitive_reactance = (6600000/float(request.POST.get('frequency')))*(math.log(float(request.POST.get('spacing_between_conductors'))/float(diameter/2)))
        disruptive_voltage = 0.0374*math.log((float(request.POST.get('spacing_between_conductors')))/float(diameter/2))
        tower.corona_losses = (0.0000244/1.225)*(float(request.POST.get('frequency')) +25)*math.sqrt((diameter/2)/(float(request.POST.get('spacing_between_conductors'))*1000))*math.pow((((float(request.POST.get('sending_end_voltage_in_KV'))/math.sqrt(3))*1000)-disruptive_voltage),1)
        tower.power_received_at_load_in_MVA = float(request.POST.get('power_transmitted_in_MVA')) - float(tower.corona_losses)/1000
        tower.efficiency = int((float(tower.power_received_at_load_in_MVA)/float(request.POST.get('power_transmitted_in_MVA')))*100)
        tower.voltage_regulation = int(((float(request.POST.get('sending_end_voltage_in_KV'))- float(tower.receiving_end_voltage_in_KV))/float(tower.receiving_end_voltage_in_KV))*100)
        print(tower.voltage_regulation)
        print(tower.power_received_at_load_in_MVA)
        tower.temperature_effect = request.POST.get('temperature_effect')
        tower.tower_height = request.POST.get('tower_height')
        tower.frequency = request.POST.get('frequency')
        tower.conductor_crosssectional_area = request.POST.get('conductor_crosssectional_area')
        tower.spacing_between_conductors = request.POST.get('spacing_between_conductors')
        tower.line_type = request.POST.get('line_type')
        tower.insulator_type = request.POST.get('insulator_type')
        vr = tower.voltage_regulation
        form = TubularTower()
    return render(request, 'detailpage.html', context={'product':tower,'temp_resistance':temp_resistance,'form': form, 'voltage_regulation':vr})
