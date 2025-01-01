import matplotlib.pyplot as plt

import numpy as np

fig,ax = plt.subplots()

xmin = -10

xmax = 10

ymin = -10

ymax = 10
plt.axis([xmin,xmax,ymin,ymax])

plt.plot([xmin,xmax], [0,0],'k')

plt.plot([0,0],[ymin,ymax],'k')

points = 2*(xmax - xmin)

x = np.linspace(xmin,xmax,points)

ax.set_aspect('equal')

y = 2*x + 1

plt.plot(x,y,label = 'y = 2*x + 1')

plt.plot([4], [6], 'k' , label = 'point')

ax.set_xlabel("valores de x")

ax.set_ylabel("valores de y")

ax.set_title("plano cartesiano by edgar")

ax.grid(True)

ax.set_xticks(np.arange(xmin,xmax,1))

ax.set_yticks(np.arange(ymin,ymax,1))

for x in range(1):
	
	y = 0.5*x + 1
	
	plt.plot(x,y, 'ro')
	
plt.show()