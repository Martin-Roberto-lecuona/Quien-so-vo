import pyray as rl
from inicio import Inicio
from input import InputField
from tablero import Tablero
from utilities import *
from chatHistory import ChatHistory
from miPersonaje import MiPersonaje
from adivinar import botonAdivinar



SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900
# IMAGEN_RUTA = "img/fondo-inicio2.png"

def main():
    # print(rl.get_screen_width())
    # print(rl.get_screen_height())

    configuracion_inicial()

    dibujar_ventana_inicio()

    dibujar_ventana_juego()

    rl.close_window()

def configuracion_inicial():
    rl.set_config_flags(rl.ConfigFlags.FLAG_WINDOW_RESIZABLE | rl.ConfigFlags.FLAG_VSYNC_HINT)


    rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Quien so vo?")
    rl.set_window_min_size(320,240)
    rl.set_target_fps(60)

def dibujar_ventana_juego():
    ANCHO_TABLERO = 300
    ALTO_TABLERO = 650
    ANCHO_INPUT_FIELD = 500
    ALTO_INPUT_FIELD = 60

    tablero = Tablero()
    chat_history = ChatHistory(rl.get_screen_width()-(ANCHO_TABLERO + rl.get_screen_width()/30), 30, ANCHO_TABLERO, ALTO_TABLERO)
    input_field = InputField(100, 800, ANCHO_INPUT_FIELD, ALTO_INPUT_FIELD,chat_history)
    mi_personaje = MiPersonaje(1172,700,150,150,"img/personaje_desconocido.png")
    boton_adivinar = botonAdivinar(800,770,150,100)

    boton_adivinar_activado = False
    elegido_personaje_a_adivinar = False

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.BLUE)
        input_field.process_input()

        tablero.dibujar()
        input_field.dibujar()
        chat_history.dibujar()
        mi_personaje.dibujar()
        boton_adivinar.dibujar()


        # rl.draw_text(f"{rl.get_screen_width()}, {rl.get_screen_height()} fps: {rl.get_fps()}",0,0,30,rl.WHITE)
        rl.draw_text(f"actual: {rl.get_screen_width()}, {rl.get_screen_height()} base: {SCREEN_WIDTH}, {SCREEN_HEIGHT} fps: {rl.get_fps()}",0,0,30,rl.WHITE)

        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT) and elegido_personaje_a_adivinar == False:
            mouse_pos = rl.get_mouse_position()
            if boton_adivinar_activado == True :
                personaje_a_adivinado = tablero.obtener_personaje(mouse_pos)
                print(f"nombre personaje elegido para adivinar : {personaje_a_adivinado._nombre}")
                elegido_personaje_a_adivinar=True
                boton_adivinar.activar_boton()
                    

        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            mouse_pos = rl.get_mouse_position()
            print(f"mouse: {mouse_pos.x}, {mouse_pos.y}")
            tablero.on_click(mouse_pos)
            if boton_adivinar.on_click(mouse_pos) and elegido_personaje_a_adivinar == False:
              boton_adivinar_activado = boton_adivinar.activar_boton()
                


        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT) and mi_personaje.personaje_elegido() == False:
            print("eligiendo personaje")
            if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
                mouse_pos = rl.get_mouse_position()
                personaje_a_adivinar = tablero.obtener_personaje(mouse_pos)
                if personaje_a_adivinar != None:
                    print("Personaje elegible")
                    mi_personaje.elegir_personaje(personaje_a_adivinar)
            


        if input_field.overflow():
            input_field.dibujar_con_crlf(1.0)

        rl.end_drawing()

def dibujar_ventana_inicio():
    PATH_IMAGE = get_path_img()
    BACKGROUND_IMAGE = add_path_file(PATH_IMAGE,"fondo-inicio2.png")

    inicio = Inicio(SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE)
    while inicio.get_visible() and not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.DARKGREEN)
        inicio.dibujar()
        rl.draw_text(f"actual: {rl.get_screen_width()}, {rl.get_screen_height()} base: {SCREEN_WIDTH}, {SCREEN_HEIGHT} fps: {rl.get_fps()}",0,0,30,rl.WHITE)

        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            mouse_pos = rl.get_mouse_position()
            print(f"Mouse : {mouse_pos.x} , {mouse_pos.y}")
            inicio.on_click(mouse_pos)

        rl.end_drawing()


if __name__ == "__main__":
    main()
