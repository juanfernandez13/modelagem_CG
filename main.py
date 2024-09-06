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

cubo1 = create_cube()
cubo1 = rotation_x(cubo1, np.pi/4)
cubo1 = rotation_y(cubo1, np.pi/4)
cubo1 = translation(cubo1, [-2, -2, -2])
plot_cube(ax, cubo1)


#Definindo cone e cano no mesmo octante

cone1 = create_cone()
cone1 = scale_polygon(cone1, [2, 2, 2])
cone1 = translation(cone1, [-8, -8, -8])

plot_cone(ax, cone1)

cano1 = create_cano([-9, -2, -9], [10, 10, 0], [-4, -2, -4], [10, 5, 0], radius=0.5)

cano1 = rotation_x(cano1, np.pi/6)
cano1 = translation(cano1, [0, -5, 0])

plot_cano(ax, cano1)

#Definindo tronco de cone e caneca no mesmo octante

caneca1 = create_mug()
caneca1 = scale_polygon(caneca1, [4, 4, 4])
caneca1 = rotation_z(caneca1, np.pi/3)
caneca1 = rotation_y(caneca1, -np.pi/3)
caneca1 = translation(caneca1, [5, 5, 5])

plot_mug(ax, caneca1)

tronco_cone = create_cone_trunk()
tronco_cone = rotation_y(tronco_cone, np.pi/4)
tronco_cone = rotation_x(tronco_cone, np.pi/4)
tronco_cone = scale_polygon(tronco_cone, [2, 2, 2])
tronco_cone = translation(tronco_cone, [2, 2, 2])

plot_cone_trunk(ax, tronco_cone)




#create_cano([-5,0,5], [10,10,0], [4,0,-4], [10,5,0], radius=0.3, num_pointsC=40)

plt.show()

