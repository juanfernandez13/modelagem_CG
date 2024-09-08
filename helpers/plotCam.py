import numpy as np


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

# Função para projeção de perspectiva
def perspective_projection(point, fov, aspect_ratio, near, far):
    fov_rad = 1 / np.tan(fov / 2)

    projection_matrix = np.array([
        [fov_rad / aspect_ratio, 0, 0, 0],
        [0, fov_rad, 0, 0],
        [0, 0, -(far + near) / (far - near), -(2 * far * near) / (far - near)],
        [0, 0, -1, 0]
    ])

    point_homogeneous = np.append(point, 1)  # Coordenadas homogêneas
    projected_point = np.dot(projection_matrix, point_homogeneous)

    # Divisão por w para perspectiva correta
    if projected_point[3] != 0:
        projected_point /= projected_point[3]

    return projected_point[:2]  # Retorna x, y em 2D

# Função para transformar pontos do mundo para a visão da câmera e projetar em 2D
def project_to_2d(polygons, camera_position, target_position, fov, aspect_ratio, near, far):
    view_matrix = look_at(camera_position, target_position)

    projected_polygons = []
    for polygon in polygons:
        projected_polygon = []
        for point in polygon:
            point_homogeneous = np.append(point, 1)
            transformed_point = np.dot(view_matrix, point_homogeneous)[:3]
            projected_point = perspective_projection(transformed_point, fov, aspect_ratio, near, far)
            projected_polygon.append(projected_point)
        projected_polygons.append(projected_polygon)

    return projected_polygons

# Função para plotar os polígonos projetados em 2D
def plot_2d_projection(ax, polygons_2d, face_color, edge_color, alpha=0.5):
    for polygon in polygons_2d:
        polygon = np.array(polygon)
        ax.fill(polygon[:, 0], polygon[:, 1], facecolor=face_color, edgecolor=edge_color, alpha=alpha)


# Função para realizar a projeção e o plot
def plotCam(ax, polygons, fcolor, edcolor,cam_position=[10, 10, 10], target_position=[0, 0, 0], fov=np.pi/3, aspect_ratio=1, near=0.1, far=10):
    for i in range(0, len(polygons)):
        projected_polygons = project_to_2d(polygons[i], np.array(cam_position), np.array(target_position), fov,
                                           aspect_ratio, near, far)
        plot_2d_projection(ax, projected_polygons, fcolor[i], edcolor[i])
