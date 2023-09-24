def multi(num1,num2):
    return num1*num2
print('Escriba numero1: ')
num1 = int(input()) #no poner espacios entre valores porque puede generar error
print('Escriba numero2: ')
num2 = int(input())

print ('multiplicación 3')

operacion = input()

if operacion =='3':
    print(num1,'*',num2,'=',multi(num1,num2))