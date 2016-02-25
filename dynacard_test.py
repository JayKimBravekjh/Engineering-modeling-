# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:27:02 2015

"""

import math
import numpy as np

def dynacard(area, unit_weight_rod,  base_temperature,
                    sg_gas=0.9):
    '''
    Calculates the gas formation factor using Standing's correlation
    
    :param pressure_at_depth: pressure (psi)
    :param base_temperature: temperature (F)
    :param sg_gas: specific gravity of gas
    :return: (Gas formation Factor,
            Standing's Z gas law correction)
    '''
    # calculate gas compression correction
 #   pdb.set_trace()
    critical_temperature = 169 + 314 * sg_gas                                                            
    critical_pressure = 708.75 - 57.5 * sg_gas                                                         
    reduced_temperature = (base_temperature + 460)/critical_temperature                                                             
    reduced_pressure = pressure_at_depth/critical_pressure                                                          
    a = 1.39 * math.sqrt(reduced_temperature - 0.92) - 0.36 * reduced_temperature - 0.101 
    b = (0.62 - 0.23 * reduced_temperature) * reduced_pressure 
    c = (0.066 / (reduced_temperature - 0.86) - 0.037) * reduced_pressure ** 2
    d = (0.32 / (10 ** (9 * (reduced_temperature - 1)))) * reduced_pressure ** 6 
    e = b + c + d 
    f = 0.132 - 0.32 * math.log(reduced_temperature,10)
    g = 10**(0.3106 - 0.49 * reduced_temperature + 0.1824 * reduced_temperature ** 2)
    z = a + ( 1 - a) * (2.71828 ** (-e)) + f * reduced_pressure ** g
    
    # gas law with correction
    gas_formation_fac = (z * 14.7 * base_temperature) / (pressure_at_depth * 68)
    return gas_formation_fac




    
