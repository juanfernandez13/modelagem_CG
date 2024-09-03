import matplotlib.pyplot as plt
from world import define_world
from poligonos.cubo import create_cube, plot_cube
from poligonos.cone import hermite_cone


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

define_world(ax)

c1 = create_cube(position=[-5, -5, -5], scale=[2,2,2])
plot_cube(ax, c1)

hermite_cone(ax)
plt.show()

