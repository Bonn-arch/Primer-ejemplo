'''
Un objeto es una "instancia" de una clase. Una clase es simplemente una plantilla para crear objetos, que son copias individuales de la clase con valores reales.

En el último ejercicio, creamos una clase para modelar a los estudiantes:
class Student:
  student_id = 0
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False



Usando el StudentClase, vamos a crear un objeto para modelar el icónico Wednesday Addams de Nevermore Academy – un internado para marginados e inadaptados.

La sintaxis para crear un objeto se ve así:
wednesday = Student()

Ahora que hemos creado un objeto de StudentY lo guardó para wednesday, podemos acceder y editar los atributos de clase mediante el uso de la sintaxis de puntos, .attribute:
wednesday.student_id = 1113
wednesday.name = 'Wednesday Addams'
wednesday.year = 11
wednesday.gpa = 4.0
wednesday.enrolled = True
'''
'''
En el último ejercicio, hemos creado una RestaurantClase.

En un nuevo archivo llamado bobs_burgers.py, crea una instancia de la RestaurantClase llamada bobs_burgersCon los siguientes atributos:

    'Bob\'s Burgers'
    'American Diner'
    4.7
    False

Una vez que lo hagas, crea dos instancias más de la RestaurantClase con tus lugares favoritos para cenar cerca.

Entonces, usa print(vars())¡Para producir cada uno de los tres restaurantes!
'''
class Restaurant:
    name = str
    category = str
    rating = float
    delivery = bool
bobs_burgers = Restaurant()
bobs_burgers.name = "Bob\'s Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False
print(vars(bobs_burgers))


