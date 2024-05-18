import pyray as rl
from inicio import Inicio
from input import InputField
from tablero import Tablero

def main():
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 900
    # IMAGEN_RUTA = "./img/fondo-inicio2.png"
    ## corregir para que sea por ruta relativa
    IMAGEN_RUTA = "../img/fondo-inicio2.png"
    rl.init_window(SCREEN_WIDTH,SCREEN_HEIGHT,"Quien so vo?")
    rl.set_target_fps(60)

    inicio = Inicio(SCREEN_WIDTH,SCREEN_HEIGHT,IMAGEN_RUTA)

    while inicio.get_visible() and not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.DARKGREEN)
        inicio.dibujar()

        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            mouse_pos = rl.get_mouse_position()
            print(f"Mouse : {mouse_pos.x} , {mouse_pos.y}")
            inicio.on_click(mouse_pos)
        
        rl.end_drawing()
    
    tablero = Tablero()
    input_field = InputField(100,800,500,60)

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.DARKGREEN)
        input_field.process_input()

        tablero.dibujar()
        input_field.dibujar()

        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            mouse_pos = rl.get_mouse_position()
            print(f"mouse: {mouse_pos.x}, {mouse_pos.y}")
            tablero.on_click(mouse_pos)

        if input_field.overflow():
            input_field.dibujar_con_crlf(1.0)
        
        rl.end_drawing()
            
    rl.close_window()

    


    

    
    

if __name__ == "__main__":
    main()