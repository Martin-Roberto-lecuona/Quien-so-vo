import pyray as rl
import sys

ANCHO_MOUSE = 0.5


class Inicio:

    def __init__(self, ancho, alto, imagen_ruta):
        self._textura = rl.load_texture(imagen_ruta)
        if (self._textura.id == 0):
            rl.trace_log(rl.TraceLogLevel.LOG_WARNING,
                         f"failed to load texture from {imagen_ruta}")
            exit()

        print("Imagen Ruta: " + imagen_ruta)

        self._fondo = rl.Rectangle(0, 0, ancho, alto)

        self._titulo = rl.Rectangle(((ancho-(ancho/2))/2),((alto-(alto/6))/20),(ancho/2),(alto/4))

        self._crear_partida = rl.Rectangle((ancho / 4) - 10, alto / 3,
                                           ancho / 4, alto / 6)

        self._unirse_partida = rl.Rectangle((ancho / 2) + 10, alto / 3,
                                            ancho / 4, alto / 6)
        self._visible = 1

    def dibujar(self):
        try:
            self.dibujar_fondo()

            self.dibujar_titulo()

            self.dibujar_boton_iniciar_partida()

            self.dibujar_boton_unirse_a_partida()
        except ZeroDivisionError:
            print("ERROR DE TEXTURA")
            exit()


    def dibujar_titulo(self):
        TAM_FONT_TITULO = 70
        rl.draw_rectangle_rec(self._titulo,rl.YELLOW)
        texto_titulo = "Quien so vo?"
        tt_measure = rl.measure_text_ex(rl.get_font_default(),texto_titulo,TAM_FONT_TITULO,0.0)
        rl.draw_text(texto_titulo, int(self._titulo.x + self._titulo.width/2 - (tt_measure.x/2)),
                         int(self._titulo.y+self._titulo.height/2-(tt_measure.y/2)),TAM_FONT_TITULO,rl.BLACK)

    def dibujar_fondo(self):
        escala_ancho = self._fondo.width / self._textura.width
        rl.draw_texture_ex(self._textura, (self._fondo.x, self._fondo.y),
                               0.0, escala_ancho, rl.WHITE)

    def dibujar_boton_unirse_a_partida(self):
        TAM_FONT_UAP=40
        text_unirse_partida = "Unirse a Partida"
        tup_measure = rl.measure_text_ex(rl.get_font_default(),text_unirse_partida,TAM_FONT_UAP,0.0)
        rl.draw_rectangle_rec(self._unirse_partida, rl.BLUE)
        rl.draw_text(text_unirse_partida, int(self._unirse_partida.x + self._unirse_partida.width/2 - (tup_measure.x/2)),
                         int(self._unirse_partida.y + self._unirse_partida.height/2 - (tup_measure.y/2)), TAM_FONT_UAP, rl.WHITE)

    def dibujar_boton_iniciar_partida(self):
        TAM_FONT_IAP=40
        rl.draw_rectangle_rec(self._crear_partida, rl.RED)
        text_crear_partida = "Crear Partida"
        tcp_measure = rl.measure_text_ex(rl.get_font_default(),text_crear_partida,TAM_FONT_IAP,0.0)
        rl.draw_text(text_crear_partida, int(self._crear_partida.x + self._crear_partida.width/2 - (tcp_measure.x/2)),
                         int(self._crear_partida.y + self._crear_partida.height/2 - (tcp_measure.y/2)), TAM_FONT_IAP, rl.WHITE)

    def on_click(self, punto) -> bool:

        if rl.check_collision_point_rec(punto,self._crear_partida):
            print("Ejecutar Servidor")
            self._visible = 0
        elif rl.check_collision_point_rec(punto,self._unirse_partida):
            print("Ejecutar Cliente")
            self._visible = 0

        return rl.check_collision_point_rec(punto,self._fondo)

    def get_visible(self):
        return self._visible == 1

    def __del__(self):
        rl.unload_texture(self._textura)
