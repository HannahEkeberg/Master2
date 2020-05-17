import numpy as np 
from scipy import interpolate
import matplotlib.pyplot as plt 

x = np.array([1,2,3,4])
y=np.array([75,0,25,100])

x_new = np.linspace(0,4,300)
a_BSpline = interpolate.make_interp_spline(x, y)
y_new = a_BSpline(x_new)

plt.plot(x_new,y_new)
plt.show()