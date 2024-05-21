import pyray as rl
from boton import Boton
from constants import game_name  


class Inicio:

    def __init__(self, ancho, alto, imagen_ruta):
        self._textura = rl.load_texture(imagen_ruta)
        if (self._textura.id == 0):
            rl.trace_log(rl.TraceLogLevel.LOG_WARNING,
                         f"failed to load texture from {imagen_ruta}")
            exit()

        print("Imagen Ruta: " + imagen_ruta)

        self._fondo = rl.Rectangle(0, 0, ancho, alto)
        self._rectangulo_titulo = rl.Rectangle(((ancho-(ancho/2))/2),((alto-(alto/6))/20),(ancho/2),(alto/4))
        rectangulo_iniciar_partida = rl.Rectangle((ancho / 4) - 10, alto / 3, ancho / 4, alto / 6)
        rectangulo_unirse_partida = rl.Rectangle((ancho / 2) + 10, alto / 3, ancho / 4, alto / 6)

        self._tam_titulo = 70
        self._medida_titulo = rl.measure_text_ex(rl.get_font_default(),game_name,self._tam_titulo,0.0)
        self._boton_iniciar_partida = Boton(rectangulo_iniciar_partida,rl.BLUE,"iniciar partida",40)
        self._boton_unirse_partida = Boton(rectangulo_unirse_partida,rl.RED,"unirse a partida",40)
        self._visible = 1

    def dibujar(self):
        try:
            self.dibujar_fondo()
            self.dibujar_titulo()
            self._boton_iniciar_partida.dibujar()
            self._boton_unirse_partida.dibujar()

        except ZeroDivisionError:
            print("ERROR DE TEXTURA")
            exit()


    def dibujar_titulo(self):
        rl.draw_rectangle_rec(self._rectangulo_titulo,rl.YELLOW)
        rl.draw_text(game_name, int(self._rectangulo_titulo.x + self._rectangulo_titulo.width/2 - (self._medida_titulo.x/2)),
                         int(self._rectangulo_titulo.y+self._rectangulo_titulo.height/2-(self._medida_titulo.y/2)),self._tam_titulo,rl.BLACK)

    def dibujar_fondo(self):
        escala_ancho = self._fondo.width / self._textura.width
        rl.draw_texture_ex(self._textura, (self._fondo.x, self._fondo.y),
                               0.0, escala_ancho, rl.WHITE)

    def on_click(self, punto) -> bool:
        if self._boton_iniciar_partida.on_click(punto):
            print("Ejecutar Servidor")
            self._visible = 0
        elif self._boton_unirse_partida.on_click(punto):
            print("Ejecutar Cliente")
            self._visible = 0

        return rl.check_collision_point_rec(punto,self._fondo)

    def get_visible(self):
        return self._visible == 1

    def __del__(self):
        rl.unload_texture(self._textura)
