import os
import socket
import sys
import threading
import pyray as rl
from cryptography.fernet import Fernet
import socket
from pyngrok import ngrok, exception
import requests
from constants import base_url

ANCHO_MOUSE = 0.5

# Para usar una clave guardada
with open("../security/clave.key", "rb") as key_file:
    clave = key_file.read()

# Crear un objeto Fernet con la clave
cipher_suite = Fernet(clave)

class Inicio:

    def __init__(self, ancho, alto, imagen_ruta):
        self._textura = rl.load_texture(imagen_ruta)
        if (self._textura.id == 0):
            rl.trace_log(rl.TraceLogLevel.LOG_WARNING,
                         f"failed to load texture from {imagen_ruta}")
            exit()

        print("Imagen Ruta: " + imagen_ruta)

        self._fondo = rl.Rectangle(0, 0, ancho, alto)

        self._titulo = rl.Rectangle(((ancho-(ancho/2))/2),((alto-(alto/6))/20),(ancho/2),(alto/4))

        self._crear_partida = rl.Rectangle((ancho / 4) - 10, alto / 3,
                                           ancho / 4, alto / 6)

        self._unirse_partida = rl.Rectangle((ancho / 2) + 10, alto / 3,
                                            ancho / 4, alto / 6)
        self._visible = 1
        self._socket = None
        self._creador = None

    def dibujar(self):
        try:
            self.dibujar_fondo()

            self.dibujar_titulo()

            self.dibujar_boton_iniciar_partida()

            self.dibujar_boton_unirse_a_partida()
        except ZeroDivisionError:
            print("ERROR DE TEXTURA")
            exit()


    def dibujar_titulo(self):
        TAM_FONT_TITULO = 70
        rl.draw_rectangle_rec(self._titulo,rl.YELLOW)
        texto_titulo = "Quien so vo?"
        tt_measure = rl.measure_text_ex(rl.get_font_default(),texto_titulo,TAM_FONT_TITULO,0.0)
        rl.draw_text(texto_titulo, int(self._titulo.x + self._titulo.width/2 - (tt_measure.x/2)),
                         int(self._titulo.y+self._titulo.height/2-(tt_measure.y/2)),TAM_FONT_TITULO,rl.BLACK)

    def dibujar_fondo(self):
        escala_ancho = self._fondo.width / self._textura.width
        rl.draw_texture_ex(self._textura, (self._fondo.x, self._fondo.y),
                               0.0, escala_ancho, rl.WHITE)

    def dibujar_boton_unirse_a_partida(self):
        TAM_FONT_UAP=40
        text_unirse_partida = "Unirse a Partida"
        tup_measure = rl.measure_text_ex(rl.get_font_default(),text_unirse_partida,TAM_FONT_UAP,0.0)
        rl.draw_rectangle_rec(self._unirse_partida, rl.BLUE)
        rl.draw_text(text_unirse_partida, int(self._unirse_partida.x + self._unirse_partida.width/2 - (tup_measure.x/2)),
                         int(self._unirse_partida.y + self._unirse_partida.height/2 - (tup_measure.y/2)), TAM_FONT_UAP, rl.WHITE)

    def dibujar_boton_iniciar_partida(self):
        TAM_FONT_IAP=40
        rl.draw_rectangle_rec(self._crear_partida, rl.RED)
        text_crear_partida = "Crear Partida"
        tcp_measure = rl.measure_text_ex(rl.get_font_default(),text_crear_partida,TAM_FONT_IAP,0.0)
        rl.draw_text(text_crear_partida, int(self._crear_partida.x + self._crear_partida.width/2 - (tcp_measure.x/2)),
                         int(self._crear_partida.y + self._crear_partida.height/2 - (tcp_measure.y/2)), TAM_FONT_IAP, rl.WHITE)

    def on_click(self, punto) -> bool:

        if rl.check_collision_point_rec(punto,self._crear_partida):
            try:
                hilo = threading.Thread(target=self.crear_partida)
                hilo.start()
                hilo.join()
                self._creador = True
                self._visible = 0
            except exception.PyngrokNgrokError:
                sys.exit()
        elif rl.check_collision_point_rec(punto,self._unirse_partida):
            codigo = input("Ingresar codigo: ")
            tries = 0
            while(self._socket == None and tries < 6):
                hilo = threading.Thread(target=self.unirse_partida, args=(codigo,))
                hilo.start()
                hilo.join()
                tries+=1
            if (self._socket == None):
                sys.exit()
            self._creador = False
            self._visible = 0 

        return rl.check_collision_point_rec(punto,self._fondo)

    def get_visible(self):
        return self._visible == 1
    
    def get_socket(self):
        return self._socket,self._creador
    
    def __del__(self):
        rl.unload_texture(self._textura)
    
    def cifrar_datos(self,datos):
        datos_bytes = datos.encode('utf-8') 
        return cipher_suite.encrypt(datos_bytes).decode()
    
    def descifrar_datos(self,datos):
        datos_bytes = cipher_suite.decrypt(datos.encode())  
        return datos_bytes.decode('utf-8') 

    def add_text_api(self,puerto_encriptado):
        url = f"{base_url}/add/"
        payload = {
            "text": puerto_encriptado
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error al agregar el texto:", response.status_code, response.json())
            exit()

    def crear_partida(self) -> socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 0))  # Bind a cualquier puerto disponible
        server_socket.listen(1)
        puerto = server_socket.getsockname()[1]

        # Inicia un túnel ngrok para el puerto del servidor
        url_tunel = ngrok.connect(puerto, "tcp")
        url_cifrada = self.cifrar_datos(url_tunel.public_url)
        response_api = self.add_text_api(url_cifrada)
        print(f"Partida creada. codigo de sala: {response_api}")
        print(f"Esperando conexión en el puerto: {puerto}")

        conn, addr = server_socket.accept()
        print(f"Conectado con {addr}")
        print(f"socket: {conn}")

        self._socket = conn
    
    def get_text_api(self,codigo_sala):
        url = f"{base_url}/get/{codigo_sala}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error al obtener el texto:", response.status_code, response.json())
            exit()


    def unirse_partida(self,code):
        # Obtiene la IP y el puerto del URL de ngrok
        
        url_ngrok = self.get_text_api(code)
        url_ngrok = url_ngrok["text"]
        print(f"\n\nURL NEGROK: {url_ngrok}\n\n")
        
        url_ngrok = self.descifrar_datos(url_ngrok)
        _, direccion = url_ngrok.split("//")
        ip_remota, puerto_codificado = direccion.split(":")
        puerto = int(puerto_codificado)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_remota, puerto))
        print(f"Conectado al servidor en IP: {ip_remota}, Puerto: {puerto}")
        
        self._socket = client_socket