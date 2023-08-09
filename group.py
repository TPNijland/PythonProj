import pandas as pd
import mysql.connector
from json import loads, dumps
from flask import jsonify
from decimal import Decimal

""" #LowCode, Java, Powerapp(?)
@app.route("/Producten")
def Prods():
    return tom.Producten() """


#Important data the group is using
def Producten():
    df = pd.read_csv("Festival.csv")
    # Filter for male customers
    male_df = df[df['Gender'] == 'M']
    # Find the highest order frequency among male customers
    max_order_frequency = male_df['Orders'].max()
    # Filter for male customers with the highest order frequency
    filtered_df = male_df[male_df['Orders'] == max_order_frequency]
    # Select only desired columns
    desired_columns = ['Cust_name', 'Gender', 'Orders']
    filtered_df = filtered_df[desired_columns]
    # Drop rows with missing values
    filtered_df.dropna(inplace=True)
    # Convert to JSON records
    result = filtered_df.to_json(orient="records")
    parsed = loads(result)

    return parsed
