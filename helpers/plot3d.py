from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def plot_3d(ax, faces, f_color='r', e_color="cyan", alpha=.5):
    ax.add_collection3d(Poly3DCollection(faces, facecolors=f_color, linewidths=1, edgecolors=e_color, alpha=alpha))
