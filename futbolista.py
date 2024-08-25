class Futbolista(Persona, Deportista):
    listaFutbolistas = []  # Atributo de clase para almacenar todos los futbolistas

    def __init__(self, nombre, edad, altura, sexo, deporte, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        # Inicialización de atributos de la clase base Persona
        Persona.__init__(self, nombre, edad, altura, sexo)
        # Inicialización de atributos de la clase base Deportista
        Deportista.__init__(self, deporte, añosPracticando)
        # Inicialización de atributos propios de Futbolista
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil
        # Agregar el futbolista a la lista de futbolistas
        Futbolista.listaFutbolistas.append(self)

    # Métodos get
    def get_golesMarcados(self):
        return self.__golesMarcados
    
    def get_tarjetasRojas(self):
        return self.__tarjetasRojas
    
    def get_piernaHabil(self):
        return self.__piernaHabil
    
    # Métodos set
    def set_golesMarcados(self, golesMarcados):
        self.__golesMarcados = golesMarcados
    
    def set_tarjetasRojas(self, tarjetasRojas):
        self.__tarjetasRojas = tarjetasRojas
    
    def set_piernaHabil(self, piernaHabil):
        self.__piernaHabil = piernaHabil

    # Método __str__ para representar al objeto como cadena
    def __str__(self):
        return (f"Mi nombre es {self.get_nombre()}, soy profesional en el deporte {self.get_deporte()}. "
                f"Tengo {self.get_edad()} años de edad y llevo {self.get_añosPracticando()} años en el deporte")