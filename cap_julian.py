#esta es la funcion
def suma(num1, num2):
    return num1+num2  

def resta(num1, num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2
    
print('digita numero 1')
num1 = float(input())
print('digita numero 2')
num2 = float(input())

print('que deseas hacer')
print('1 suma')
print('2 resta')
print('3 Multiplicacion')
operacion = input()

if operacion == '1':
    print(num1, '+', num2, '=', suma(num1, num2))
elif operacion == '2':
    print(num1, '-', num2, '=', resta(num1, num2))
elif operacion == '3':
    print(num1,'*',num2,'=',multi(num1,num2))

