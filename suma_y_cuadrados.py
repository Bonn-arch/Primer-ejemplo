numero = int(input("Ingrese un número: "))
suma = 0
for i in range(1, numero + 1):
    suma = i * i + suma
print (suma)


#Version Gemini

number = int(input("Please enter an integer: "))
total = 0
for i in range(1, number + 1):
    square = i ** 2
    total = total + square
print(total)