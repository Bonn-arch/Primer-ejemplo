'''
Objeto de ciudad 
'''
class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
New_York = City("New York", "USA", 8419600, ["Statue of Liberty", "Central Park", "Times Square"]) 
print(vars(New_York)) 
