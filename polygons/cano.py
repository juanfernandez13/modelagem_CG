import numpy as np
from function.hermite import hermite


def generate_circle(center, tangent, radius, num_points):
    # Gerar um círculo no plano perpendicular à tangente
    theta = np.linspace(0, 2 * np.pi, num_points)
    v = np.cross(tangent, [1, 0, 0])
    if np.linalg.norm(v) < 1e-6:
        v = np.cross(tangent, [0, 1, 0])
    v /= np.linalg.norm(v)
    u = np.cross(tangent, v)
    u /= np.linalg.norm(u)
    circle = np.array([center + radius * (np.cos(t) * u + np.sin(t) * v) for t in theta])
    return circle


def create_cano(p0, t0, p1, t1, num_pointsH=20, num_pointsC=20, radius=0.5):
    cano = []
    edge_color = "#bc57cd"
    face_color = "#ffd700"

    pontosHermite = hermite(p0, t0, p1, t1, num_pointsH)

    # Gerar círculos ao longo da curva da alça
    previous_circle = None
    for i in range(len(pontosHermite)):
        if i < len(pontosHermite) - 1:
            tangent = np.array(pontosHermite[i + 1]) - np.array(pontosHermite[i])
        else:
            tangent = np.array(pontosHermite[i]) - np.array(pontosHermite[i - 1])
        tangent /= np.linalg.norm(tangent)

        # Gerar o círculo usando o ponto atual e a tangente
        circle = generate_circle(np.array(pontosHermite[i]), tangent, radius, num_pointsC)

        # Conectar o círculo anterior ao atual, se houver
        if previous_circle is not None:
            for j in range(len(circle) - 1):
                cano.append([previous_circle[j], previous_circle[j + 1], circle[j + 1], circle[j]])
        previous_circle = circle

    return cano, face_color, edge_color
