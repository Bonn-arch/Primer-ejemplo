i = 0

while i < 6:
  j = 0
  while j < 6:
    print(i * j)
    j = j + 1
  i = i + 1



import random

lucky_number = random.randint(1, 9)
not_found = True

while not_found:
  for i in range(1, 10):
    if i == lucky_number:
      not_found = False
      break
    else:
      print(i)

print(f"Yay I got my lucky number {lucky_number}! 🍀")