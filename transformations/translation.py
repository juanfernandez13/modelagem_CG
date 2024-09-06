import numpy as np

def translation(polygon, translation_vector):
    # Criar a matriz de translação 4x4
    T = np.array([
        [1, 0, 0, translation_vector[0]],
        [0, 1, 0, translation_vector[1]],
        [0, 0, 1, translation_vector[2]],
        [0, 0, 0, 1]
    ])

    translated_polygon = []
    for face in polygon:
        face_transladada = []
        for vertice in face:
            # Converter o vértice para coordenadas homogêneas [x, y, z, 1]
            vertice_homogeneo = np.append(vertice, 1)
            # Multiplicar pela matriz de translação
            vertice_transladado_homogeneo = np.dot(T, vertice_homogeneo)
            # Voltar para as coordenadas 3D (x, y, z)
            vertice_transladado = vertice_transladado_homogeneo[:3]
            face_transladada.append(vertice_transladado)
        translated_polygon.append(face_transladada)
    return translated_polygon
