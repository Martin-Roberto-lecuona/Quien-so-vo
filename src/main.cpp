#include <raylib.h>
#include <iostream>
#include "tablero.cpp"

int main() {
    const int screenWidth = 1000;
    const int screenHeight = 900;

    InitWindow(screenWidth, screenHeight, "Quien so vo?");
    SetTargetFPS(60);

    Tablero tablero;

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(DARKGREEN); 

        tablero.dibujar();

        if (IsMouseButtonPressed(MOUSE_LEFT_BUTTON)) {
            Vector2 mousePos = GetMousePosition();
            std::cout << "MOUSE :"<< mousePos.x << ", " << mousePos.y << std::endl;
            tablero.onClick(mousePos);
        }

        EndDrawing();
    }

    CloseWindow(); 

    return 0;
}
