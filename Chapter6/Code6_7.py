import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.optimize import curve_fit
def func(x, a, b,c):
    return a * (1-np.exp(- (x-c)/b))
def func2(x,a,b,c):
    return a*np.exp(-(x-c)/b)
my_data = genfromtxt('RCSeguenza.dat', delimiter=' ')
x = my_data[: , 0]
y = my_data[:, 1]
plt.xlabel('t (s)')
plt.ylabel('V (volt)')
plt.plot(x, y, color = 'black')#charge the first plot

x = my_data[(my_data[:,0]<0.74) , 0]
y = my_data[(my_data[:,0]<0.74), 1]
suggest =[5,0.03,0.421]
popt, pcov = curve_fit(func, x, y, p0=suggest)
plt.plot(x, func(x, *popt), 'r-',linestyle='--',color = 'b',label='fit: a=%5.3f, b=%7.5f, c=%5.3f' % tuple(popt))

x = my_data[(my_data[:,0]>2.04) , 0]
y = my_data[(my_data[:,0]>2.04), 1]
suggest =[5,0.1,2]
popt, pcov = curve_fit(func2, x, y, p0=suggest)
plt.plot(x, func2(x, *popt), 'r-',linestyle='--',color='r',label='fit: a=%5.3f, b=%7.5f, c=%5.3f' % tuple(popt))
plt.legend()
plt.show()
