'''
Desde 1996, la franquicia de videojuegos Pokémon ha encantado a los jugadores de todo el mundo con monstruos de bolsillo coleccionable. Una Pokédex es un dispositivo que rastrea la información de los Pokémon que se ven o se capturan.

Crear un nuevo archivo llamado pokedex.py.

A continuación, vamos a definir un PokemonClase con los siguientes atributos:

    entry(entero)
    name(cuerda)
    types(lista de cuerdas)
    description(cuerda)
    is_caught(booleano)

Nota: Asegúrese de utilizar el __init__()Método.

A continuación, cree un método de instancia llamado .speak()Esto imprime una cadena del sonido que hace un Pokémon. Un Pokémon generalmente solo dice su nombre, así que haz el .speak()¡Simplemente imprime su nombre dos veces!

Luego, crea otro método de instancia llamado .display_details()Que imprime los atributos de un PokemonObjeto como el siguiente:

Entry Number: 25
Name: Pikachu
Type: Electric
Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
Pikachu has already been caught!

Por último, crear tres PokemonObjetos de clase y utilizar el .speak()o .display_details()Métodos de ejemplo para cada uno.

Para obtener más información sobre cualquier Pokémon que quieras agregar, consulta la Pokédex !

¿Estás listo para ganar la próxima insignia?

Bonus: Para todos los súper fans, intenta añadir más atributos a la PokemonDefinición de clase, como level, region, height, o weight.
'''
class Pokedex:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    def speak(self):
        print(f"{self.name} {self.name}!")

    def display_details(self):
        caught_status = "has already been caught!" if self.is_caught else "has not been caught yet."
        types_str = ', '.join(self.types)
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {types_str}")
        print(f"Description: {self.description}")
        print(f"{self.name} {caught_status}")
# Crear tres objetos Pokemon
pikachu = Pokedex(25, "Pikachu", ["Electric"], "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True)
charmander = Pokedex(4, "Charmander", ["Fire"], "Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.", False)
bulbasaur = Pokedex(1, "Bulbasaur", ["Grass", "Poison"], "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.", True)
# Usar los métodos de los objetos    
pikachu.speak()
pikachu.display_details()
charmander.speak()
charmander.display_details()
bulbasaur.speak()
bulbasaur.display_details()