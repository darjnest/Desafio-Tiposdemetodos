class Personaje:
    def __init__(self, nombre):
        """
        Constructor de la clase Personaje.
        Inicializa el nombre del personaje, su nivel (1) y su experiencia (0).
        """
        self.nombre = nombre
        self.nivel = 1
        self.experencia = 0

    def get_estado(self):
        """
        Getter para obtener el estado del personaje.
        Retorna un string con el nombre, nivel y experiencia del personaje.
        """
        return (
            f"NOMBRE: {self.nombre} \t NIVEL: {self.nivel} \t EXP: {self.experiencia}"
        )

    def set_estado(self, experencia):
        """
        Setter para asignar experiencia al personaje y actualizar su nivel.
        La experiencia puede ser positiva o negativa.
        Cada 100 puntos de experiencia, el nivel sube. Si la experiencia total es negativa, el nivel baja.
        """
        experencia_total = self.experencia + experencia

        # Aumenta el nivel por cada 100 puntos de experiencia positiva
        while experencia_total >= 100:
            experencia_total -= 100
            self.nivel += 1

        # Reduce el nivel si la experiencia total es negativa y el nivel es mayor a 1
        while experencia_total < 0 and self.nivel > 1:
            experencia_total += 100
            self.nivel -= 1

        # Si el personaje esta en el nivel 1 y la experencia es negativa
        if self.nivel == 1 and experencia_total < 0:
            experencia_total = 0

        # Asigna la experencia final
        self.experencia = experencia_total

    def __lt__(self, otro):
        """
        Sobrecarga del operador menor que (<).
        Compara dos personajes según su nivel.
        """
        return self.nivel < otro.nivel

    def __gt__(self, otro):
        """
        Sobrecarga del operador mayor que (>).
        Compara dos personajes según su nivel.
        """
        return self.nivel > otro.nivel

    def __eq__(self, otro):
        """
        Sobrecarga del operador igual que (==).
        Compara dos personajes según su nivel.
        """
        return self.nivel == otro.nivel

    def probabilidad_ganar(self, otro):
        """
        Método que calcula la probabilidad de ganar de la instancia actual contra otro personaje.
        Retorna un valor entre 0.33 y 0.66 basado en la comparación de niveles.
        """
        if self > otro:
            return 0.66
        elif self < otro:
            return 0.33
        else:
            return 0.5

    @staticmethod
    def opcion_enfrentamiento(probabilidad):
        """
        Método estático que muestra el diálogo de enfrentamiento con el orco.
        Muestra la probabilidad de ganar y solicita al jugador que elija entre atacar o huir.
        Retorna la opción seleccionada por el jugador.
        """
        print(
            f"Con tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al Orco."
        )
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        return int(input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n"))
