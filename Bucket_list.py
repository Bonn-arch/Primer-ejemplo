#Cree un programa de bucket.list.py con su propia lista de cubos único.
#Primero, crear un things_to_dolista, y agrega cosas que quieres hacer en tu vida.
things_to_do = [
  '🚀 Create the dopest learn to code platform ever.',
  '⛰️ Hike the Pacific Crest Trail.',
  '🏡 Build an A-frame house and raise some goats.',
  '🌏 Live somewhere in Asia for a year.',
  '🎸 Release an album.',
  '📝 Write a book.',
  '🏆 Reach 100k subscribers on YouTube.',
  '🚐 Road trip with the fam.',
  '🍳 Open a cozy diner upstate.',
  '👴🏻 Grow old with no regrets.'
]
things_to_do.append('💻 Learn to code and help others learn too!')
things_to_do.pop(5)
things_to_do.remove('🏡 Build an A-frame house and raise some goats.')
print(things_to_do)
for i in things_to_do:
    print(i)
