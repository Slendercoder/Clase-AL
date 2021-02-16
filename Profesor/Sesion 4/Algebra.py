import numpy as np
import matplotlib.pyplot as plt

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
#            print(f"Vector {nombre}=({x}, {y}) creado!")
        else:
            indice = self.nombres.index(nombre)
            self.vectores[0,indice] = x
            self.vectores[1,indice] = y
            self.colores[indice] = color
#            print(f"Vector {nombre}=({x}, {y}) modificado!")

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

class EspacioVectorial3D :

    def __init__(self) :
        self.vectores = np.array([[0], [0], [0]])
        self.colores = ['black']
        self.nombres = ['O']

    def asignar_vector(self, nombre, x, y, z, color='blue'):
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
        V = self.vectores
        num_rows, num_cols = V.shape
        ceros = [0]*num_cols
        origin = np.array([ceros, ceros, ceros])
        xses = V[0,:]
        x_max = np.max(xses) + 0.5
        x_min = np.min(xses) - 0.5
        yses = V[1,:]
        y_max = np.max(yses) + 0.5
        y_min = np.min(yses) - 0.5
        zses = V[1,:]
        z_max = np.max(zses) + 0.5
        z_min = np.min(zses) - 0.5
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(*origin,
                   xses,
                   yses,
                   zses
                  )
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.set_zlim([z_min, z_max])
        ax.view_init(elevacion, angulo)
        plt.show()

    def puntos(self, elevacion, angulo):
        V = self.vectores[:, 1:]
        xses = V[0,:]
        x_max = np.max(xses) + 0.5
        x_min = np.min(xses) - 0.5
        yses = V[1,:]
        y_max = np.max(yses) + 0.5
        y_min = np.min(yses) - 0.5
        zses = V[2,:]
        z_max = np.max(zses) + 0.5
        z_min = np.min(zses) - 0.5
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(xses, yses, zses)
        ax.view_init(elevacion, angulo)
        plt.show()
