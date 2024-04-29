#   def __init__(self):
#       es para inicializar el constructor
# se pueden crear metodos de la clase tienen que estar a la misma altura del constructor
# se le agrega por parametro el self haciendo referencia a que apunta al objeto y con el
# parametro se accede a los atributos si le pasamos None por parametro podemos crear la instancia null
#se le agrega la anotacion @property para indicar que se acceder desde ahi al getter
# para el setter @nombre.setter se agrega el atributo y .setter
class Persona:

    def __init__(self, nombre=None, apellido=None, edad=None):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def toString(self):
        print(f"se creo el objeto  {self._nombre}  + {self._apellido} + {self._edad} ")


print(type(Persona))

persona1 = Persona()
print(persona1.edad)
persona1.nombre ="juan"
persona1.apellido ="perez"
persona1.edad=28
print(persona1.edad)
persona1.toString()
# se puede agregar atributos a un objeto pero este no se comparte con los otros
persona1.telefono = "23142423"
print(persona1.telefono)
