import pandas

def mijnfunctie():
    pokemons = pandas.read_csv("Pokemon.csv")
    print(pokemons)
    return "hij doet het"