import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def define_world(ax):
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    # Adicionando linhas divisórias para os octantes
    ax.plot([1, -1], [0, 0], [0, 0], color='k', linewidth=2)
    ax.plot([0, 0], [1, -1], [0, 0], color='k', linewidth=2)
    ax.plot([0, 0], [0, 0], [1, -1], color='k', linewidth=2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
