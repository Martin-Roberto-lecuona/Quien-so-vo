import pyray as rl

class botonAdivinar:
    def __init__(self,x,y,ancho,alto) -> None:
        self._rectangulo = rl.Rectangle(x,y,ancho,alto)
        self._presionado = False
        self._color = rl.PURPLE

    def dibujar(self):

        rl.draw_rectangle_rounded(self._rectangulo,2.5,0,self._color)
        texto = "adivinar"
        measure = rl.measure_text_ex(rl.get_font_default(),texto,20,0)
        rl.draw_text(texto,int(self._rectangulo.x + self._rectangulo.width/2 - (measure.x/2)),int(self._rectangulo.y + self._rectangulo.height/2 - (measure.y/2)),20,rl.BLACK)
        
    def on_click(self,punto) -> bool:
        return rl.check_collision_point_rec(punto,self._rectangulo)
    
    def activar_boton(self) -> bool:
        if self._presionado == False:
            self._presionado = True
            self._color = rl.RED
            return True
        elif self._presionado==True:
            self._presionado =False
            self._color = rl.PURPLE
            return False
