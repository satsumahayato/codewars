# Codewars.com
# July 10, 2020
# Get Planet Name By ID
# https://www.codewars.com/kata/515e188a311df01cba000003

# The function is not returning the correct values. Can you figure out why?
# get_planet_name(3) # should return 'Earth'

def get_planet_name(id):
    switch = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return switch.get(id)
