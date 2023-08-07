import pandas as pd
import mysql.connector
from json import loads, dumps
from flask import jsonify
from decimal import Decimal


#Important data I'm using
def chartbarfunctie3(katg):
    print(katg)
    df = pd.read_csv("Festival.csv")
    filtered_df = df[df['Product_Category'] == katg]
    result = filtered_df.to_json(orient="records")
    parsed = loads(result)
    
    return parsed

def JobEarnings():
    print()
    df = pd.read_csv("Festival.csv")
    desired_columns = ['Amount', 'Occupation']
    filtered_df = df[desired_columns]
    filtered_df.dropna(inplace=True)
    result = filtered_df.to_json(orient="records")
    parsed = loads(result)

    return parsed

def ProdEarnings():
    print()
    df = pd.read_csv("Festival.csv")
    desired_columns = ['Amount', 'Product_Category']
    filtered_df = df[desired_columns]
    filtered_df.dropna(inplace=True)
    result = filtered_df.to_json(orient="records")
    parsed = loads(result)

    return parsed

def AgeSexAmount():
    print()
    df = pd.read_csv("Festival.csv")
    desired_columns = ['Amount', 'Gender', 'Age Group']
    filtered_df = df[desired_columns]
    filtered_df.dropna(inplace=True)
    result = filtered_df.to_json(orient="records")
    parsed = loads(result)

    return parsed

def State():
    print()
    df = pd.read_csv("Festival.csv")
    desired_columns = ['Amount', 'State', 'Zone']
    filtered_df = df[desired_columns]
    filtered_df.dropna(inplace=True)
    result = filtered_df.to_json(orient="records")
    parsed = loads(result)

    return parsed






#Extra data
def mijnfunctie3():
    print("plz werk?")
    Festival = pd.read_csv("Festival.csv")
    
    # Dropping the "Status" and "unnamed1" columns
    columns_to_drop = ["Status", "unnamed1"]
    filtered_festival = Festival.drop(columns=columns_to_drop)

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

def chartbarfunctie2():
    df = pd.read_csv("Festival.csv")
    filtered_df = df[df['Product_Category'] == 'Clothing & Apparel']
    result = filtered_df.to_json(orient="records")
    parsed = loads(result)

    return parsed


     




