# variables python no es necesario definir el tipo de dato y puede mutar el tipo de dato
# en la ejecucion del codigo
miVariable = "asddsa"
print(miVariable)
# para saber el tipo de dato
print(type(miVariable))
miVariable = "3"
print(miVariable)
# para saber el puntero en memoria
print(id(miVariable))
print(type(miVariable))
# se concatena igual que en java con + o con ,
# parseo de string a int
int(miVariable)
miVariable = 1 > 2
#estructura de if

if miVariable:
    print("true")
else:
    print("false")
    # se puede usar los operadores ternarios para el if pero solo si es algo corto
    print("true") if miVariable else print("false")

#para insertar valor por consola
#print("ingrese un valor")
#un input devuelve siempre un string asi que debemos parsear el retorno al tipo de dato que queremos
resultado = input("ingrese un valor")
float(resultado)
print(resultado)
# operadores + suma - resta  * multiplicacion /division // division entero  con / devuelve float con // deveulve un entero ** exponente % modulo
#print se usa f comillas dentro el literal y la variable entre llaves
#print con '''
print(f'''
        {resultado}
        {miVariable}    
    ''')
print(f"el resultado es: {resultado}")

# && es and  or es igual or y la negacion es not.
# se puede obviar el and interponiendo la variable a comparar entre los operadores
edad = 10
if 5 <= edad < 10:
    print("es mayor a 5 y menor a 10")
else:
    print("no esta entre 5 y 10")

boleano = True
print(not boleano)
# None es el equivalente a null en java
#estructura de while
condicion = True
while condicion:
    print("ejecutando while")
    condicion = False
else:
    print("fin")

#estructura de for se utiliza el auxiliar que va a tomar el valor y se indica de que lista itera.
cadena = "hola"

#for indice, letra in cadena:
for indice, letra in enumerate(cadena):
    print(f" indice {indice}    {letra}")
else:
    print("fin de iteracion")
#listas para acceder desde el final se usan valores negativos -1 es el ultimo -2 el penultimo y asi
nombres = ["juan", "carla", "ricardo"]

print(nombres)
print(nombres[0])
#para acceder entre el rango 0 y 1 el 2 no lo abarca
print(nombres[0:2])
#para acceder entre el rango 0 y 1 el 2 no lo abarca
print(nombres[:2])
#para saber el tamaño
print(len(nombres))
#para agregar elementos
nombres.append("jose")
#para agregar en un indice especifico los demas se mueven un indice
nombres.insert(1, "pedro")
#para remover por valor
nombres.remove("pedro")
#para remover el ultimo indice
nombres.pop()
#para eliminar por indice
del nombres[1]
#diferencia entre las tuplas y listas las listas se pueden modificar las tuplas no estas comienzan con ()
frutas = ("naranja", "banana", "manzana")
#set colection  no se modifican los elementos pero si se pueden agregar y eliminar no poseen un orden y no admite duplicados
planetas = {"marte", "jupiter", "venus"}
print(planetas)
#para verificar si existe un elemento en el set
print("marte" in planetas)
#para agregar se usa add
planetas.add("tierra")
#para eliminar
planetas.remove("tierra")  #puede lanzar error .
planetas.discard("tierra")  #si no existe no lo elimina y no lanza error.
#diccionarios  key value si se puede modificar valores y no se puede repetidos

diccionario = {
    "ide": "integrated development enviroment",
    "oop": "object oriented programming",
    "dbms": "database management system"
}

print(diccionario)
#para acceder desde la llave
print(diccionario["ide"])
print(diccionario.get("ide"))

# recorrer el diccionario solo las key

for key in diccionario:
    print(key)

    # recorrer el diccionario key y value
    for key, valor in diccionario.items():
        print(key, valor)

#funcion se define con def y se escribe con _ o con camelCase tiene que definirse antes de ejecutar.
saludo = "hola"
nombre = "augusto"


def miFuncion(saludo="hi", nombre="none"):
    print(f"{saludo} , {nombre}")


miFuncion(saludo, nombre)
miFuncion(saludo, nombre)


#funciones sin saber la cantidad de parametros *args o cualquier otro nombre pero en general es arg
def listarNombres(*args):
    for nombre in args:
        print(nombre)
    return list(nombres)
listarNombres("pedro", "pablo", "juan")
print(listarNombres("pedro", "pablo", "juan"))

#funcion con argumento de diccionario llave valor se usa **kwargs o se le puede poner cualquier nombre

def listarTerminos(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
listarTerminos(IDE="juan", PK="ASD")


# funcion con  lista

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres=["pedro","maria","jose"]
desplegarNombres(nombres)

