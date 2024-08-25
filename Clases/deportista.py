class Deportista:
    def __init__(self, deporte, añosPracticando):
        self.__deporte = deporte
        self.__añosPracticando = añosPracticando

    # Métodos get
    def get_deporte(self):
        return self.__deporte
    
    def get_añosPracticando(self):
        return self.__añosPracticando
    
    # Métodos set
    def set_deporte(self, deporte):
        self.__deporte = deporte
    
    def set_añosPracticando(self, añosPracticando):
        self.__añosPracticando = añosPracticando