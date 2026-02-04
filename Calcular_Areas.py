#Vamos a realizar una caluladora de areas de figuras geometricas que termita hallar el area del cuadrado, triangulo, rectangulo y circulo, o simplemente salir del programa
import math
print('*** Calculadora de Areas ***')
print('1. Area del Cuadrado')
print('2. Area del Triangulo')
print('3. Area del Rectangulo')
print('4. Area del Circulo')
print('5. Salir')
opcion = int(input('Elija una opcion (1-5): '))
if opcion == 1:
    lado = float(input('Ingrese el lado del cuadrado: '))
    lado = lado * lado
    print('El area del cuadrado es:', lado)
elif opcion == 2:
    print('Ingrese la base y la altura del triangulo:')
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    area = (base * altura) / 2
    print('El area del triangulo es:', area)
elif opcion == 3:
    print('Ingrese la base y la altura del rectangulo:')
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    area = base * altura
    print('El area del rectangulo es:', area)   
elif opcion == 4:
    print('Ingrese el radio del circulo:')
    radio = float(input('Radio: '))
    area = math.pi * (radio ** 2)
    print('El area del circulo es:', area)  
elif opcion == 5:
    print('Saliendo del programa...')
else:
    print('Opcion invalida. Por favor, elija una opcion del 1 al 5.')
    