import pyray as rl
import sys
from utilities import add_path_file

ANCHO_MOUSE = 0.5
FONT_SIZE = 40
IMAGE_BACKGROUND = add_path_file("pantallaLoser.png")
FONT_PATH = add_path_file("Roboto-Black.ttf") 

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
        if self._ganar:
            self.dibujar_perder()
        else :
            ## hacer funcion
            try:
                self.dibujar_fondo()

                self.dibujar_titulo()

                self.dibujar_boton_cerrar_partida()

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

    
    def draw_background_lose(self):
        rl.clear_background(rl.RAYWHITE)
        rl.draw_rectangle(0, 0, self._bkg_width, self._bkg_heigh, rl.SKYBLUE)

    def draw_image_lose(self,texture):
        source_rec = rl.Rectangle(0, 0, texture.width, texture.height)
        dest_rec = rl.Rectangle(self._bkg_width / 2, self._bkg_heigh / 2, texture.width, texture.height)
        origin = rl.Vector2(texture.width / 2, texture.height / 2)
        rotation = 0
        rl.draw_texture_pro(texture, source_rec, dest_rec, origin, rotation, rl.WHITE)

    def draw_message_lose(self,font):
        message1 = "Perdiste!"

        text_width1 = rl.measure_text_ex(font, message1, FONT_SIZE, 1).x
        text_height = FONT_SIZE 

        rl.draw_text_ex(font, message1, rl.Vector2((self._bkg_width - text_width1) / 2, (self._bkg_heigh - text_height) / 2), FONT_SIZE, 1, rl.BLACK)

        
    
    def load_texture_lose():
        image = rl.load_image(IMAGE_BACKGROUND)
        return rl.load_texture_from_image(image)

    def load_font_lose():
        return rl.load_font(FONT_PATH)
    
    def dibujar_perder(self):
        texture = self.load_texture_lose()
        font = self.load_font_lose()
        self.draw_background_lose()
        self.draw_image_lose(texture)
        self.draw_message_lose(font)