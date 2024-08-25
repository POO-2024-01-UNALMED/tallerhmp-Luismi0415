class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad      # Atributo privado
        self.__altura = altura  # Atributo privado
        self.__sexo = sexo      # Atributo privado

    # Métodos get para obtener los valores de los atributos
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_altura(self):
        return self.__altura
    
    def get_sexo(self):
        return self.__sexo
    
    # Métodos set para dar valores a los atributos
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def set_altura(self, altura):
        self.__altura = altura
    
    def set_sexo(self, sexo):
        self.__sexo = sexo