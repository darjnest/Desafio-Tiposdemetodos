# Desafio-Tiposdemetodos

# Gran Fantasía - Desafío de Desarrollo de Juegos en Python

## Descripción

Este proyecto es parte de un desafío de desarrollo para la startup "Juegos por comida". El objetivo es crear un prototipo de la primera escena de su próximo juego "Gran Fantasía". Este prototipo se desarrolla como una aplicación de consola escrita en Python.

## Requisitos del Desafío

1. **Crear la clase `Personaje` en el archivo `personaje.py`:**

   - **Constructor:** Inicializa el nombre del personaje, su nivel (1) y su experiencia (0).
   - **Getter de estado:** Permite consultar el estado del personaje (nombre, nivel, experiencia).
   - **Setter de estado:** Asigna experiencia al personaje y actualiza su nivel en función de la experiencia total.
   - **Sobrecarga para comparar personajes:**
     - `__lt__` para comparar si un personaje es menor que otro (basado en el nivel).
     - `__gt__` para comparar si un personaje es mayor que otro (basado en el nivel).
     - `__eq__` (opcional) para comparar si dos personajes son iguales en nivel.
   - **Método para calcular la probabilidad de ganar contra otro personaje** (opcional).
   - **Método estático para mostrar el diálogo de enfrentamiento con un orco y retornar la opción del jugador** (opcional).

2. **Crear el script `juego.py` para ejecutar la escena del juego:**
   - **Flujo del juego:**
     - Dar la bienvenida al jugador y solicitar el nombre de su personaje.
     - Crear el personaje del jugador y mostrar su estado.
     - Crear un personaje "Orco" y calcular la probabilidad de ganar del jugador contra el orco.
     - Mostrar la probabilidad de ganar y preguntar al jugador si desea atacar o huir.
     - Si el jugador decide atacar, calcular el resultado del ataque y actualizar los estados de los personajes.
     - Mostrar los estados actualizados y volver a consultar al jugador.
     - Si el jugador decide huir, mostrar un mensaje indicando que el orco ha quedado atrás.

## Código

### `personaje.py`

```python
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        return f"NOMBRE: {self.nombre}\tNIVEL: {self.nivel}\tEXP: {self.experiencia}"

    def asignar_experiencia(self, exp):
        suma_exp = self.experiencia + exp

        while suma_exp >= 100:
            self.nivel += 1
            suma_exp -= 100

        while suma_exp < 0 and self.nivel > 1:
            self.nivel -= 1
            suma_exp += 100

        if suma_exp < 0:
            suma_exp = 0

        self.experiencia = suma_exp

    def __lt__(self, otro):
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        return self.nivel > otro.nivel

    def __eq__(self, otro):
        return self.nivel == otro.nivel

    def calcular_probabilidad(self, otro):
        if self > otro:
            return 0.66
        elif self < otro:
            return 0.33
        else:
            return 0.5

    @staticmethod
    def enfrentar_orco(probabilidad):
        print(f"Con tu nivel actual, tienes {probabilidad * 100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        return int(input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n"))

Ejecución del Juego

Para ejecutar el juego, simplemente corre el script juego.py desde tu terminal:

## python juego.py
## ¡Disfruta de la aventura en Gran Fantasía!
```
