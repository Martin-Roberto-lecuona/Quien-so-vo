#include <raylib.h>
#include <iostream>
#include "tablero.cpp"
#include "input.cpp"
#include "inicio.cpp"

int main() {
    const int screenWidth = 1000;
    const int screenHeight = 900;

    InitWindow(screenWidth, screenHeight, "Quien so vo?");
    SetTargetFPS(60);

    Tablero tablero;
    InputField inputField(100,800,500,60);
    Inicio inicio(screenWidth,screenHeight,"./img/fondo-inicio.png");
    
    while (inicio.getVisible() && !WindowShouldClose())
    {   
        BeginDrawing();
        ClearBackground(DARKGREEN);
        inicio.dibujar();
        if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) 
        {
            Vector2 mousePos = GetMousePosition();
            std::cout << "MOUSE :"<< mousePos.x << ", " << mousePos.y << std::endl;
            inicio.onClick(mousePos);
        }
        EndDrawing();
    }
    
    while (!WindowShouldClose()) 
    {
        BeginDrawing();
        ClearBackground(DARKGREEN); 
        inputField.processInput();

        tablero.dibujar();
        inputField.dibujar();
       
        if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) 
        {
            Vector2 mousePos = GetMousePosition();
            std::cout << "MOUSE :"<< mousePos.x << ", " << mousePos.y << std::endl;
            tablero.onClick(mousePos);
        }
        if(inputField.overflow()) 
                inputField.dibujar(1.0f);
        EndDrawing();
    }

    CloseWindow(); 

    return 0;
}
