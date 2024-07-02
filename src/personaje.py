import pyray as rl

# ANCHO_MOUSE = 0.5


class Personaje:

    def __init__(self, x, y, ancho, alto, imagen_ruta, opacidad=1.0, id = 0, name = "None"):
        self._name = name
        self._id = id
        self._hover_color = rl.YELLOW
        self._imagen_ruta = imagen_ruta
        image = rl.load_image(imagen_ruta)
        rl.image_resize(image, ancho, alto)
        self._textura = rl.load_texture_from_image(image)
        rl.unload_image(image)

        if self._textura.id == 0:
            rl.trace_log(4, f"Failed to load texture from {imagen_ruta}")
            exit(-1)

        self._rectangulo = rl.Rectangle(x, y, ancho, alto)


        self._opacidad = opacidad

    def dibujar(self):
        color_modificado = rl.Color(255, 255, 255, 255)
        color_modificado.a = int(self._opacidad * 255)
        borde_redondeado = 0.05
        grosor_borde = 2.5
        tam_texto = 20 

        rl.draw_rectangle_rounded(self._rectangulo, borde_redondeado, 0, rl.WHITE)
        rl.draw_texture_ex(self._textura, (self._rectangulo.x, self._rectangulo.y), 0.0, 1, color_modificado)

        nombre_x = self._rectangulo.x + self._rectangulo.width // 2 - rl.measure_text(self._name, tam_texto) // 2
        nombre_y = self._rectangulo.y + self._rectangulo.height + 5 
        rl.draw_text(self._name, int(nombre_x), int(nombre_y), tam_texto, rl.WHITE)
        borde = rl.BLACK
        if self.on_hover():
            borde = self._hover_color

        rl.draw_rectangle_rounded_lines(self._rectangulo,borde_redondeado,0,grosor_borde,borde)

    def on_hover(self):
        return rl.check_collision_point_rec(rl.get_mouse_position(),self._rectangulo)

    def hover(self,adivinando):
        if self.on_hover():
            if adivinando:
                self._hover_color= rl.RED
            else:
                self._hover_color= rl.YELLOW

    def ajustar_opacidad(self):
        self._opacidad = 0.4 if self._opacidad == 1.0 else 1.0

    def on_click(self, punto) -> bool:
        return rl.check_collision_point_rec(punto,self._rectangulo)


    def __del__(self):
        rl.unload_texture(self._textura)
