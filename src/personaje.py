import pyray as rl

ANCHO_MOUSE = 0.5

class Personaje: 
    def __init__(self, x, y, ancho, alto, imagen_ruta, opacidad=1.0):
        image = rl.load_image(imagen_ruta)
        self._textura = rl.load_texture_from_image(image)
        rl.unload_image(image)

        if self._textura.id == 0:
            rl.trace_log(4, f"Failed to load texture from {imagen_ruta}")

        self._rectangulo = rl.Rectangle(
            x,
            y,
            ancho,
            alto
        )

        self._opacidad = opacidad

    def dibujar(self):
        color_modificado = rl.Color(255, 255, 255, 255)
        color_modificado.a = int(self._opacidad * 255)
        try:
            escala_ancho = self._rectangulo.width / self._textura.width
            escala_alto = self._rectangulo.height / self._textura.height
            escala = min(escala_ancho, escala_alto)

            rl.draw_texture_ex(
                self._textura, 
                (self._rectangulo.x, self._rectangulo.y), 
                0.0, 
                escala, 
                color_modificado
            )
        except ZeroDivisionError:
            print("ERROR DE TEXTURA")
            exit()

    def ajustar_opacidad(self):
        self._opacidad = 0.4 if self._opacidad == 1.0 else 1.0

    def on_click(self, punto) -> bool:
        mouse = rl.Rectangle(
            punto.x,
            punto.y,
            ANCHO_MOUSE,
            ANCHO_MOUSE
        )

        return rl.check_collision_recs(mouse, self._rectangulo)

    def __del__(self):
        rl.unload_texture(self._textura)
