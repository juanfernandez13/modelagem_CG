import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from function.hermite import hermite

def generate_circle(center, tangent, radius):
    # Gerar um círculo no plano perpendicular à tangente
    theta = np.linspace(0, 2 * np.pi, 10)
    v = np.cross(tangent, [1, 0, 0])
    if np.linalg.norm(v) < 1e-6:
        v = np.cross(tangent, [0, 1, 0])
    v /= np.linalg.norm(v)
    u = np.cross(tangent, v)
    print(np.linalg.norm(u))
    u /= np.linalg.norm(u)
    circle = np.array([center + radius * (np.cos(t) * u + np.sin(t) * v) for t in theta])
    return circle

def create_cano():
    mug_cylinder = []
    height = 5
    # Criar a alça da xícara usando a curva de Hermite, iniciando na borda
    p0_handler = np.array([1, 0, height * -0.25])  # Começando na borda do cilindro
    p1_handler = np.array([1, 0, height * 0.75])  # Terminando na borda no topo

    arc_t1_handler = [1 * 1.5, 0, 0]  # Controle da curva da alça
    arc_t2_handler = [-1 * 1.5, 0, 0]

    # Gerar pontos da curva de Hermite da alça
    p = hermite(p0_handler, arc_t1_handler, p1_handler, arc_t2_handler, round(20))

    # Gerar círculos ao longo da curva da alça
    previous_circle = None
    for i in range(len(p)):
        if i < len(p) - 1:
            tangent = np.array(p[i + 1]) - np.array(p[i])
        else:
            tangent = np.array(p[i]) - np.array(p[i - 1])
        tangent /= np.linalg.norm(tangent)

        # Gerar o círculo usando o ponto atual e a tangente
        circle = generate_circle(np.array(p[i]), tangent, radius=0.5)

        # Conectar o círculo anterior ao atual, se houver
        if previous_circle is not None:
            for j in range(len(circle) - 1):
                mug_cylinder.append([previous_circle[j], previous_circle[j + 1], circle[j + 1], circle[j]])
        previous_circle = circle

    return mug_cylinder

def plot_cano(ax, faces):
    ax.add_collection3d(Poly3DCollection(faces, facecolors='r', linewidths=1, edgecolors='cyan', alpha=.5))