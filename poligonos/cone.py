from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from function.hermite import hermite

def hermite_cone(ax,height=2, radius=1, num_points=20):
    P0 = (0, 0, 0)
    P1 = (radius, 0, 0)
    arc_t1 = (0, radius * 2, 0)
    arc_t2 = (0, -radius * 2, 0)

    base_vertices = []

    base_vertices += hermite(P0, arc_t1, P1, arc_t2, round(num_points/2))
    base_vertices += hermite(P0, arc_t2, P1, arc_t1, round(num_points/2))

    #define o meio da base do cone e depois a altura
    vertex = [radius/2, 0, height]

    # Conectar cada ponto da base ao vértice para formar as laterais do cone
    cone = []
    for i in range(len(base_vertices)):
        # Obter o ponto atual e o próximo ponto (para criar uma face lateral)
        p1 = base_vertices[i]
        p2 = base_vertices[(i + 1) % len(base_vertices)]  # O próximo ponto, ou o primeiro se for o último ponto
        print(p1, p2, vertex)
        # Criar um triângulo que conecta p1, p2 e o vértice
        cone.append([p1, p2, vertex])


    cone.append(base_vertices)
    ax.add_collection3d(Poly3DCollection(cone, facecolors='r', linewidths=1, edgecolors='cyan', alpha=.5))

