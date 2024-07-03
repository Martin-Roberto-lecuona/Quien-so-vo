import pyray as rl
from personaje import Personaje
import random
from constants import nombres_personajes

class MiPersonaje:
    def __init__(self,x,y,ancho,alto,imagen_ruta) -> None:
        self._id = random.randint(1, 15)
        self._name = nombres_personajes[self._id]
        imagen_ruta = "../img/personaje_" + str(self._id) + ".png"
        image = rl.load_image(imagen_ruta)
        rl.image_resize(image, ancho, alto)
        self._textura = rl.load_texture_from_image(image)
        rl.unload_image(image)

        self._personaje_elegido = False

        if self._textura.id == 0:
            rl.trace_log(4, f"Failed to load texture from {imagen_ruta}")


        self._rectangulo = rl.Rectangle(x, y, ancho, alto)
    
    def dibujar(self):
        color_modificado = rl.Color(255, 255, 255, 255)
        borde_redondeado = 0.05
        grosor_borde = 2.5
        tam_texto = 20 

        rl.draw_rectangle_rounded(self._rectangulo,
                                   borde_redondeado, 0, rl.WHITE)
        rl.draw_texture_ex(self._textura,
                            (self._rectangulo.x, self._rectangulo.y), 0.0,
                            1, color_modificado)

        nombre_x = self._rectangulo.x + self._rectangulo.width // 2 - rl.measure_text(self._name, tam_texto) // 2
        nombre_y = self._rectangulo.y + self._rectangulo.height + 5 
        rl.draw_text(self._name, int(nombre_x), int(nombre_y), tam_texto, rl.WHITE)

        rl.draw_rectangle_rounded_lines(self._rectangulo,borde_redondeado,0,grosor_borde+1,rl.YELLOW)

    def on_click(self, punto) -> bool:
        return rl.check_collision_point_rec(punto,self._rectangulo)
    

    def personaje_elegido(self) -> bool: 
        return self._personaje_elegido
        

    def elegir_personaje(self, personaje):  
        if not self.personaje_elegido():
            rl.unload_texture(self._textura)
            image = rl.load_image(personaje._imagen_ruta)
            rl.image_resize(image, 150, 150)
            self._textura = rl.load_texture_from_image(image)
            rl.unload_image(image)
            self._name = personaje._name
            self._personaje_elegido = True
    

    def __del__(self):
        rl.unload_texture(self._textura)
