import pyray as rl
from personaje import Personaje
from utilities import *
import random
from constants import nombres_personajes
FILAS = 3
COLUMNAS = 5
PADDING = 30


class Tablero:

    def __init__(self) -> None:
        self._personajes = [[None for _ in range(COLUMNAS)]
                            for _ in range(FILAS)]


        ancho_celda = 180
        alto_celda = 200
        imagen_ruta_base = "../img/personaje_"
        n_personaje = 0
        for i in range(FILAS):
            for j in range(COLUMNAS):
                n_personaje += 1
                imagen_ruta = imagen_ruta_base + str(n_personaje) + ".png"
                pos_x = (j + 1) * (ancho_celda + PADDING) - ancho_celda
                pos_y = (i + 1) * (alto_celda + PADDING) - alto_celda

                self._personajes[i][j] = Personaje(x=pos_x, y=pos_y, ancho=ancho_celda, alto=alto_celda, imagen_ruta=imagen_ruta,
                                                   id=n_personaje,name=nombres_personajes[n_personaje])

    def dibujar(self, adivinando):
        for i in range(FILAS):
            for j in range(COLUMNAS):
                self._personajes[i][j].hover(adivinando)
                self._personajes[i][j].dibujar()

    def on_click(self, mouse_pos):
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if (self._personajes[i][j].on_click(mouse_pos)):
                    self._personajes[i][j].ajustar_opacidad()
    
    
    def obtener_personaje(self,mouse_pos) -> Personaje :
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if (self._personajes[i][j].on_click(mouse_pos)):
                    return self._personajes[i][j]
        
        return None
    
    def obtener_personaje_aleatorio(self) -> Personaje:
        fila_aleatoria = random.randint(0,FILAS-1)
        columna_aleatoria = random.randint(0,COLUMNAS-1)

        return self._personajes[fila_aleatoria][columna_aleatoria]
    