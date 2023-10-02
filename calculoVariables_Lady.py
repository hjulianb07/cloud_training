
#Programa calculo de Edad
edad = 29
print("Mi edad es: " + str(edad))

edadCadena = str(edad)
print ("Mi edad convertida: " + edadCadena)

print ("Digite año actual: ")
añoActual = int(input())
print ("Digite año a calcular:")
añoCalcul = int(input())
edadCalculada = (añoCalcul  - añoActual) + edad
print ("Edad Calculada al año " +str(añoCalcul) + " es : " + str(edadCalculada))

#Programa calculo de numeros Operadores Logicos

print("Digite número 1 : ")
numero1 = int(input())
print("Digite número 2 : ")
numero2 = int(input())
print ("Los números son iguales " + " número1 : "+ str(numero1) +  ", número2 : " + str(numero2))
print(numero1 == numero2)
print("Los números son diferentes " + " número1 : "+ str(numero1) +  ", número2 : " + str(numero2))
print(numero1 != numero2)
print("El número1: " + str(numero1) + ", es mayor que el número2: " + str(numero2) )
print(numero1 > numero2)
print("el número2: " + str(numero2) + ", es mayor que el número1: " + str(numero1) )
print(numero1 < numero2)
