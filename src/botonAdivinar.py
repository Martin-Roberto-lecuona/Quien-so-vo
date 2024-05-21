import pyray as rl
from boton import Boton

class BotonAdivinar(Boton):

    def __init__(self, rectangulo: rl.Rectangle, color, texto, tam_fuente) -> None:
        super().__init__(rectangulo, color, texto, tam_fuente)
        self._esta_presionado = False

    def dibujar(self):
        rl.draw_rectangle_rounded(self._rectangulo,2.5,0,self._color)
        rl.draw_text(self._texto,int(self._rectangulo.x + self._rectangulo.width/2 - (self._medidas_texto.x/2)),int(self._rectangulo.y + self._rectangulo.height/2 - (self._medidas_texto.y/2)),self._tam_fuente,rl.BLACK)
        
    def on_click(self,punto) -> bool:
        if rl.check_collision_point_rec(punto,self._rectangulo):
            return self.cambiar_estado()
        
        return self._esta_presionado
    
    def cambiar_estado(self) -> bool:
        if not self._esta_presionado:
            self._esta_presionado = not self._esta_presionado
            self._color=rl.RED
            return self._esta_presionado
        else:
            self._esta_presionado=not self._esta_presionado
            self._color = rl.PURPLE
            return self._esta_presionado
