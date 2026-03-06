# EJERCICIOS VARIABLES:

# 1. Pedir al usuario dos números y mostrar la suma, resta, multiplicación y división.
# 2. Pedir el nombre del usuario y salúdalo con "Hola, {nombre}".
# 3. Implementar un código que verifique si el input introducido es un booleano.
"""
variable = input("Introduce un valor: ")
if variable.lower() == "true" or variable.lower() == "false":
    print("Es un valor booleano")
else:
    print("No es un valor booleano")
"""

#=================================================================================================#

# EJERCICIOS CONDICIONALES:

# 1. Pedir un número y determinar si es positivo, negativo o cero.
"""
numero = int(input("Introduce un numero: "))
if numero > 0:
    print("Es positivo")
elif numero == 0:
    print("Es igual a 0")
else:
    print("Es negativo")
"""
# 2. Calcular la nota de un estudiante (0-100) y mostrar la letra correspondiente.
# A (>= 90), B (>= 80), C (>= 70), F (< 70)
# 3. Pedir al usuario dos números y mostrar cuál es mayor o si son iguales.
# 4. Implementar un Switch.

"""
def opcion1():
    return "Seleccionaste la funcion 1"
def opcion2():
    return "Seleccionaste la funcion 2"
def opcion3():
    return "Seleccionaste la funcion 3"
switch = {
    1: opcion1,
    2: opcion2,
    3: opcion3
}

opcion = int(input("Introduce una clave: "))
print(switch.get(opcion, lambda: "Opcion Invalida")())
"""

#=================================================================================================#

# EJERCICIOS BUCLES:]

# 1. Imprimir los números del 1 al 20 usando for.
# 2. Imprimir los numeros pares del 2 al 50
# 3. Sumar todos los numeros de una lista usando for.
"""
lista = [10,20,30]
acumulador = 0
for i in lista:
    acumulador += i
print(acumulador)


# 4. Pedir números al usuario hasta que escriba 0, y muestra la suma suma total (while).
numero = int(input("Introduce un numero (0 para salir): "))
acumulador = 0
while numero != 0:
    acumulador += numero
    numero = int(input("Introduce un numero (0 para salir): "))
print(acumulador)
# 5. Usar enumerate() en una lista de nombres y mostrar indice + nombre.
"""

#=================================================================================================#
