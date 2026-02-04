#Uso del elif para determinar el grado del estudiante
print('*** Uso del elif para determinar el grado del estudiante ***')
grade = int(input("Ingresa el numero de tu grado: "))
if grade > 90:
  print('A')
elif grade > 80:
  print('B')
elif grade > 70:
  print('C')
elif grade > 60:
  print('D')
else:
  print('F')

  print()
  #Vamos a calcular el pH 
print('*** Vamos a calcular el pH ***')
pH = float(input('Ingrese el valor del pH de entre 0 a 14: '))
if pH > 7.0:
    print('El pH es básico')
elif pH <= 7.0:
    print('El pH es ácido')
else:
    print('El pH es neutro')
    