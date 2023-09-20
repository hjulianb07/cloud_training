#esta es la funcion
def suma(num1, num2):
    return num1+num2  

def resta(num1, num2):
    return num1-num2

print('digita numeros')
num1 = float(input())
num2 = float(input())

print('que deseas hacer')
print('1 suma')
print('2 resta')
operacion = input()

if operacion == '1':
    print(num1, '+', num2, '=', suma(num1, num2))
elif operacion == '2':
    print(num1, '-', num2, '=', resta(num1, num2))
