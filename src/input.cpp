#include <raylib.h>
#include <string>
#include <vector>
#include <iostream>
// #include <winsock2.h>
#define FONT_SIZE 17
#define PADDINGX 5
#define PADDINGY 8
#define MAX_LINEAS 3


/*
MEJORAR ESTA CLASE
LE FALTA MEJORAR LA FUENTE
MEJORAR TEMA DE LEER TECLAS ESPECIALES COMO ? ! #, ETC
PERMITIR USO DE FLECHAS PARA MOVERSE POR EL TEXTO
MANTENER APRETADA UNA TECLA ES COMO TOCARLA VARIAS VECES
SI MANTENGO DELETE DEBERIA BORRAR HASTA QUE DEJE DE APRETARLO
*/ 
class InputField 
{
    public:
        InputField(int x, int y, int ancho, int alto) : text("") 
        {
            campo.x=x;
            campo.y=y;
            campo.height=alto;
            campo.width=ancho;
            tamLinea=0;
            cantLineas=0;
        }

        void processInput() 
        {   
            int key = GetKeyPressed();
            if(cantLineas>=MAX_LINEAS)
            {
                if (key == KEY_ENTER) 
                {
                    // sendTextOverSocket();
                    borrarCampo();
                }
                return;
            }
            while (key > 0) 
            {
                if (key == KEY_BACKSPACE) 
                {
                    if (!text.empty()) 
                    {
                        text.pop_back(); 
                        tamLinea = tamLinea>0 ? tamLinea--  : 0 ;
                    }
                } else if (key == KEY_ENTER) 
                {
                    // sendTextOverSocket();
                    borrarCampo();
                } else 
                {
                    text += (char)key; 
                    tamLinea++;
                }
                key = GetKeyPressed(); 
            }
        }

        void dibujar() 
        {
            // Dibujar el campo de texto
            Color colorModificado = BLACK; 
            colorModificado.a = (unsigned char)(0.5 * 255); 
            DrawRectangleRec(campo, colorModificado);
            DrawText(text.c_str(), campo.x + PADDINGX, campo.y + PADDINGY , FONT_SIZE, WHITE);
        }
        void dibujar(float crlf) 
        {
            cantLineas++;
            if(cantLineas<=MAX_LINEAS)
            {
                text += '\n'; 
                dibujar();
            }

        }
        bool overflow()
        {   
            if(tamLinea > campo.width/FONT_SIZE + FONT_SIZE - PADDINGX)
            {
                tamLinea=0;
                return true;
            }
            return false;
        }
        void  borrarCampo()
        {
            text.clear(); 
            tamLinea=0;
            cantLineas=0;
        }
        void sendTextOverSocket()
        {
            text.clear(); 
        }
    private:
        Rectangle campo;
        int tamLinea;
        int cantLineas;
        std::string text;
};
