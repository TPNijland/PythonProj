import pandas as pd
import json

def mijnfunctie():
    pokemons = pandas.read_csv("Pokemon.csv")
    print(pokemons)
    return "hij doet het"

def chartbarfunctie():
    df = pd.read_csv("Festival.csv")
    filtered_df = df[df['Product_Category'] == 'Clothing & Apparel']
    result = filtered_df.to_json(orient="records")
    parsed = json.loads(result)
    
    return parsed 

#print(chartbarfunctie())
