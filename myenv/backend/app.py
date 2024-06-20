from flask import Flask, render_template, request
import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

def execute_sql_commands(sql):
    con = sqlite3.connect("zoo.db", check_same_thread=False)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

def return_sql_data(sql):
    con = sqlite3.connect("zoo.db", check_same_thread=False)
    cur = con.cursor()
    res = cur.execute(sql).fetchall()
    con.close()
    return res


@app.route('/', methods=['post'])
def hello():
    # sql = "DELETE FROM animals"
    # execute_sql_commands(sql)
        sql =           """CREATE TABLE IF NOT EXISTS animals (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        kind TEXT,
                        name TEXT,
                        age INTEGER);"""
        execute_sql_commands(sql)
        # sql = "INSERT INTO animals (kind, name, age) VALUES ('Lion', 'Pena', 15)"
        # execute_sql_commands(sql)
        # sql = "INSERT INTO animals (kind, name, age) VALUES ('pinguin', 'funny', 4)"
        # execute_sql_commands(sql)
        # return "HELLO WORLD!!!"

    

@app.route('/add_animal', methods = ['post'])
def add_animals():
     data = request.get_json()
     newKind = "Popotam"
     newName = "Hipo"
     newAge = 45
    #  newKind = data["kind"]
    #  newName = data["name"]
    #  newAge = data["age"]
     sql = f"INSERT INTO animals (kind,name,age) VALUES ('{newKind}', '{newName}', {newAge})"
     execute_sql_commands(sql)
     return "HELLO WORLD!!!"

@app.route('/get_animals', methods = ['get'])
def get_animals():
    sql = """
        select * from animals
        """
    res = return_sql_data(sql)
    animals_list = []
    for row in res:
        dict_row = {"id":row[0], "kind":row[1], "name":row[2], "age":row[3]}
        animals_list.append(dict_row)
    return animals_list


if __name__ == '__main__':
    app.run(debug=True)


