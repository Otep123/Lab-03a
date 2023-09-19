planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

def addPlanetPrefix(planets):
    return ['Planet ' + planet for planet in planets if planets.index(planet) % 2]

def checkPluto(L):
    return True if 'Pluto' in L else False


R = addPlanetPrefix(planets=planets)
print(R)
print(planets)
if checkPluto(planets):
    print('Pluto does not exist in this list!')
else:  
    print('Pluto exists!')
if checkPluto(R):
    print('Pluto does not exist in this list!')
else:  
    print('Pluto exists!')