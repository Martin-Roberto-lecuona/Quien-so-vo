import pyray as rl
from chatHistory import ChatHistory
FONT_SIZE = 17
PADDING_X = 5
PADDING_Y = 8
MAX_LINEAS = 3


class InputField:

    def __init__(self, x, y, ancho, alto, chat_history , text="" ) -> None:
        self._campo = rl.Rectangle(x, y, ancho, alto)

        self._text = text

        self._tam_linea = 0
        self._cant_lineas = 0
        
        self._chat_history = chat_history

    def process_input(self):
        key = rl.get_key_pressed()
        if self._cant_lineas >= MAX_LINEAS:
            if key == rl.KeyboardKey.KEY_ENTER:
                self.send_text()
            return
        while key > 0:
            if key == rl.KeyboardKey.KEY_BACKSPACE:
                if self._text:
                    self._text = self._text[:-1]
                    self._tam_linea = self._tam_linea - 1 if self._tam_linea > 0 else 0
            elif key == rl.KeyboardKey.KEY_ENTER:
                self.send_text()
            else:
                self._text += chr(key)
                self._tam_linea += 1
            key = rl.get_key_pressed()

    def dibujar(self):
        color_modificado = rl.Color(0, 0, 0, 255)
        color_modificado.a = int(0.5 * 255)
        rl.draw_rectangle_rec(self._campo, color_modificado)
        rl.draw_text(self._text, int(self._campo.x + PADDING_X),
                     int(self._campo.y + PADDING_Y), FONT_SIZE, rl.WHITE)

    def dibujar_con_crlf(self, crlf):
        self._cant_lineas += 1
        if self._cant_lineas <= MAX_LINEAS:
            self._text += '\n'
            self.dibujar()

    def overflow(self) -> bool:
        if self._tam_linea > self._campo.width / FONT_SIZE + FONT_SIZE - PADDING_X:
            self._tam_linea = 0
            return True

        return False

    def borrar_campo(self):
        self._text = ""
        self._tam_linea = 0
        self._cant_lineas = 0

    def send_text(self):
        if (self._chat_history.es_mi_turno()):
            self._chat_history.recive_data_input(self._text)
            self.borrar_campo()
