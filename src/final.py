import pyray as rl
import sys
from utilities import add_path_file

ANCHO_MOUSE = 0.5
FONT_SIZE = 40
IMAGE_BACKGROUND = add_path_file("pantallaLoser.png")

class Final:

    def __init__(self, bkg_width, bkg_heigh, imagen_ruta, ganar):
        self._textura = rl.load_texture(imagen_ruta)
        if (self._textura.id == 0):
            rl.trace_log(rl.TraceLogLevel.LOG_WARNING,
                         f"failed to load texture from {imagen_ruta}")
            exit()

        print("Imagen Ruta: " + imagen_ruta)

        self._fondo = rl.Rectangle(0, 0, bkg_width, bkg_heigh)

        self._titulo = rl.Rectangle(((bkg_width-(bkg_width/2))/2),((bkg_heigh-(bkg_heigh/6))/20),(bkg_width/2),(bkg_heigh/4))

        self._cerrar_partida = rl.Rectangle((bkg_width / 4) - 10, bkg_heigh / 3,
                                          (bkg_width/2),(bkg_heigh/4))
        self._visible = 1
        self._ganar = ganar
        self._bkg_width = bkg_width
        self._bkg_heigh = bkg_heigh

    def dibujar(self):
        text = "PERDISTEEE"
        if self._ganar:
            text = "GANASSSTE"
        else :
            try:
                self.dibujar_fondo()
                self.dibujar_titulo(text)
                self.dibujar_boton_cerrar_partida()
            except ZeroDivisionError:
                print("ERROR DE TEXTURA")
                exit()


    def dibujar_titulo(self, text):
        TAM_FONT_TITULO = 70
        rl.draw_rectangle_rec(self._titulo,rl.YELLOW)
        texto_titulo = text
        tt_measure = rl.measure_text_ex(rl.get_font_default(),texto_titulo,TAM_FONT_TITULO,0.0)
        rl.draw_text(texto_titulo, int(self._titulo.x + self._titulo.width/2 - (tt_measure.x/2)),
                         int(self._titulo.y+self._titulo.height/2-(tt_measure.y/2)),TAM_FONT_TITULO,rl.BLACK)

    def dibujar_fondo(self):
        escala_ancho = self._fondo.width / self._textura.width
        rl.draw_texture_ex(self._textura, (self._fondo.x, self._fondo.y),
                               0.0, escala_ancho, rl.WHITE)

    def dibujar_boton_cerrar_partida(self):
        TAM_FONT_UAP=40
        text_cerrar_partida = "Cerrar juego"
        tup_measure = rl.measure_text_ex(rl.get_font_default(),text_cerrar_partida,TAM_FONT_UAP,0.0)
        rl.draw_rectangle_rec(self._cerrar_partida, rl.BLUE)
        rl.draw_text(text_cerrar_partida, int(self._cerrar_partida.x + self._cerrar_partida.width/2 - (tup_measure.x/2)),
                         int(self._cerrar_partida.y + self._cerrar_partida.height/2 - (tup_measure.y/2)), TAM_FONT_UAP, rl.WHITE)


    def on_click(self, punto) -> bool:

        if rl.check_collision_point_rec(punto,self._cerrar_partida):
            print("Ejecutar Servidor")
            self._visible = 0
        return rl.check_collision_point_rec(punto,self._fondo)

    def get_visible(self):
        return self._visible == 1

    def __del__(self):
        rl.unload_texture(self._textura)