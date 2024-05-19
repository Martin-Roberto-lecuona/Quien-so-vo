import pyray as rl

ANCHO_MOUSE = 0.5


class Personaje:

    def __init__(self, x, y, ancho, alto, imagen_ruta, opacidad=1.0):
        self.nombre = "ARGENTINA"
        image = rl.load_image(imagen_ruta)
        rl.image_resize(image, ancho, alto)
        self._textura = rl.load_texture_from_image(image)
        rl.unload_image(image)

        if self._textura.id == 0:
            rl.trace_log(4, f"Failed to load texture from {imagen_ruta}")

        self._rectangulo = rl.Rectangle(x, y, ancho, alto)

        self._opacidad = opacidad

    def dibujar(self):
        color_modificado = rl.Color(255, 255, 255, 255)
        color_modificado.a = int(self._opacidad * 255)
        try:
            borde_redondeado = 0.05  # Radio del borde redondeado
            rl.draw_rectangle_rounded(self._rectangulo,
                                   borde_redondeado, 0, rl.WHITE)
            rl.draw_rectangle_rounded_lines(self._rectangulo,
                                         borde_redondeado, 0, 2, rl.BLACK)
            rl.draw_texture_ex(self._textura,
                               (self._rectangulo.x, self._rectangulo.y), 0.0,
                               1, color_modificado)

            nombre_x = self._rectangulo.x + self._rectangulo.width // 2 - rl.measure_text(self.nombre, 20) // 2
            nombre_y = self._rectangulo.y + self._rectangulo.height + 5 
            rl.draw_text(self.nombre, int(nombre_x), int(nombre_y), 20, rl.WHITE)
                    
        except ZeroDivisionError:
            print("ERROR DE TEXTURA")
            exit()

    def ajustar_opacidad(self):
        self._opacidad = 0.4 if self._opacidad == 1.0 else 1.0

    def on_click(self, punto) -> bool:
        mouse = rl.Rectangle(punto.x, punto.y, ANCHO_MOUSE, ANCHO_MOUSE)

        return rl.check_collision_recs(mouse, self._rectangulo)

    def __del__(self):
        rl.unload_texture(self._textura)
