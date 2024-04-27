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
