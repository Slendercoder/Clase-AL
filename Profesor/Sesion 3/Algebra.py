import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

class EspacioVectorial2D :

    def __init__(self) :
        self.vectores = np.array([[0], [0]])
        self.colores = ['black']
        self.nombres = ['O']

    def asignar_vector(self, nombre, x, y, color='blue'):
        if nombre not in self.nombres:
            self.vectores = np.c_[self.vectores, np.array([[x], [y]])]
            self.nombres.append(nombre)
            self.colores.append(color)
        else:
            indice = self.nombres.index(nombre)
            self.vectores[0,indice] = x
            self.vectores[1,indice] = y
            self.colores[indice] = color

    def coordenadas(self, nombre) :
        indice = self.nombres.index(nombre)
        return self.vectores[:,indice]

    def dibujar(self, dim=1, ajustar=False):
        V = self.vectores
        num_rows, num_cols = V.shape
        ceros = [0]*num_cols
        origin = np.array([ceros, ceros])
        xses = V[0,:]
        x_max = np.max(xses) + 0.5
        x_min = np.min(xses) - 0.5
        yses = V[1,:]
        y_max = np.max(yses) + 0.5
        y_min = np.min(yses) - 0.5
        if ajustar:
            fig = plt.subplots()
        else:
            fig = plt.subplots(figsize=(dim*(x_max-x_min), dim*(y_max-y_min)))
        plt.quiver(*origin,
                   xses,
                   yses,
                   color=self.colores,
                   angles='xy',
                   scale_units='xy',
                   scale=1
                  )
        plt.axis([x_min, x_max, y_min, y_max])
        plt.show()

    def puntos(self, dim=1):
        V = self.vectores[:, 1:]
        xses = V[0,:]
        x_max = np.max(xses) + 0.5
        x_min = np.min(xses) - 0.5
        yses = V[1,:]
        y_max = np.max(yses) + 0.5
        y_min = np.min(yses) - 0.5
        fig = plt.subplots(figsize=(dim*(x_max-x_min), dim*(y_max-y_min)))
        plt.scatter(xses, yses)
        plt.axis([x_min, x_max, y_min, y_max])
        plt.show()


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().

	taken from: https://stackoverflow.com/questions/13685386/matplotlib-equal-unit-length-with-equal-aspect-ratio-z-axis-is-not-equal-to
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


'''
Next two functions to add color to vectors.
Adapted from: https://gist.github.com/sytrus-in-github/a3b2ef4414fb144cb08505a060c99b18
'''
def repeatForEach(elements, times):
    return [e for e in elements for _ in range(times)]
def renderColorsForQuiver3d(colors):
    colors = list(filter(lambda x: x!='black', colors))
    return colors + repeatForEach(colors, 2)

class EspacioVectorial3D :

    def __init__(self) :
        self.vectores = np.array([[0], [0], [0]])
        self.colores = ['black']
        self.nombres = ['O']

    def asignar_vector(self, nombre, x, y, z, color='red'):
        if nombre not in self.nombres:
            self.vectores = np.c_[self.vectores, np.array([[x], [y], [z]])]
            self.nombres.append(nombre)
            self.colores.append(color)
        else:
            indice = self.nombres.index(nombre)
            self.vectores[0,indice] = x
            self.vectores[1,indice] = y
            self.vectores[2,indice] = z
            self.colores[indice] = color

    def coordenadas(self, nombre) :
        indice = self.nombres.index(nombre)
        return self.vectores[:,indice]

    def dibujar(self, elevacion=30, angulo=45):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        V = self.vectores
        num_rows, num_cols = V.shape
        ceros = [0]*num_cols
        origin = np.array([ceros, ceros, ceros])
        xses = V[0,:]
        yses = V[1,:]
        zses = V[2,:]
        ax.quiver(*origin,
                   xses,
                   yses,
                   zses,
                   colors=renderColorsForQuiver3d(self.colores)
                  )
        x_max = np.max(xses) + 0.5
        x_min = np.min(xses) - 0.5
        y_max = np.max(yses) + 0.5
        y_min = np.min(yses) - 0.5
        z_max = np.max(zses) + 0.5
        z_min = np.min(zses) - 0.5
        x_middle = np.mean([x_max, x_min])
        x_range = x_max - x_min
        y_middle = np.mean([y_max, y_min])
        y_range = y_max - y_min
        z_middle = np.mean([z_max, z_min])
        z_range = z_max - z_min
        plot_radius = 0.5*max([x_range, y_range, z_range])
        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
        ax.view_init(elevacion, angulo)
        plt.show()

    def puntos(self, elevacion=30, angulo=45):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        V = self.vectores[:, 1:]
        xses = V[0,:]
        yses = V[1,:]
        zses = V[2,:]
        ax.scatter(xses, yses, zses)
        set_axes_equal(ax)
        ax.view_init(elevacion, angulo)
        plt.show()

    def vectores_puntos(self, elevacion=30, angulo=45, num_vectores=1):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        num_vectores += 1
        V = self.vectores[:, num_vectores:]
        xses = V[0,:]
        yses = V[1,:]
        zses = V[2,:]
        ax.scatter(xses, yses, zses)
        V = self.vectores[:, :num_vectores]
        num_rows, num_cols = V.shape
        ceros = [0]*num_cols
        origin = np.array([ceros, ceros, ceros])
        xses = V[0,:]
        yses = V[1,:]
        zses = V[2,:]
        ax.quiver(*origin,
		           xses,
		           yses,
		           zses,
                   colors=renderColorsForQuiver3d(self.colores[:num_vectores])
		          )
        set_axes_equal(ax)
        ax.view_init(elevacion, angulo)
        plt.show()
