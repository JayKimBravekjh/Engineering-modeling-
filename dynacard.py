
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

E = 30000000 
A = 2
L = 150 
w = 1




        
x = np.arange(3, 43)



s = (x/30000000*2*(1*(150-x/2)-2*100))
y = 4*x + 3
u = y - s 
u_t = 2/60000000*x + 4.000000833333333


#plt.plot(y, u_t, 'o--')
plt.plot(u, u_t, 'k', lw=2)   
#for x in range(43):   
y_p = 10*x + 3
u_p = y_p - s
u_tp = 2/120000000*x + 10.000000833333333


plt.plot(u_p, u_tp, 'o--', lw=2)

plt.show()
#plt.plot(u_p, u_tp)

#for r in range(4:10):
#    e = 33.0000025 

#for r_t in range(4:10):
#    e_t = 
#plt.show()
    
