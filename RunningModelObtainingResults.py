# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:39:57 2020

@author: dodo
"""

###Krk model
# the model was run and tested in Calliope version 0.6.4.
import calliope

# read already saved results from .nc files
model = calliope.read_netcdf('results\Krk_BAU_26Nov.nc') # scenario 1
model = calliope.read_netcdf('results\Krk_Min25PercentEle_S2.nc') # scenario 2
model = calliope.read_netcdf(r'results\NormalMin65eleTrans_S3_26112020.nc') # scenario 3
model = calliope.read_netcdf('results\HourlyTimeResMin65eleTrans_withCO2_264112020.nc') # sensitivity scenario 1
model = calliope.read_netcdf('results\OneLocationMin65eleTrans_withCO2_26112020.nc') # sensitivity scenario 2

# Create models for scenarios 1 to 3, as well as Sensitivity analysis 1 and 2
model = calliope.Model('model.yaml', scenario = 'Max5PercentElectrified')
model = calliope.Model('model.yaml', scenario = 'Min25PercentElectrified')
model = calliope.Model('model.yaml', scenario = 'Min65Elemin5percentHydrogenTransport')
model = calliope.Model('model.yaml', scenario = 'HourlyTimeResMin65eleTrans')
model = calliope.Model('model.yaml', scenario = 'OneGeogrLocationMin65eleTrans')

# run the model
model.run()