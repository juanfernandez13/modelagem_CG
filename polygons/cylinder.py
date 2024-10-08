import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from function.hermite import hermite


def create_cylinder(height=1, radius=1, num_points=20):
    p0_bottom = np.array([0, 0, 0])
    p1_bottom = np.array([radius, 0, 0])

    arc_t1_bottom = [0, radius * 2, 0]
    arc_t2_bottom = [0, -radius * 2, 0]

    space_around = (radius - radius) / 2

    p0_top = np.array([space_around, 0, height])
    p1_top = np.array([space_around + radius, 0, height])

    arc_t1_top = [0, radius * 2, 0]
    arc_t2_top = [0, -radius * 2, 0]

    # Gerar os vértices da base maior
    base_vertices_bottom = []
    base_vertices_bottom += hermite(p0_bottom, arc_t1_bottom, p1_bottom, arc_t2_bottom, round(num_points / 2))
    base_vertices_bottom += hermite(p0_bottom, arc_t2_bottom, p1_bottom, arc_t1_bottom, round(num_points / 2))

    # Gerar os vértices da base menor (topo)
    base_vertices_top = []
    base_vertices_top += hermite(p0_top, arc_t1_top, p1_top, arc_t2_top, round(num_points / 2))
    base_vertices_top += hermite(p0_top, arc_t2_top, p1_top, arc_t1_top, round(num_points / 2))

    # Conectar os pontos correspondentes das duas bases para formar as laterais do tronco
    cone_trunk = []
    for i in range(len(base_vertices_bottom)):
        if i == num_points / 2 - 1:
            continue
        p1 = base_vertices_bottom[i]
        p2 = base_vertices_bottom[(i + 1) % len(base_vertices_bottom)]
        p3 = base_vertices_top[(i + 1) % len(base_vertices_top)]
        p4 = base_vertices_top[i]
        cone_trunk.append([p1, p2, p3, p4])

    # Adicionar as duas bases
    cone_trunk += [base_vertices_bottom]
    cone_trunk += [base_vertices_top]

    return cone_trunk


def plot_cylinder(ax, faces):
    ax.add_collection3d(Poly3DCollection(faces, facecolors='r', linewidths=1, edgecolors='cyan', alpha=.5))
