# matplot_linspace
import scipy as sc
import matplotlib.pylab as plt
t= sc.linspace(0,1,100)
plt.plot(t,t**2)
plt.show()