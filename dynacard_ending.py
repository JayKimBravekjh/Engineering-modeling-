# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:34:30 2015
Rod_pump algorithm (dynacard) : from uphole data, we can predict down hole data and status. 

@author: Jay Kim 
"""
import math
import cmath
import numpy as np
from sympy import * 
import matplotlib.pyplot as plt



def dynacard(area, unit_weight_rod, young_modulus, length, pressure, moved_length, time, diameter, damping_value, specific_gravity_solution, effective_load_max, effective_load_min):
    
    '''
    Calculates the gas formation factor using Standing's correlation
    
    :param pressure_at_depth: pressure (psi)
    :param base_temperature: temperature (F)
    :param sg_gas: specific gravity of gas
    :return: (Gas formation Factor,
            Standing's Z gas law correction)
    '''
        
    
    velocity = diameter/2 * math.sqrt(3.14*young_modulus*9.18/unit_weight_rod)

    damping_coefficient = 3.14*velocity*damping_value/(2*length)     
    
    k = unit_weight_rod/0.0024   
#    k = unit_weight_rod/damping_coefficient 
    
    L = 200               # L = maximum moved length 
    
    
    fig = plt.figure()
    

    
    for moved_length in range(1, L):  # at surface. 
         f = area/moved_length*math.e**(complex(0, 1)*(unit_weight_rod*time+k*moved_length)) - moved_length*(unit_weight_rod*(length - moved_length/2.0)-area*pressure)/(young_modulus*area)    
         f_d = area/moved_length*math.e**(complex(0, 1)*(unit_weight_rod*time-k*moved_length)) - moved_length*(unit_weight_rod*(length - moved_length/2.0)-area*pressure)/(young_modulus*area)
    
    #     X = f.diff(moved_length)
  #       X = diff(f, moved_length, 1)
  #       Y = diff(f_d, moved_length, 1)
         
     #    Y = f_d.diff(moved_length)
   #      moved_length_s = math.floor(f)
  #       y = f.diff(moved_length_s)
  #       moved_length_t = math.floor(f_d)
  #       y_d = f.diff(moved_length_t) 
         
         
  #       moved_length_s = min(range(-100000, 100000), key=lambda x: abs(x -f))
  #       y = f.diff(moved_length_s)
         
         gradient = 62.4/144*specific_gravity_solution 
         buyance = moved_length*area*gradient
                   
         force = effective_load_max - pressure  #- buyance 
         force_1 = effective_load_min - pressure # - buyance
         
  #       t == 1         


  #       ax1 = fig.add_subplot(122)
         ax1 = fig.add_subplot(122)
         
 #        ax = fig.add_subplot(111, axisbg='#FFFFCC') 
         ax1.plot(f, force, 'o') 
  #       ax2 = fig.add_subplot(122)
         ax2 = fig.add_subplot(122)             
         ax2.plot(f_d, force_1, 'x')    
  #       print f, f_d, force, force_1
         
#    F = min(range(-10000, 10000), key=lambda x:abs(x - f))
#    F_D  = min (range(-10000, 10000), key=lambda x:abs(x - f_d) )   

    """        
    for t in range(-60, 100):

         gradient = 62.4/144*specific_gravity_solution 
         buyance = t*area*gradient
        
         force = effective_load_max - pressure  - buyance
         force_1 = effective_load_min - pressure  - buyance
              
         ax3 = fig.add_subplot(122)
         ax3.plot(t, force, 'o')
         ax4 = fig.add_subplot(122)
         ax4.plot(t, force_1, 'x') """
        

      
    plt.show ()
    return f, f_d
  #       print f, f_d, force, forc
    
def dynacard_2(area, unit_weight_rod, young_modulus, length, pressure, moved_length, time, diameter, damping_value, specific_gravity_solution, effective_load_max, effective_load_min):
    
    '''
    Calculates the gas formation factor using Standing's correlation
    
    :param pressure_at_depth: pressure (psi)
    :param base_temperature: temperature (F)
    :param sg_gas: specific gravity of gas
    :return: (Gas formation Factor,
            Standing's Z gas law correction)
    '''
        
    
    velocity = diameter/2 * math.sqrt(3.14*young_modulus*9.18/unit_weight_rod)

    damping_coefficient = 3.14*velocity*damping_value/(2*length)     
    
    k = unit_weight_rod/0.0024   
#    k = unit_weight_rod/damping_coefficient 
    
    L = 200               # L = maximum moved length 
    
    
    fig = plt.figure()
    

    
    for moved_length in range(1, L):  # at surface. 
         f = area/moved_length*math.e**(complex(0, 1)*(unit_weight_rod*time+k*moved_length)) - moved_length*(unit_weight_rod*(length - moved_length/2.0)-area*pressure)/(young_modulus*area)    
         f_d = area/moved_length*math.e**(complex(0, 1)*(unit_weight_rod*time-k*moved_length)) - moved_length*(unit_weight_rod*(length - moved_length/2.0)-area*pressure)/(young_modulus*area)
    
    #     X = f.diff(moved_length)
  #       X = diff(f, moved_length, 1)
  #       Y = diff(f_d, moved_length, 1)
         
     #    Y = f_d.diff(moved_length)
   #      moved_length_s = math.floor(f)
  #       y = f.diff(moved_length_s)
  #       moved_length_t = math.floor(f_d)
  #       y_d = f.diff(moved_length_t) 
         
         
  #       moved_length_s = min(range(-100000, 100000), key=lambda x: abs(x -f))
  #       y = f.diff(moved_length_s)
         
    #     F = area/moved_length*mat  
         
         
  #       t == 1         


  #       ax1 = fig.add_subplot(122)
         ax1 = fig.add_subplot(122)
         
 #        ax = fig.add_subplot(111, axisbg='#FFFFCC') 
         ax1.plot(f, force, 'o') 
  #       ax2 = fig.add_subplot(122)
         ax2 = fig.add_subplot(122)             
         ax2.plot(f_d, force_1, 'x')    
  #       print f, f_d, force, force_1
         
#    F = min(range(-10000, 10000), key=lambda x:abs(x - f))
#    F_D  = min (range(-10000, 10000), key=lambda x:abs(x - f_d) )   

    """        
    for t in range(-60, 100):

         gradient = 62.4/144*specific_gravity_solution 
         buyance = t*area*gradient
        
         force = effective_load_max - pressure  - buyance
         force_1 = effective_load_min - pressure  - buyance
              
         ax3 = fig.add_subplot(122)
         ax3.plot(t, force, 'o')
         ax4 = fig.add_subplot(122)
         ax4.plot(t, force_1, 'x') """
        

      
    plt.show ()
    return f, f_d
  #       print f, f_d, force, forc

def dynacard_vertical(area, unit_weight_rod, young_modulus, length, pressure, moved_length, time, diameter, damping_value, specific_gravity_solution, effective_load_max, effective_load_min):
    
    
    (f, f_d, force, force_1) = dynacard(area, unit_weight_rod, young_modulus, length, pressure, moved_length, time, diameter, damping_value, specific_gravity_solution, effective_load_max, effective_load_min)

    F = min(range(-40, 100), key=lambda x:abs(x - f))
    F_D  = min (range(-40, 30), key=lambda x:abs(x - f_d) )   

  #       t == 1         
    for t in range( F, F_D):

        gradient = 62.4/144*specific_gravity_solution 
        buyance = t*area*gradient
        
        force = effective_load_max - pressure  - buyance
        force_1 = effective_load_min - pressure  - buyance
              
        ax3 = fig.add_subplot(122)
        ax3.plot(t, force, 'o')
        ax4 = fig.add_subplot(122)
        ax4.plot(t, force_1, 'x')
        
    plt.show()    
    
         
