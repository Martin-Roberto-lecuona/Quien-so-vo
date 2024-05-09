#include <raylib.h>
#include <iostream>
#define ANCHO_MOUSE 0.5f

class Inicio {
public:
    Inicio(int ancho, int alto, const char* imagenRuta) {
        textura = LoadTexture(imagenRuta);
        if (textura.id == 0) {
            TraceLog(LOG_WARNING, "Failed to load texture from %s", imagenRuta);
        }
        std::cout<<"imagenRuta: "<<imagenRuta<<std::endl;
        fondo.x = 0;
        fondo.y = 0;
        fondo.height = alto;
        fondo.width = ancho;

        crearPartida.x = (ancho / 4) -10; 
        crearPartida.y = alto / 3; 
        crearPartida.width = ancho / 4; 
        crearPartida.height = alto / 6; 

        unirsePartida.x = (ancho / 2) +10 ; 
        unirsePartida.y = alto / 3; 
        unirsePartida.width = ancho / 4; 
        unirsePartida.height = alto / 6;

        visible = 1;
    }

    void dibujar() const {
        // Dibuja el fondo
        float escalaAncho = fondo.width / textura.width;
        DrawTextureEx(textura, { fondo.x, fondo.y }, 0.0f, escalaAncho, WHITE);

        // Dibuja el botón para crear partida
        DrawRectangleRec(crearPartida, RED); // Dibuja el rectángulo en rojo
        DrawText("Crear Partida", crearPartida.x + 10, crearPartida.y + 10, 20, WHITE);

        // Dibuja el botón para unirse a partida
        DrawRectangleRec(unirsePartida, BLUE); // Dibuja el rectángulo en azul
        DrawText("Unirse a Partida", unirsePartida.x + 10, unirsePartida.y + 10, 20, WHITE);
    }

    bool onClick(Vector2 punto) {
        Rectangle mouse = {
            (float)punto.x,
            (float)punto.y,
            ANCHO_MOUSE,
            ANCHO_MOUSE
        };

        if (CheckCollisionRecs(mouse, crearPartida)) {
            std::cout << "Ejecutar Servidor" << std::endl;
            visible = 0;
        } else if (CheckCollisionRecs(mouse, unirsePartida)) {
            std::cout << "Ejecutar Cliente" << std::endl;
            visible = 0;
        }

        return CheckCollisionRecs(mouse, fondo);
    }

    bool getVisible() const {
        return visible == 1;
    }

private:
    Rectangle fondo;
    Rectangle crearPartida;
    Rectangle unirsePartida;
    int visible;
    Texture2D textura;
};
