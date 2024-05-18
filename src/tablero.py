import pyray as rl
from personaje import Personaje

FILAS = 3
COLUMNAS = 5
PADDING = 30

class Tablero:
    def __init__(self) -> None:
        self._personajes = [[Personaje] * COLUMNAS for _ in range(FILAS)]

        ancho_celda = 150
        alto_celda = 250
        imagen_ruta = "../img/Ricardo-Fort.png"

        for i in range(FILAS):
            for j in range(COLUMNAS):
                pos_x = (j+1) * (ancho_celda+PADDING) - ancho_celda
                pos_y = i*alto_celda

                self._personajes[i][j] = Personaje(
                    pos_x,
                    pos_y,
                    ancho_celda,
                    alto_celda,
                    imagen_ruta
                )

    def dibujar(self):
        for i in range(FILAS):
            for j in range(COLUMNAS):
                self._personajes[i][j].dibujar()

    def on_click(self, mouse_pos):
        for i in range(FILAS):
            for j in range(COLUMNAS):
                if (self._personajes[i][j].on_click(mouse_pos)):
                    self._personajes[i][j].ajustar_opacidad()


                
            
                
