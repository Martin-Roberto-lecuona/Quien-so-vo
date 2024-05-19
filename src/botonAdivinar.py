import pyray as rl

class BotonAdivinar:
    def __init__(self,x,y,ancho,alto) -> None:
        self._rectangulo = rl.Rectangle(x,y,ancho,alto)
        self._esta_presionado = False
        self._color = rl.PURPLE

    def dibujar(self):

        rl.draw_rectangle_rounded(self._rectangulo,2.5,0,self._color)
        texto = "adivinar"
        medida = rl.measure_text_ex(rl.get_font_default(),texto,20,0)
        rl.draw_text(texto,int(self._rectangulo.x + self._rectangulo.width/2 - (medida.x/2)),int(self._rectangulo.y + self._rectangulo.height/2 - (medida.y/2)),20,rl.BLACK)
        
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
