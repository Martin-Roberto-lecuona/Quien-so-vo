import os
from typing import Any
import pyray as rl
import threading
import socket
from pyngrok import ngrok
from cryptography.fernet import Fernet
import requests
from constants import base_url
import re

FONT_SIZE = 17
PADDING_X = 5
PADDING_Y = 8
MAX_LINEAS = 3
banReceive = False
maxMensajes = 5 
cantMensajes = 0
alive_thread = True
class ChatHistory:
    def manejar_conexion(self,conn):
        global banReceive
        global maxMensajes
        global cantMensajes
        global alive_thread
        while alive_thread:
            if self._mi_turno:
                if banReceive:
                    mensaje = self._linea
                    match_ganaste = re.match(r'^/ganaste$', mensaje)
                    match_perdiste = re.match(r'^/perdiste$', mensaje)
                    self._socket.sendall(mensaje.encode())
                    if (match_ganaste or match_perdiste):
                        self._socket.close()
                        break
                    self._mi_turno = False
                    banReceive = False
            else: 
                if cantMensajes >= maxMensajes:
                    self._text = ""
                    cantMensajes = 0  
                try:
                    datos = self._socket.recv(1024)
                    if not datos:
                        break
                    mensaje_recibido = str(datos.decode())
                    print("mensaje_recibido" + mensaje_recibido)
                    match_adivinar = re.match(r'^/adivinar (\d+)$', mensaje_recibido)
                    match_ganaste = re.match(r'^/ganaste$', mensaje_recibido)
                    match_perdiste = re.match(r'^/perdiste$', mensaje_recibido)
                    if match_adivinar:
                        self._adivinado = int(match_adivinar.group(1))
                    elif match_ganaste or match_perdiste:
                        self._win_response = mensaje_recibido[1:]
                        print(f"mensaje_recibido en ganaste o perdiste |{self._win_response}|" )
                        self._socket.close()
                        break
                    else:
                        self._text = self._text + "Oponente: " + mensaje_recibido + "\n"
                        cantMensajes += 1
                    
                    self._mi_turno = True
                except socket.timeout:
                    print(f"en cathc {alive_thread}")
                    continue



    def __init__(self, x, y, ancho, alto, text="", el_socket: Any = None , creador: Any = None) -> None:
        self._campo = rl.Rectangle(x, y, ancho, alto)

        self._text = text
        self._linea = ""
        self._adivinado = -1
        self._win_response = None

        self._tam_linea = 0
        self._cant_lineas = 0
        self._mi_turno = creador
        self._socket = el_socket
        self._socket.settimeout(2.0)
        print(f"socket en chat history {self._socket}")
        self._hilo_lectura = threading.Thread(target=self.manejar_conexion, args=(self._socket,))
        self._hilo_lectura.start()

    def __del__(self):
        global alive_thread
        alive_thread = False
        print(f"en DELETE{alive_thread}")
        self._hilo_lectura.join()

    def dibujar(self):
        color_modificado = rl.Color(0, 0, 0, 255)
        color_modificado.a = int(0.5 * 255)
        rl.draw_rectangle_rec(self._campo, color_modificado)
        rl.draw_text(self._text, int(self._campo.x + PADDING_X),
                     int(self._campo.y + PADDING_Y), FONT_SIZE, rl.WHITE)
    
    def recive_data_input(self, text):
        global banReceive
        self._linea = text

        # Dividir el texto en segmentos de 15 caracteres
        self._linea = ''
        while len(text) > 15:
            self._linea += text[:15] + '\n'
            text = text[15:]
        self._linea += text  # Añadir el resto del texto

        self._text += "Tu: " + self._linea + "\n"
        banReceive = True
    
    def recive_command(self, text):
        global banReceive
        self._linea = "/" + str(text)
        banReceive = True
        
    def recive_data_socket(self):
        # esperar lectura socket 
        while(not rl.window_should_close()):
            if (not self._mi_turno):
                text = self.leer_socket()
                self._text =self._text + "Oponente: " + text + "\n"
                self._mi_turno = True
    
    def es_mi_turno(self):
        return self._mi_turno
    
    def leer_socket(self):
        datos = self._socket.recv(1024)
        if not datos:
            return
        print(f"Turno del oponente: {datos.decode()}")
        self._mi_turno = True
    def get_personaje_adivinado(self):
        return self._adivinado
    def get_win_response(self):
        return self._win_response