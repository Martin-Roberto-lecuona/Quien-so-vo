#include <raylib.h>
#include <iostream>
#define ANCHO_MOUSE 0.5f
class Personaje {
    public:
        Personaje(int x, int y, int ancho, int alto, const char* imagenRuta): opacidad(1.0f) 
        {
            textura = LoadTexture(imagenRuta);
            if (textura.id == 0) 
                TraceLog(LOG_WARNING, "Failed to load texture from %s", imagenRuta);

            rectangulo.x=x;
            rectangulo.y=y;
            rectangulo.height=alto;
            rectangulo.width=ancho;
        }
        Personaje(): opacidad(1.0f) { }

        ~Personaje() 
        {
            UnloadTexture(textura);
        }

        void dibujar() const 
        {
            Color colorModificado = WHITE; 
            colorModificado.a = (unsigned char)(opacidad * 255); 

            float escalaAncho = rectangulo.width / textura.width;

            DrawTextureEx(textura, { rectangulo.x, rectangulo.y }, 0.0f, escalaAncho, colorModificado);
        }

         void ajustarOpacidad() {
            opacidad = (opacidad == 1.0f) ? 0.4f : 1.0f;
        }

        bool onClick(Vector2 punto) const {
            Rectangle mouse = {
                (float)punto.x,
                (float)punto.y,
                ANCHO_MOUSE,
                ANCHO_MOUSE
            };
            if(CheckCollisionRecs(mouse, this->rectangulo))
                std::cout << "PJ :"<< this->rectangulo.x << ", " << this->rectangulo.y << std::endl;
            return CheckCollisionRecs(mouse, this->rectangulo);
        }

    private:
        Rectangle rectangulo;
        Texture2D textura;
        float opacidad;
};
