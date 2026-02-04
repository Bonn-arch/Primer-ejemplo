#Resultado de dinero durante un viaje y transformar el resultado a dolares
print('*** Resultado de dinero durante un viaje ***')
soles = int(input('Ingrese la cantidad de soles: '))
peso_colombiano = int(input('Ingrese la cantidad de pesos colombianos: '))
reales_brasilenos = int(input('Ingrese la cantidad de reales brasileños: '))
dolares = (soles * 0.30) + (peso_colombiano * 0.00045) + (reales_brasilenos * 0.40)
print(f'El total en dólares es: {dolares}')  
