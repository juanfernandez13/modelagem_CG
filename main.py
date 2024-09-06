import matplotlib.pyplot as plt
from world import define_world
from polygons.cubo import create_cube, plot_cube
from polygons.cone import create_cone, plot_cone
from polygons.trunk_cone import create_cone_trunk, plot_cone_trunk
from polygons.cylinder import create_cylinder, plot_cylinder
from polygons.mug import create_mug, plot_mug
from polygons.cano import create_cano, plot_cano


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

define_world(ax)

c1 = create_cube(position=[-5, -5, -5], scale=[2,2,2])
#plot_cube(ax, c1)



cot1 = create_mug()
plot_mug(ax, cot1)

plt.show()

