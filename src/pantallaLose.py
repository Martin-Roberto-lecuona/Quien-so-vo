import pyray  as rl
from utilities import add_path_file

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

JUEGO_NAME = "Quien so vo?"
FONT_SIZE = 40
IMAGE_BACKGROUND = add_path_file("pantallaLoser.png")
FONT_PATH = add_path_file("Roboto-Black.ttf") 

def init_window():
    rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, JUEGO_NAME)
    rl.set_target_fps(60)

def load_texture():
    image = rl.load_image(IMAGE_BACKGROUND)
    return rl.load_texture_from_image(image)

def load_font():
    return rl.load_font(FONT_PATH)

def draw_background():
    rl.clear_background(rl.RAYWHITE)
    rl.draw_rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, rl.SKYBLUE)

def draw_image(texture):
    source_rec = rl.Rectangle(0, 0, texture.width, texture.height)
    dest_rec = rl.Rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, texture.width, texture.height)
    origin = rl.Vector2(texture.width / 2, texture.height / 2)
    rotation = 0
    rl.draw_texture_pro(texture, source_rec, dest_rec, origin, rotation, rl.WHITE)

def draw_message(font):
    message1 = "Perdiste!"

    text_width1 = rl.measure_text_ex(font, message1, FONT_SIZE, 1).x
    text_height = FONT_SIZE 

    rl.draw_text_ex(font, message1, rl.Vector2((SCREEN_WIDTH - text_width1) / 2, (SCREEN_HEIGHT - text_height) / 2), FONT_SIZE, 1, rl.BLACK)

def main():
    init_window()
    texture = load_texture()
    font = load_font()

    while not rl.window_should_close():
        rl.begin_drawing()
        draw_background()
        draw_image(texture)
        draw_message(font)
        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()