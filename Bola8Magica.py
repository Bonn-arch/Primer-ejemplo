#Creacion de una programa que simule una bola 8 magica
import random
print('*** Bola 8 Mágica ***')
preguna = input('¿Cuál es tu pregunta?: ')
random_number = random.randint(1, 9)
if random_number == 1:
    print('Sí, definitivamente.')   
elif random_number == 2:
    print('Es decididamente así')   
elif random_number == 3:
    print('Sin duda.')
elif random_number == 4:
    print('Responde nebuloso, intentalo de nuevo.')
elif random_number == 5:
    print('Pregunta de nuevo más tarde.')
elif random_number == 6:
    print('Mejor no te lo digas ahora.')
elif random_number == 7:
    print('Mis fuentes dicen que no.')
elif random_number == 8:
    print('Las perspectivas no son tan buenas.')
elif random_number == 9:
    print('Muy dudoso.')






