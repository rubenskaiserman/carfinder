# from flask import Flask, request, jsonify
import psycopg
import json
# import psycopg.extras

# app = Flask(__name__)

# @app.route('/', methods=["POST"])
# def index():

def get_request(id:str):
    with psycopg.connect("dbname=car_search user=kaiserman password=chakalaka") as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM cars WHERE id='{id}'")
            dict_result = dict()
            result = cur.fetchall()
            i = 0
            for column in cur.description:
                dict_result[column.name] = result[0][i]
                i+=1
            
            return dict_result


teste = json.dumps(get_request('9ecbe8c340a04bb1ab3837c6f9232ff7'), indent=4)
print(teste)
    
            




