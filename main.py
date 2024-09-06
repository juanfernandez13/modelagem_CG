import matplotlib.pyplot as plt
import numpy as np

from world import define_world
from polygons import create_cube, create_cano, create_mug, create_cone, create_cone_trunk
from transformations import translation, scale_polygon, rotation_x, rotation_y, rotation_z
from helpers import plot_2d, plot_3d


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#define os limites nos eixos x, y e z
define_world(ax)

cubo1, cubo1_faceColor, cubo1_edgeColor = create_cube()
#cubo1 = rotation_x(cubo1, np.pi/4)
#cubo1 = rotation_y(cubo1, np.pi/4)
#cubo1 = translation(cubo1, [-2, -2, -2])
plot_3d(ax, cubo1, cubo1_faceColor, cubo1_edgeColor)


#Definindo cone e cano no mesmo octante

cone1, cone1_faceColor, cone1_edgeColor = create_cone()
cone1 = scale_polygon(cone1, [2, 2, 2])
cone1 = translation(cone1, [-8, -8, -8])

plot_3d(ax, cone1, cone1_faceColor, cone1_edgeColor)

cano1, cano1_faceColor, cano1_edgeColor = create_cano([-9, -2, -9], [10, 10, 0], [-4, -2, -4], [10, 5, 0], radius=0.5)

#cano1 = rotation_x(cano1, np.pi/6)
#cano1 = translation(cano1, [0, -5, 0])

plot_3d(ax, cano1, cano1_faceColor, cano1_edgeColor)

#Definindo tronco de cone e caneca no mesmo octante

caneca1, caneca1_face_color, caneca1_edgeColor = create_mug()
caneca1 = scale_polygon(caneca1, [4, 4, 4])
#caneca1 = rotation_z(caneca1, np.pi/3)
#caneca1 = rotation_y(caneca1, -np.pi/3)
caneca1 = translation(caneca1, [5, 5, 5])

plot_3d(ax, caneca1, caneca1_face_color, caneca1_edgeColor)

tronco_cone, tronco_cone_face_color, tronco_cone_edge_color = create_cone_trunk()
#tronco_cone = rotation_y(tronco_cone, np.pi/4)
#tronco_cone = rotation_x(tronco_cone, np.pi/4)
tronco_cone = scale_polygon(tronco_cone, [2, 2, 2])
tronco_cone = translation(tronco_cone, [2, 2, 2])

plot_3d(ax, tronco_cone, tronco_cone_face_color, tronco_cone_edge_color)




fig2, ax2 = plt.subplots()
#fig3, ax3 = plt.subplots()
#fig4, ax4 = plt.subplots()

plot_2d(ax2, cano1, face_color=cano1_faceColor, edge_color=cano1_edgeColor, axis='xy')
plot_2d(ax2, caneca1, face_color=caneca1_face_color, edge_color=caneca1_edgeColor, axis='xy')
plot_2d(ax2, cone1, face_color=cone1_faceColor, edge_color=cone1_edgeColor, axis='xy')
plot_2d(ax2, tronco_cone, face_color=tronco_cone_face_color, edge_color=tronco_cone_edge_color, axis='xy')
plot_2d(ax2, cubo1, face_color=cubo1_faceColor, edge_color=cubo1_edgeColor, axis='xy')



plt.show()


