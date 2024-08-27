import random
from personaje import Personaje


def main():
    """
    Función principal que controla el flujo del juego.
    Crea al personaje del jugador y al orco, maneja el enfrentamiento entre ellos,
    y permite al jugador elegir si desea atacar o huir.
    """
    print("¡Bienvenido a Gran Fantasía!")

    # Solicita el nombre del personaje del jugador
    nombre_jugador = input("Por favor indique nombre de su personaje: ")

    # Crea los personajes del jugador y del orco
    jugador = Personaje(nombre_jugador)
    orco = Personaje("Orco")

    # Muestra el estado inicial del jugador
    print(jugador.get_estado())
    print("¡Oh no!, ¡Ha aparecido un Orco!")

    while True:
        # Calcula la probabilidad de que el jugador gane al orco
        probabilidad = jugador.probabilidad_ganar(orco)

        # Muestra el diálogo de enfrentamiento y obtiene la opción del jugador
        opcion = jugador.opcion_enfrentamiento(probabilidad)

        if opcion == 2:
            # El jugador ha decidido huir
            print("¡Has huido! El orco ha quedado atrás.")
            break
        elif opcion == 1:
            # El jugador decide atacar
            resultado = random.uniform(0, 1)  # Genera un número aleatorio entre 0 y 1
            if resultado <= probabilidad:
                # El jugador gana el enfrentamiento
                print("¡Le has ganado al orco, felicidades!")
                jugador.set_estado(50)  # El jugador gana 50 puntos de experiencia
                orco.set_estado(-30)  # El orco pierde 30 puntos de experiencia
            else:
                # El orco gana el enfrentamiento
                print("¡Oh no! ¡El orco te ha ganado!")
                jugador.set_estado(-30)  # El jugador pierde 30 puntos de experiencia
                orco.set_estado(50)  # El orco gana 50 puntos de experiencia

            # Muestra el estado actualizado de ambos personajes
            print(jugador.get_estado())
            print(orco.get_estado())


if __name__ == "__main__":
    main()
