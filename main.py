import numpy as np
import matplotlib.pyplot as plt

from polygons import create_cube, create_cano, create_mug, create_cone, create_cone_trunk
from transformations import translation, scale_polygon, rotation_x, rotation_y, rotation_z
from helpers import plot_2d, plot_3d, define_world3d, define_world2d, plotCam, plot_polygons


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#define os limites nos eixos x, y e z
define_world3d(ax)

cubo1, cubo1_faceColor, cubo1_edgeColor = create_cube()
#cubo1 = rotation_x(cubo1, np.pi/4)
#cubo1 = rotation_y(cubo1, np.pi/4)
cubo1 = translation(cubo1, [1, 1, 0])
plot_3d(ax, cubo1, cubo1_faceColor, cubo1_edgeColor, 0.8)


#Definindo cone e cano no mesmo octante

cone1, cone1_faceColor, cone1_edgeColor = create_cone()
cone1 = scale_polygon(cone1, [2, 2, 2])
cone1 = translation(cone1, [-8, -8, -8])

plot_3d(ax, cone1, cone1_faceColor, cone1_edgeColor)

cano1, cano1_faceColor, cano1_edgeColor = create_cano([-9, -2, -9], [10, 10, 0], [-4, -2, -4], [10, 5, 0], radius=0.5)
cano1 = translation(cano1, [3.5, -2, 2])
plot_3d(ax, cano1, cano1_faceColor, cano1_edgeColor)

#Definindo tronco de cone e caneca no mesmo octante

caneca1, caneca1_face_color, caneca1_edgeColor = create_mug()
caneca1 = scale_polygon(caneca1, [3, 3, 3])
caneca1 = translation(caneca1, [5, 5, 5])
plot_3d(ax, caneca1, caneca1_face_color, caneca1_edgeColor)


tronco_cone, tronco_cone_face_color, tronco_cone_edge_color = create_cone_trunk()
tronco_cone = scale_polygon(tronco_cone, [2, 2, 2])
tronco_cone = translation(tronco_cone, [2, 2, 2])
plot_3d(ax, tronco_cone, tronco_cone_face_color, tronco_cone_edge_color)

plt.show()

#Vizualização nos eixos X e Y

fig2, ax2 = plt.subplots()
define_world2d(ax2, title="Vizualização nos eixos X e Y", xlabel="Eixo x", ylabel="Eixo y")

plot_2d(ax2, cano1, face_color=cano1_faceColor, edge_color=cano1_edgeColor, axis='xy')
plot_2d(ax2, caneca1, face_color=caneca1_face_color, edge_color=caneca1_edgeColor, axis='xy')
plot_2d(ax2, cone1, face_color=cone1_faceColor, edge_color=cone1_edgeColor, axis='xy')
plot_2d(ax2, tronco_cone, face_color=tronco_cone_face_color, edge_color=tronco_cone_edge_color, axis='xy')
plot_2d(ax2, cubo1, face_color=cubo1_faceColor, edge_color=cubo1_edgeColor, axis='xy')

plt.show()

#Vizualização nos eixos X e Z

fig3, ax3 = plt.subplots()
define_world2d(ax3, title="Vizualização nos eixos X e Z", xlabel="Eixo x", ylabel="Eixo Z")

plot_2d(ax3, cano1, face_color=cano1_faceColor, edge_color=cano1_edgeColor, axis='xz')
plot_2d(ax3, caneca1, face_color=caneca1_face_color, edge_color=caneca1_edgeColor, axis='xz')
plot_2d(ax3, cone1, face_color=cone1_faceColor, edge_color=cone1_edgeColor, axis='xz')
plot_2d(ax3, tronco_cone, face_color=tronco_cone_face_color, edge_color=tronco_cone_edge_color, axis='xz')
plot_2d(ax3, cubo1, face_color=cubo1_faceColor, edge_color=cubo1_edgeColor, axis='xz')

plt.show()

#Vizualização nos eixos Y e Z

fig4, ax4 = plt.subplots()
define_world2d(ax4, title="Vizualização nos eixos Y e Z", xlabel="Eixo Y", ylabel="Eixo Z")

plot_2d(ax4, cano1, face_color=cano1_faceColor, edge_color=cano1_edgeColor, axis='yz')
plot_2d(ax4, caneca1, face_color=caneca1_face_color, edge_color=caneca1_edgeColor, axis='yz')
plot_2d(ax4, cone1, face_color=cone1_faceColor, edge_color=cone1_edgeColor, axis='yz')
plot_2d(ax4, tronco_cone, face_color=tronco_cone_face_color, edge_color=tronco_cone_edge_color, axis='yz')
plot_2d(ax4, cubo1, face_color=cubo1_faceColor, edge_color=cubo1_edgeColor, axis='yz')

plt.show()

#plot 3d na visão da camera
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot_polygons(ax, [cubo1, tronco_cone, caneca1], [cubo1_faceColor, tronco_cone_face_color, caneca1_face_color],
        [cubo1_edgeColor, tronco_cone_edge_color, caneca1_edgeColor],[5, -10, 5], 60)

plt.show()

#plot 2d na visão da camera
figCam1, axCam1 = plt.subplots()

plotCam(axCam1, [cubo1, tronco_cone, caneca1],
        [ cubo1_faceColor, tronco_cone_face_color, caneca1_face_color],
        [ cubo1_edgeColor, tronco_cone_edge_color, caneca1_edgeColor],
        cam_position=[5, -10, 5], target_position=[-5, -10, -5])

plt.show()
