import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

points=1000000
x_max=10
x_min=0
circle_center=(5,5)
circle_radius=2

p=np.random.uniform(x_min, x_max, size=(2,points))
x_points, y_points= p

n=[]
for i in range (len(x_points)):
    if ((x_points[i] - circle_center[0])**2 +(y_points[i] - circle_center[1])**2< circle_radius**2):
        n.append(1)
num_inside= len(n)

print(f"The number of points inside the circle is '{num_inside}")
print(f"The total number of points is{points}")
pi=(num_inside/points)*(x_max/circle_radius)**2
print(f"The value of pi is approximately{pi}")

fig, ax=plt.subplots()
ax.plot(x_points,y_points,'o',ms=2,zorder=-1)
circle=patches.Circle(circle_center, circle_radius, linewidth=2, edgecolor='k' , facecolor='none')
ax.add_patch(circle)
plt.xlim(x_min,x_max)
plt.ylim(x_min,x_max)
plt.gca().set_aspect('equal',adjustable='box')
plt.show()