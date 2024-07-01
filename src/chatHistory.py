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
banReceive = False
maxMensajes = 5 
cantMensajes = 0
class ChatHistory:
    def manejar_conexion(self,conn):
        global banReceive
        global maxMensajes
        global cantMensajes
        while True:
            if self._mi_turno:
                if banReceive:
                    # mandar al socket
                    mensaje = self._linea
                    self._socket.sendall(mensaje.encode())
                    # crear hilo de recibir
                    self._mi_turno = False
                    banReceive = False
            else: 
                if cantMensajes >= maxMensajes:
                    self._text = ""
                    cantMensajes = 0     
                datos = self._socket.recv(1024)
                if not datos:
                    break
                self._text = self._text + "Oponente: " + datos.decode() + "\n"
                cantMensajes+=1
                
                self._mi_turno = True



    def __init__(self, x, y, ancho, alto, text="", el_socket: Any = None , creador: Any = None) -> None:
        self._campo = rl.Rectangle(x, y, ancho, alto)

        self._text = text
        self._linea = ""

        self._tam_linea = 0
        self._cant_lineas = 0
        self._mi_turno = creador
        self._socket = el_socket
        print(f"socket en chat history {self._socket}")
        self._hilo_lectura = threading.Thread(target=self.manejar_conexion, args=(self._socket,))
        self._hilo_lectura.start()

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
        global banReceive
        self._text =self._text + "Tu: " + text + "\n"
        self._linea = text
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
    
