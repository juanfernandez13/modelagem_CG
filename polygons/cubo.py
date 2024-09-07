import numpy as np

def create_cube():
    # Definindo os vértices do cubo
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

    vertices2 = np.array([[0.1, 0.1, 0.1], [0.9, 0.1, 0.1], [0.9, 0.9, 0.1], [0.1, 0.9, 0.1],
                         [0.1, 0.1, 1], [0.9, 0.1, 1], [0.9, 0.9, 1], [0.1, 0.9, 1]])

    # Definindo as faces da caixa
    faces = [[vertices[j] for j in [0, 1, 2, 3]],
             [vertices[j] for j in [0, 3, 7, 4]],
             [vertices[j] for j in [1, 2, 6, 5]],
             [vertices[j] for j in [0, 1, 5, 4]],
             [vertices[j] for j in [2, 3, 7, 6]],

             #Criando caixa menor
             [vertices2[j] for j in [0, 1, 2, 3]],
             [vertices2[j] for j in [0, 3, 7, 4]],
             [vertices2[j] for j in [1, 2, 6, 5]],
             [vertices2[j] for j in [0, 1, 5, 4]],
             [vertices2[j] for j in [2, 3, 7, 6]],

             #Conectando base da cubo menor com o maior
             [vertices2[0], vertices2[1], vertices[1], vertices[0]],
             [vertices2[1], vertices2[2], vertices[2], vertices[1]],
             [vertices2[2], vertices2[3], vertices[3], vertices[2]],
             [vertices2[0], vertices2[3], vertices[3], vertices[0]],
             #Conectando topo da cubo menor com o maior
             [vertices2[4], vertices2[5], vertices[5], vertices[4]],
             [vertices2[5], vertices2[6], vertices[6], vertices[5]],
             [vertices2[6], vertices2[7], vertices[7], vertices[6]],
             [vertices2[4], vertices2[7], vertices[7], vertices[4]],

             #Braços internos
             [vertices2[0], vertices2[4], vertices[4], vertices[0]],
             [vertices2[1], vertices2[5], vertices[5], vertices[1]],
             [vertices2[2], vertices2[6], vertices[6], vertices[2]],
             [vertices2[3], vertices2[7], vertices[7], vertices[3]],
             ]

    face_color = "#cdbf9b"
    edge_color = "#643f23"

    return faces, face_color, edge_color

