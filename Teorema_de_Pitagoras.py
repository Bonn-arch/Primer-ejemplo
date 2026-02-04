#Entrada de datos del usuario
print('*** Entrada de datos del usuario ***')
nombre_de_usuario = input('Ingrese su nombre: ')
print(nombre_de_usuario)
print()
#Entrda de int 
edad = int(input('Ingrese su edad: '))
print(f'La edad ingresada es: {edad}')
print()
#Aplicar el teorema de Pitágoras
print('*** Aplicar el teorema de Pitágoras ***')

opuesto = float(input('Ingrese el valor del cateto opuesto: '))
adyacente = float(input('Ingrese el valor del cateto adyacente: '))
hipotenusa = (opuesto ** 2 + adyacente ** 2) ** 0.5
print(f'La hipotenusa es: {hipotenusa}')

