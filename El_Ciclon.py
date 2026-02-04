altura = float(input('Ingrese su altura en metros: '))
creditos = int(input('Ingrese el número de créditos que ha completado: '))
if altura >= 1.37 and creditos >= 10:
    print('¡Disfruta el viaje!')
elif altura < 1.37 and creditos >= 10:
    print('No eres lo suficientemente alto para montar.')
elif altura >= 1.37 and creditos < 10:
    print('No tienes suficientes créditos.')
if not altura:
    print('No cumples con los requisitos para la beca.') 