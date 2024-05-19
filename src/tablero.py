import pyray as rl
from personaje import Personaje

FILAS = 3
COLUMNAS = 5
PADDING = 30


class Tablero():

    def __init__(self,screen_width, screen_height) -> None:
            # self._personajes = [[Personaje] * COLUMNAS for _ in range(FILAS)]
        self._personajes = [[None for _ in range(COLUMNAS)]
                            for _ in range(FILAS)]

        ancho_celda = screen_width - 700
        alto_celda = screen_height - 500
        imagen_ruta_base = "../img/personaje_"
        n_personaje = 0
        for i in range(FILAS):
            for j in range(COLUMNAS):
                n_personaje += 1
                imagen_ruta = imagen_ruta_base + str(n_personaje) + ".png"
                pos_x = (j + 1) * (ancho_celda + PADDING) - ancho_celda
                pos_y = (i + 1) * (alto_celda + PADDING) - alto_celda

                self._personajes[i][j] = Personaje(pos_x, pos_y, ancho_celda,
                                                   alto_celda, imagen_ruta)

    def dibujar(self):
        for i in range(FILAS):
            for j in range(COLUMNAS):
                self._personajes[i][j].dibujar()

    def on_click(self, mouse_pos):
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if (self._personajes[i][j].on_click(mouse_pos)):
                    self._personajes[i][j].ajustar_opacidad