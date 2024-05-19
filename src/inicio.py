import pyray as rl
import sys

ANCHO_MOUSE = 0.5


class Inicio:

    def __init__(self, ancho, alto, imagen_ruta):
        image = rl.load_image(imagen_ruta)
        self._textura = rl.load_texture_from_image(image)
        rl.unload_image(image)
        if (self._textura.id == 0):
            rl.trace_log(rl.LOG_WARNING,
                         f"failed to load texture from {imagen_ruta}")

        print("Imagen Ruta: " + imagen_ruta)

        self._fondo = rl.Rectangle(0, 0, ancho, alto)

        self._crear_partida = rl.Rectangle((ancho / 4) - 10, alto / 3,
                                           ancho / 4, alto / 6)

        self._unirse_partida = rl.Rectangle((ancho / 2) + 10, alto / 3,
                                            ancho / 4, alto / 6)
        self._visible = 1

    def dibujar(self):
        try:
            escala_ancho = self._fondo.width / self._textura.width
            rl.draw_texture_ex(self._textura, (self._fondo.x, self._fondo.y),
                               0.0, escala_ancho, rl.WHITE)

            rl.draw_rectangle_rec(self._crear_partida, rl.RED)
            rl.draw_text("Crear Partida", int(self._crear_partida.x + 10),
                         int(self._crear_partida.y + 10), 20, rl.WHITE)

            rl.draw_rectangle_rec(self._unirse_partida, rl.BLUE)
            rl.draw_text("Unirse a Partida", int(self._unirse_partida.x + 10),
                         int(self._unirse_partida.y + 10), 20, rl.WHITE)
        except ZeroDivisionError:
            print("ERROR DE TEXTURA")
            exit()

    def on_click(self, punto) -> bool:
        mouse = rl.Rectangle(punto.x, punto.y, ANCHO_MOUSE, ANCHO_MOUSE)

        if rl.check_collision_recs(mouse, self._crear_partida):
            print("Ejecutar Servidor")
            self._visible = 0
        elif rl.check_collision_recs(mouse, self._unirse_partida):
            print("Ejecutar Cliente")
            self._visible = 0

        return rl.check_collision_recs(mouse, self._fondo)

    def get_visible(self):
        return self._visible == 1

    def __del__(self):
        rl.unload_texture(self._textura)
