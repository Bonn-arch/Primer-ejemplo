
print()
#Sombre seleccionador de la Escuela de Brujería y Hechicería de Hogwarts
print('*** Sombrero seleccionador de la Escuela de Brujería y Hechicería de Hogwarts ***')
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('Responde las siguientes preguntas para determinar tu casa:')
respuesta1 = int(input('¿Te gusta el amanecer o el anochecer? (1 para amanecer, 2 para anochecer): '))
if respuesta1 == 1: 
    gryffindor += 1
    ravenclaw += 1
else:
    slytherin += 1
    hufflepuff += 1
respuesta2 = int(input('Cuando esté muerto, quiero que la gente me recuerde como El bueno, el grande, el sabio o el audaz (1 para bueno, 2 para grande, 3 para sabio, 4 para audaz): '))
if respuesta2 == 1:
    hufflepuff += 2
elif respuesta2 == 2:
    slytherin += 2      
elif respuesta2 == 3:
    ravenclaw += 2
elif respuesta2 == 4:
    gryffindor += 2
else:
    print('Entrada incorrecta.')
respuesta3 = int(input('¿Qué tipo de instrumento te agrada más a tu oído, el violín, la trompeta, el piano o el tambor? (1 para violín, 2 para trompeta, 3 para piano, 4 para tambor): '))
if respuesta3 == 1:
    slytherin += 4
elif respuesta3 == 2:
    hufflepuff += 4
elif respuesta3 == 3:
    ravenclaw += 4
elif respuesta3 == 4:
    gryffindor += 4
else:
    print('Entrada incorrecta.')
print('Resultados:')
if gryffindor > hufflepuff and gryffindor > ravenclaw and gryffindor > slytherin:
    print('🦁 Gryffindor')
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print('🦡 Hufflepuff')
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print('🦅 Ravenclaw')
elif slytherin > gryffindor and slytherin > hufflepuff and slytherin > ravenclaw:
    print('🐍 Slytherin')