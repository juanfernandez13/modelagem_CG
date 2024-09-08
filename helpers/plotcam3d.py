import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Função para normalizar vetores
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


# Função para calcular a matriz de visualização da câmera
def look_at(camera_position, target_position, up_vector=np.array([0, 0, 1])):
    forward = normalize(target_position - camera_position)
    right = normalize(np.cross(forward, up_vector))
    up = np.cross(right, forward)

    # Matriz de rotação da câmera
    rotation_matrix = np.array([right, up, -forward])

    # Translação da câmera
    translation = -np.dot(rotation_matrix, camera_position)

    # Matriz de visualização
    view_matrix = np.eye(4)
    view_matrix[:3, :3] = rotation_matrix
    view_matrix[:3, 3] = translation
    return view_matrix


# Função para transformar pontos do mundo para a visão da câmera
def apply_view_transform(polygons, view_matrix):
    transformed_polygons = []
    for polygon in polygons:
        transformed_polygon = []
        for point in polygon:
            point_homogeneous = np.append(point, 1)  # Adiciona coordenada homogênea
            transformed_point = np.dot(view_matrix, point_homogeneous)[:3]
            transformed_polygon.append(transformed_point)
        transformed_polygons.append(transformed_polygon)
    return transformed_polygons


# Função para plotar os polígonos
def plot_polygons(ax, polygons, fcolors, edolors, camera_position, target_position, fov):
    # Define a matriz de visualização da câmera
    view_matrix = look_at(camera_position, target_position)
    # Ajusta o campo de visão da câmera (fov)
    ax.dist = fov

    for i in range(0, len(polygons)):
        # Aplica a transformação de visualização aos polígonos
        transformed_polygons = apply_view_transform(polygons[i], view_matrix)
        # Plota os polígonos transformados
        for polygon in transformed_polygons:
            verts = [list(map(list, polygon))]
            ax.add_collection3d(Poly3DCollection(verts, facecolors=fcolors[i], linewidths=1, edgecolors=edolors[i], alpha=.5))
