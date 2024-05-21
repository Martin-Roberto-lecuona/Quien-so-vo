import pyray as rl

class Boton:
    def __init__(self,rectangulo: rl.Rectangle, color, texto, tam_fuente) -> None:
        self._rectangulo = rectangulo
        self._color = color
        self._texto = texto
        self._tam_fuente = tam_fuente
        self._medidas_texto = rl.measure_text_ex(rl.get_font_default(), self._texto, self._tam_fuente,0.0)
    
    def dibujar(self):
        rl.draw_rectangle_rec(self._rectangulo, self._color)
        rl.draw_text(self._texto, int(self._rectangulo.x + self._rectangulo.width/2 - (self._medidas_texto.x/2)),
                         int(self._rectangulo.y + self._rectangulo.height/2 - (self._medidas_texto.y/2)), self._tam_fuente, rl.WHITE)

    def on_click(self,punto) -> bool:
        return rl.check_collision_point_rec(punto, self._rectangulo)
        



