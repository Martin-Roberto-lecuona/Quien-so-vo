import pyray as rl
from final import Final
from inicio import Inicio
from input import InputField
from tablero import Tablero
from utilities import *
from chatHistory import ChatHistory
from miPersonaje import MiPersonaje
from botonAdivinar import BotonAdivinar
from constants import game_name  
import socket
from screeninfo import get_monitors
import gc

el_socket   = None
creador     = None
ganaste     = False

monitor = get_monitors()[0]
SCREEN_WIDTH = int(monitor.width * 0.85)
SCREEN_HEIGHT= int(monitor.height * 0.85)


# SCREEN_WIDTH    = 1500
# SCREEN_HEIGHT   = 900

def main():
    configuracion_inicial()

    dibujar_ventana_inicio()

    dibujar_ventana_juego()

    dibujar_ventana_final()

    rl.close_window()

def configuracion_inicial():
    rl.set_config_flags(rl.ConfigFlags.FLAG_WINDOW_RESIZABLE | rl.ConfigFlags.FLAG_VSYNC_HINT)


    rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, game_name)
    rl.set_window_min_size(320,240)
    rl.set_target_fps(60)

def dibujar_ventana_juego():
    global ganaste
    ANCHO_TABLERO = 300
    ALTO_TABLERO = 650
    ANCHO_INPUT_FIELD = 500
    ALTO_INPUT_FIELD = 60

    tablero = Tablero()
    chat_history = ChatHistory(rl.get_screen_width()-(ANCHO_TABLERO + rl.get_screen_width()/30), 30, ANCHO_TABLERO, ALTO_TABLERO, el_socket=el_socket, creador=creador)
    input_field = InputField(100, 800, ANCHO_INPUT_FIELD, ALTO_INPUT_FIELD,chat_history)
    mi_personaje = MiPersonaje(1172,700,150,150, add_path_file("personaje_desconocido.png"))
    boton_adivinar = BotonAdivinar(800,770,150,100)
    boton_adivinar_presionado = False
    terminar_juego = False

    while not rl.window_should_close() and not terminar_juego:
        rl.begin_drawing()
        rl.clear_background(rl.BLUE)
        input_field.process_input()

        tablero.dibujar(boton_adivinar_presionado)
        input_field.dibujar()
        chat_history.dibujar()
        mi_personaje.dibujar()
        boton_adivinar.dibujar()


        rl.draw_text(f"actual: {rl.get_screen_width()}, {rl.get_screen_height()} base: {SCREEN_WIDTH}, {SCREEN_HEIGHT} fps: {rl.get_fps()}",0,0,30,rl.WHITE)

        mi_personaje.elegir_personaje(tablero.obtener_personaje_aleatorio())
        
        personaje_adivinado = chat_history.get_personaje_adivinado()
        if personaje_adivinado != -1:
            print("personaje_adivinado: " + str(personaje_adivinado))
            print("mi_personaje.get_id(): " + str(mi_personaje.get_id()))
            if int(personaje_adivinado) == int(mi_personaje.get_id()):
                chat_history.recive_command("ganaste")
                ganaste = False
            else:
                chat_history.recive_command("perdiste")
                ganaste = True
            terminar_juego = True
        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            mouse_pos = rl.get_mouse_position()
            print(f"mouse: {mouse_pos.x}, {mouse_pos.y}")
            tablero.on_click(mouse_pos)
            boton_adivinar_presionado = boton_adivinar.on_click(mouse_pos)

            if boton_adivinar_presionado :
                personaje_adivinado = tablero.obtener_personaje(mouse_pos)
                if personaje_adivinado != None:
                    print(f"personaje Adivinado: {personaje_adivinado._name}")
                    chat_history.recive_command("adivinar " + str(personaje_adivinado._id))
                    boton_adivinar_presionado = boton_adivinar.cambiar_estado()
                    response = chat_history.get_win_response()
                    while (response == None):
                        response = chat_history.get_win_response()
                    print(f"response ultima {response}")
                    if (str(response) == "ganaste"):
                        ganaste = True
                    else:
                        ganaste = False
                    terminar_juego = True
        
        if input_field.overflow():
            input_field.dibujar_con_crlf(1.0)

        rl.end_drawing()
    
    del chat_history

def dibujar_ventana_inicio():
    global creador
    global el_socket
    BACKGROUND_IMAGE = add_path_file("fondo-inicio2.png")

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
    el_socket,creador = inicio.get_socket()
    print(f"el creador : {creador}")
    print(f"socket en dibujar ventana inicio {el_socket}")

def dibujar_ventana_final():
    global ganaste
    BACKGROUND_IMAGE = add_path_file("fondo-inicio2.png")
    
    final = Final(SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE, ganaste)
    while final.get_visible() and not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.DARKGREEN)
        final.dibujar()
        rl.draw_text(f"actual: {rl.get_screen_width()}, {rl.get_screen_height()} base: {SCREEN_WIDTH}, {SCREEN_HEIGHT} fps: {rl.get_fps()}",0,0,30,rl.WHITE)

        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            mouse_pos = rl.get_mouse_position()
            print(f"Mouse : {mouse_pos.x} , {mouse_pos.y}")
            final.on_click(mouse_pos)

        rl.end_drawing()
if __name__ == "__main__":
    main()
    gc.collect()
