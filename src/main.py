import pyray as rl
from screeninfo import get_monitors
from inicio import Inicio
from input import InputField
from tablero import Tablero


def main():
    window_width = 800
    window_height = 600

    monitor = get_monitors()[0]
    SCREEN_WIDTH = monitor.width
    SCREEN_HEIGHT = monitor.height

    window_width = int(SCREEN_WIDTH * 0.75)
    window_height = int(SCREEN_HEIGHT * 0.75)

    rl.init_window(window_width, window_height, "Quien so vo?")

    SCREEN_WIDTH = rl.get_screen_width()
    SCREEN_HEIGHT = rl.get_screen_height()

    rl.set_window_title("Quien so vo?")

    rl.set_target_fps(60)

    IMAGEN_RUTA = "../img/fondo-inicio2.png"

    inicio = Inicio(window_width, window_height, IMAGEN_RUTA)

    while inicio.get_visible() and not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.DARKGREEN)
        inicio.dibujar()

        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            mouse_pos = rl.get_mouse_position()
            print(f"Mouse : {mouse_pos.x} , {mouse_pos.y}")
            inicio.on_click(mouse_pos)

        rl.end_drawing()

    tablero = Tablero(window_width,window_height)
    #input_field = InputField(100, 800, 500, 60)
    input_field = InputField(100, window_height - 125, 500, 60)

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
