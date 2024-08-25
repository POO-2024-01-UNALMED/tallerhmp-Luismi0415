class Deportista:
    def __init__(self, deporte, añosPracticando):
        self.__deporte = deporte               # Atributo privado
        self.__añosPracticando = añosPracticando  # Atributo privado

    # Métodos get para obtener los valores de los atributos
    def get_deporte(self):
        return self.__deporte
    
    def get_añosPracticando(self):
        return self.__añosPracticando
    
    # Métodos set para dar valores a los atributos
    def set_deporte(self, deporte):
        self.__deporte = deporte
    
    def set_añosPracticando(self, añosPracticando):
        self.__añosPracticando = añosPracticando