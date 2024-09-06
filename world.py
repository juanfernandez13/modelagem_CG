import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def define_world(ax):
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    # Adicionando linhas divisórias para os octantes
    ax.plot([10, -10], [0, 0], [0, 0], color='k', linewidth=2)
    ax.plot([0, 0], [10, -10], [0, 0], color='k', linewidth=2)
    ax.plot([0, 0], [0, 0], [10, -10], color='k', linewidth=2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
