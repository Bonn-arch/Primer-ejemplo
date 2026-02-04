"""
    La metodología de No te repitas.
    Hemos estado usando funciones integradas como print()y input()Todo el tiempo.
    Cómo definir y llamar a una función – el proceso de dos pasos.
    Entradas con parámetros y argumentos.
    Los resultados con el returnPalabra clave.
    Alcance de funciones vs. alcance global.


Aquí está el esqueleto de la función una vez más, en caso de que lo olvides!
    def function_name(parameter1, parameter2):
        # The code inside
        return value
"""

"""
Cuando te detienes a un drive-thru como McDonald's, puedes pedir comida diciendo los números de artículo.
Por ejemplo, una Happy Meal podría ser un #3!
Crea un programa drive_thru.py con el menú de tu cadena de comida rápida favorita.

Definir a get_item()La función que toma un parámetro, el número del elemento que desea ordenar, y devuelve el nombre de ese elemento!

Por ejemplo, si llamaste a la función con:

    Valor de argumento 1, podría volver '🍔 Cheeseburger'.
    Valor de argumento 2, podría volver '🍟 Fries'.
    Valor de argumento 3, podría volver '🥤 Soda'.
    Valor de argumento 4, podría volver '🍦 Ice Cream'.
    Valor de argumento 5, podría volver '🍪 Cookie'.

¡Asegúrese de llamar a esta función varias veces para asegurarse de que funcione!

Por último, hagamos lo siguiente:

    Crear un menú de bienvenida y poner eso en un welcome()Función.
    Crear un programa principal que tome la entrada del usuario con input().
"""




#mi turno
def get_item(tu_comida):
    if tu_comida ==1:
        return '🍔 Hamburguesa'
    elif tu_comida ==2:
        return '🍟 Papas fritas'
    elif tu_comida ==3:
        return '🥤 Refresco'
    elif tu_comida ==4:
        return '🍦 Helado'
    elif tu_comida ==5:
        return '🍪 Galleta'
    else:
        return 'Artículo no encontrado'

def welcome():
    print("¡Bienvenido al Drive-Thru de Comida Rápida!")
    print("Menú:")
    print("1: 🍔 Hamburguesa")
    print("2: 🍟 Papas fritas")
    print("3: 🥤 Refresco")
    print("4: 🍦 Helado")
    print("5: 🍪 Galleta")

welcome()

comida = int(input("Por favor ingresa el número del artículo que deseas ordenar: "))
print(get_item(comida))




