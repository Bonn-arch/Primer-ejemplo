

#Mismo problema resuelto con while pero con limite a 5
adivina = 0
intentos = 0

while adivina!= 6 and intentos < 5:
  adivina = int(input('Adivina el número: '))
intentos = intentos + 1
if adivina == 6:
  print('Felicidades, adivinaste el número!')  
