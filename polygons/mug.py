import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from function.hermite import hermite

import numpy as np

def generate_circle(center, normal, radius=0.05, num_points=20):
    theta = np.linspace(0, 2 * np.pi, num_points)
    v = np.array([np.cos(theta), np.sin(theta)])  # Coordenadas 2D da circunferência

    # Encontrar dois vetores ortogonais ao vetor normal
    if np.allclose(normal, [0, 0, 1]):
        u1 = np.array([1.0, 0.0, 0.0])  # Garantir que u1 seja float
    else:
        u1 = np.cross([0, 0, 1], normal).astype(float)  # Converter para float

    u1 /= np.linalg.norm(u1)  # Normalizar

    u2 = np.cross(normal, u1).astype(float)  # Garantir que u2 também seja float
    u2 /= np.linalg.norm(u2)  # Normalizar

    # Gerar pontos do círculo com broadcast correto
    u1 = u1[:, np.newaxis]  # Transformar em coluna (3,1)
    u2 = u2[:, np.newaxis]  # Transformar em coluna (3,1)

    # Expandir os vetores circulares v para 3D (usar apenas x e y de v)
    circle_points = center[:, None] + radius * (u1 * v[0] + u2 * v[1])  # Soma vetorial

    return circle_points.T  # Transpor para obter (num_points, 3)

def create_mug(height=1, radius=1, num_points=20, handle_radius=0.1):
    # Definir os vértices da base e topo da caneca
    p0_bottom = np.array([0, 0, 0])
    p1_bottom = np.array([radius, 0, 0])

    arc_t1_bottom = [0, radius * 2, 0]
    arc_t2_bottom = [0, -radius * 2, 0]

    p0_top = np.array([0, 0, height])
    p1_top = np.array([radius, 0, height])

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

    # Conectar os pontos correspondentes das duas bases para formar as laterais do cilindro
    mug_cylinder = []
    for i in range(len(base_vertices_bottom) - 1):
        if i == num_points // 2 - 1:
            continue
        p1 = base_vertices_bottom[i]
        p2 = base_vertices_bottom[i + 1]
        p3 = base_vertices_top[i + 1]
        p4 = base_vertices_top[i]
        mug_cylinder.append([p1, p2, p3, p4])

    # Adicionar as duas bases
    mug_cylinder += [base_vertices_bottom]

    # Criar a alça da xícara usando a curva de Hermite, iniciando na borda
    p0_handler = np.array([radius, 0, height * 0.25])  # Começando na borda do cilindro
    p1_handler = np.array([radius, 0, height * 0.75])  # Terminando na borda no topo

    arc_t1_handler = [radius * 1.5, 0, 0]  # Controle da curva da alça
    arc_t2_handler = [-radius * 1.5, 0, 0]

    # Gerar pontos da curva de Hermite da alça
    p = hermite(p0_handler, arc_t1_handler, p1_handler, arc_t2_handler, round(num_points))

    # Gerar círculos ao longo da curva da alça
    handle_circles = []
    previous_circle = None
    for i in range(len(p)):
        if i < len(p) - 1:
            tangent = np.array(p[i + 1]) - np.array(p[i])
        else:
            tangent = np.array(p[i]) - np.array(p[i - 1])
        tangent /= np.linalg.norm(tangent)

        # Gerar o círculo usando o ponto atual e a tangente
        circle = generate_circle(np.array(p[i]), tangent, radius=handle_radius)

        # Conectar o círculo anterior ao atual, se houver
        if previous_circle is not None:
            for j in range(len(circle) - 1):
                mug_cylinder.append([(previous_circle[j]), previous_circle[j + 1], circle[j + 1], circle[j]])
        previous_circle = circle

    return mug_cylinder


def plot_mug(ax, faces):
    ax.add_collection3d(Poly3DCollection(faces, facecolors='r', linewidths=1, edgecolors='cyan', alpha=.5))
