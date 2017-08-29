
import os
import pandas as pd
#import fancyimpute as fi #https://pypi.python.org/pypi/fancyimpute
#import geopy as gp #https://pypi.python.org/pypi/geopy

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

import switrs_util as su
import switrs_lookups as lookup

#SWITRS -- Collision Data
#http://iswitrs.chp.ca.gov/Reports/jsp/userLogin.jsp
#   Data Requested:
#     Bike, Pedestrian and Motorcycle Data
#     Dates Jan 2012 - Feb 2017
#Collision Table
collision = pd.read_csv('switrs/CollisionRecords.txt', low_memory = False,
                        na_values = ["NA","","-"])

#Select Relevant Data
columns = [
         #unique id for collision
         'CASE_ID',
         #potential outcomes
         'COUNT_MC_KILLED', 'COUNT_MC_INJURED', 'COLLISION_SEVERITY',
         #when
         'COLLISION_DATE', 'ACCIDENT_YEAR', 'COLLISION_TIME', 'DAY_OF_WEEK',
         #where
         'INTERSECTION', 'STATE_HWY_IND', 'PRIMARY_RD', 'SECONDARY_RD',
         #environment/conditions
         'WEATHER_1', 'WEATHER_2', 'ROAD_SURFACE', 'ROAD_COND_1', 'ROAD_COND_2', 'LIGHTING',
         #accident/collision details
         'PCF_VIOL_CATEGORY', 'HIT_AND_RUN', 'TYPE_OF_COLLISION', 'MVIW',
         'ALCOHOL_INVOLVED', 'TRUCK_ACCIDENT',
         #covariates (impact collision-level severity measure)
         'PEDESTRIAN_ACCIDENT', 'BICYCLE_ACCIDENT'
         ]
moto_dat = collision[collision['MOTORCYCLE_ACCIDENT'] == Y][columns]
