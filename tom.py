import pandas as pd
import mysql.connector
from json import loads, dumps
from flask import jsonify
from decimal import Decimal


""" def mijnfunctie2():
    print("plz werk?")
    Festival = pandas.read_csv("Festival.csv")
    result = Festival.to_json(orient="records")
    parsed = loads(result)
    
    return dumps(parsed, indent=4)  """ 

def mijnfunctie3():
    print("plz werk?")
    Festival = pd.read_csv("Festival.csv")
    
    # Selecting only the desired columns
    selected_columns = ["Cust_name", "Product_ID", "Gender", "Age"]
    filtered_festival = Festival[selected_columns]
    
    # Ordering the DataFrame based on the "Age" column
    sorted_festival = filtered_festival.sort_values(by="Age")
    
    # Converting the filtered DataFrame to JSON
    result = sorted_festival.to_json(orient="records")
    parsed = loads(result)

    return parsed

def mijnfunctie4(Leeftijd):
    print("plz werk?", Leeftijd)
    Festival = pd.read_csv("Festival.csv")
    
    # Selecting only the desired columns
    selected_columns = ["Cust_name", "Product_ID", "Gender", "Age"]
    filtered_festival = Festival[selected_columns]
    
    # Ordering the DataFrame based on the "Age" column
    sorted_festival = filtered_festival.sort_values(by="Age")
    
    # Converting the filtered DataFrame to JSON
    result = sorted_festival.to_json(orient="records")
    parsed = loads(result)

    return parsed

#age: custname, prodID, gender
#json



