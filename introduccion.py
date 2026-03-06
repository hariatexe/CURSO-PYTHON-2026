# # nombre = input("Introduce tu nombre: ")
# # print(type(nombre))


# # Operaciones Elementales

# numero_1 = 40
# numero_2 = 20
# # numero_3 = 10

# # numero_1 += numero_2 # 40 + 20 = 60 (Lo guardo en la variable numero 1)
# # numero_3 += numero_1 # 10 + 60 = 70 (Lo almaceno en la variable numero 3)

# numero_1 *= numero_2


# print("Resultado de la suma: ", numero_1)



# CONDICIONALES

# valor = -200
# if valor == 10:
#     #ejecuto
#     print("Es igual a 10")
# elif valor > 0:
#     print("Es positivo")
# else:
#     print("Es negativo")


## == (Compara si dos elementos son iguales) Si lo son devuelve True
## != (Compara si dos elementos son diferentes) Si lo son devuelve True
## (condicion1) and (condicion2), si condicion1 = True y la condicion2 = True, entonces es True
## (condicion1) or (condicion2), si condicion1 = True o si la condicion2 = True, entonces es True

# nombre_1 = input("Introduce tu nombre: ")
# nombre_2 = input("Introduce tu nombre: ")
# if nombre_1 == nombre_2:
#     print("Los nombres son iguales")
# else:
#     print("Los nombres son diferentes")




# Bucles

# for, while

# for i in range(2,10,2):
#     print(i)

# lista = [10,20,30,40]

# for i in range(len(lista)):
#     print(lista[i])

# for i in lista:
#     if i > 10:
#         print(i)

# for index, value in enumerate(lista):
#     print(index, value)


numero = 10
while numero > 0:
    numero -= 1
    print(numero)
