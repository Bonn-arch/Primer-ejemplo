import random

opciones = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]

print('*** Galleta de la Fortuna ***')
print('Tu fortuna es:')
def fortuna():
    fortuna = random.randint(0, 8)
    if fortuna == 0:
        option = opciones[0]
    elif fortuna == 1:
        option = opciones[1]  
    elif fortuna == 2:
        option = opciones[2]
    elif fortuna == 3:
        option = opciones[3]
    elif fortuna == 4:
        option = opciones[4]
    elif fortuna == 5:
        option = opciones[5]
    elif fortuna == 6:
        option = opciones[6]
    elif fortuna == 7:
        option = opciones[7]
    elif fortuna == 8:
        option = opciones[8]
    else:
        option = 'Error'
    print(option)
    
fortuna()
fortuna()
fortuna()