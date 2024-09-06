import matplotlib.pyplot as plt
import numpy as np

from world import define_world
from polygons.cubo import create_cube, plot_cube
from polygons.cone import create_cone, plot_cone
from polygons.trunk_cone import create_cone_trunk, plot_cone_trunk
from polygons.cylinder import create_cylinder, plot_cylinder
from polygons.mug import create_mug, plot_mug
from transformations.translation import translation
from transformations.scale import scale_polygon
from transformations.rotation import rotation_x, rotation_y, rotation_z
from polygons.cano import create_cano, plot_cano


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

define_world(ax)
c1 = create_cube()
#c1 = rotation_x(c1, np.pi/4)
c1 = rotation_z(c1, np.pi/4)
plot_cano(ax, c1)

#create_cano([-5,0,5], [10,10,0], [4,0,-4], [10,5,0], radius=0.3, num_pointsC=40)

#cot1 = create_mug()
#plot_mug(ax, cot1)

plt.show()

