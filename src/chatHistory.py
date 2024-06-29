import os
from typing import Any
import pyray as rl
import threading
import socket
from pyngrok import ngrok
from cryptography.fernet import Fernet
import requests
from constants import base_url

FONT_SIZE = 17
PADDING_X = 5
PADDING_Y = 8
MAX_LINEAS = 3

class ChatHistory:
    def manejar_conexion(self,conn):
        while True:
            if self._mi_turno:
                mensaje = self._text
                conn.sendall(mensaje.encode())
                self._mi_turno = False
            else:
                datos = conn.recv(1024)
                if not datos:
                    break
                print(f"Turno del oponente: {datos.decode()}")
                self._mi_turno = True


    def __init__(self, x, y, ancho, alto, text="Historial : \n", el_socket: Any = None , creador: Any = None) -> None:
        self._campo = rl.Rectangle(x, y, ancho, alto)

        self._text = text

        self._tam_linea = 0
        self._cant_lineas = 0
        self._mi_turno = creador
        self._hilo_lectura = threading.Thread(target=self.manejar_conexion, args=(self._socket,))
        self._hilo_lectura.start()
        self._socket = el_socket

    def __del__(self):
        self._hilo_lectura.join()

    def dibujar(self):
        color_modificado = rl.Color(0, 0, 0, 255)
        color_modificado.a = int(0.5 * 255)
        rl.draw_rectangle_rec(self._campo, color_modificado)
        rl.draw_text(self._text, int(self._campo.x + PADDING_X),
                     int(self._campo.y + PADDING_Y), FONT_SIZE, rl.WHITE)
    
    def recive_data_input(self,text):
        # si puedo mandar (mi turno) entonces escribo en char
        self._text =self._text + "Tu: " + text + "\n"
        # mandar al socket
        mensaje = self._text
        self._socket.sendall(mensaje.encode())
        # crear hilo de recibir
        self._mi_turno = False
        
        
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
    
