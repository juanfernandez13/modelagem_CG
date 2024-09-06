import numpy as np


def scale_polygon(polygon, scale_vector):
    # Criar a matriz de escala 4x4
    S = np.array([
        [scale_vector[0], 0, 0, 0],
        [0, scale_vector[1], 0, 0],
        [0, 0, scale_vector[2], 0],
        [0, 0, 0, 1]
    ])

    scaled_polygon = []
    for face in polygon:
        face_escalada = []
        for vertice in face:
            # Converter o vértice para coordenadas homogêneas [x, y, z, 1]
            vertice_homogeneo = np.append(vertice, 1)
            # Multiplicar pela matriz de escala
            vertice_escalado_homogeneo = np.dot(S, vertice_homogeneo)
            # Voltar para as coordenadas 3D (x, y, z)
            vertice_escalado = vertice_escalado_homogeneo[:3]
            face_escalada.append(vertice_escalado)
        scaled_polygon.append(face_escalada)
    return scaled_polygon