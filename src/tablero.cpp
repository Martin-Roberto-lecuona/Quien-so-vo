#include <raylib.h>
#include "personaje.cpp" 
#define FILAS 3
#define COLUMNAS 5
#define PADDING 15
class Tablero 
{
    public:
        Tablero() 
        {
            int anchoCelda = 150;
            int altoCelda = 250;
            const char* imagenRuta = "./img/Ricardo-Fort.png";

            for (int i = 0; i < FILAS; i++) {
                for (int j = 0; j < COLUMNAS; j++) {
                    int posX = (j+1) * (anchoCelda + PADDING) - anchoCelda ;
                    int posY = i * altoCelda;
                    
                    personajes[i][j] = Personaje(posX, posY, anchoCelda, altoCelda, imagenRuta);
                }
            }
        }

        void dibujar() {
            for (int i = 0; i < FILAS; i++) { 
                for (int j = 0; j < COLUMNAS; j++) { 
                    personajes[i][j].dibujar(); 
                }
            } 
        }

        // hacer esto con hilos para que cada fila sea un hilo. Deberia tardar menos
        void onClick(Vector2 mousePos) {
            for (int i = 0; i < FILAS; i++) {
                for (int j = 0; j < COLUMNAS; j++) {
                    if (personajes[i][j].onClick(mousePos)) {
                        personajes[i][j].ajustarOpacidad(); 
                    }
                }
            }
        }

    private:
        Personaje personajes[FILAS][COLUMNAS]; 
};
