import numpy as np

def create_cube():
    # Definindo os vértices do cubo
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

    # Definindo as faces do cubo
    faces = [[vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [2, 3, 7, 6]]]

    face_color = "#cdbf9b"
    edge_color = "#643f23"

    return faces, face_color, edge_color

