# Quien so vo!

**Juego argentino de "Quién es Quién" versión online.**

Para que te diviertas con tus amigos adivinando qué personaje argentino eres.

## Descripción del Proyecto

Esta solución de software recrea el famoso juego "¿Quien es Quien?", con la diferencia de que se incluyen únicamente figuras argentinas. Este juego consta de dos jugadores, quienes se comunicarán entre sí haciéndose preguntas que los guíen a adivinar qué personaje le fue asignado a su contrincante, de manera que gana quien lo acierte primero.

## Características

- **Dos jugadores**: Cada jugador intenta adivinar el personaje asignado a su contrincante.
- **Figuras argentinas**: Personajes célebres de Argentina.
- **Comunicación en tiempo real**: Los jugadores se comunican a través de preguntas y respuestas.
- **Seguridad**: Uso de criptografía para asegurar la URL pública del túnel ngrok.

## Tecnologías Utilizadas

Para llevar a cabo dicho software, se utilizó el lenguaje de programación Python y las siguientes bibliotecas:

- **pyray**: Biblioteca de Python que proporciona bindings para raylib, una librería de desarrollo de videojuegos en C.
- **pyngrok**: Facilita el uso de ngrok, que es una herramienta que permite crear un túnel seguro desde una máquina local a Internet.
- **cryptography.fernet**: Parte de la biblioteca cryptography, proporciona herramientas de criptografía, como cifrado y descifrado de datos.
- **requests**: Biblioteca que facilita las solicitudes HTTP, permitiendo interactuar con servicios web de manera sencilla.

## Funcionamiento del Juego

Uno de los jugadores hará de servidor y el otro de cliente. Cada uno empleará un hilo para evaluar si es su turno o no, llevando a cabo la correspondiente comunicación entre ellos mediante el uso de sockets.

# Diagrama
![image](https://github.com/Martin-Roberto-lecuona/Quien-so-vo/assets/49318876/09e1534d-5255-4447-a54e-af82badde21e)

