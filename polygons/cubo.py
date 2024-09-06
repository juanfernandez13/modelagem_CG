import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def create_cube(position=[0,0,0], scale=[1,1,1]):
    # Definindo os vértices do cubo
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    vertices *= scale
    vertices += position

    # Definindo as faces do cubo
    faces = [#[vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [4, 5, 6, 7]],
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [2, 3, 7, 6]]]
    return faces

def plot_cube(ax, faces):
    # Adicionando as faces ao gráfico
    ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

# Criando e plotando dois cubos em posições diferentes
#faces1 = create_cube(position=[0, 0, 0])
#faces2 = create_cube(position=[2, 2, 2])

#plot_cube(ax, faces1)
#plot_cube(ax, faces2)

