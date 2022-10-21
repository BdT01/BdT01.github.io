#!usr/bin/env python3

from flask import Flask, make_response, request
from resthistorial.historialApi import Historial
import sqlite3
import json

app = Flask("restHistorial")
HISTORIAL = Historial()
DATABASE = "pacientes.db"

@app.route("/historial/<id>", methods=["GET", "PUT"])
def get_historial(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    
    if request.method == "GET":
        res = cur.execute(f'SELECT * FROM historial WHERE id = "{id}"').fetchone()
        if res is None:
            con.close()
            return make_response("Not found", 404)
        
        HISTORIAL.nombre = res[7]
        HISTORIAL.id = res[0]
        HISTORIAL.fecha = res[1]
        HISTORIAL.hora = res[2]
        HISTORIAL.antecedentes = res[3]
        HISTORIAL.tratamiento = res[4]
        HISTORIAL.problemas = res[5]
        HISTORIAL.observaciones = res[6]
        con.close()
        return make_response(HISTORIAL.get_historial(), 200)

    elif request.method == "PUT":
        if not request.is_json:
            return make_response("Bad request", 400)
        
        request_json = json.loads(request.get_json())

        nombre = request_json["nombre"]
        fecha = request_json["fecha"]
        hora = request_json["hora"]
        antecedentes = request_json["antecedentes"]
        tratamiento = request_json["tratamiento"]
        problemas = request_json["problemas"]
        observaciones = request_json["observaciones"]

        cur.execute(f'INSERT INTO historial VALUES ("{id}", "{fecha}", "{hora}", "{antecedentes}", "{tratamiento}", "{problemas}", "{observaciones}", "{nombre}")')
        con.commit()

        con.close()
        return make_response("OK", 200)

@app.route("/historial/antecedentes/<id>", methods=["POST"])
def add_antecedente(id):
    if not request.is_json:
        return make_response("Bad request", 400)
    
    request_json = json.loads(request.get_json())
    antecedente = request_json["antecedente"]

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM historial WHERE id = "{id}"').fetchone()
    if res is None:
        con.close()
        return make_response("Not found", 404)
    
    antecedentes = res[3]
    antecedentes += f", {antecedente}"
    cur.execute(f'UPDATE historial SET antecedentes = "{antecedentes}" WHERE id = "{id}"')
    con.commit()
    con.close()
    return make_response("OK", 200)

@app.route("/historial/tratamiento/<id>", methods=["POST"])
def add_tratamiento(id):
    if not request.is_json:
        return make_response("Bad request", 400)
    
    request_json = json.loads(request.get_json())
    tratamiento = request_json["tratamiento"]

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM historial WHERE id = "{id}"').fetchone()
    if res is None:
        con.close()
        return make_response("Not found", 404)
    
    tratamientos = res[4]
    tratamientos += f", {tratamiento}"
    cur.execute(f'UPDATE historial SET tratamiento = "{tratamientos}" WHERE id = "{id}"')
    con.commit()
    con.close()
    return make_response("OK", 200)

@app.route("/historial/problemas/<id>", methods=["POST"])
def add_problema(id):
    if not request.is_json:
        return make_response("Bad request", 400)
    
    request_json = json.loads(request.get_json())
    problema = request_json["problema"]

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM historial WHERE id = "{id}"').fetchone()
    if res is None:
        con.close()
        return make_response("Not found", 404)
    
    problemas = res[5]
    problemas += f", {problema}"
    cur.execute(f'UPDATE historial SET problemas = "{problemas}" WHERE id = "{id}"')
    con.commit()
    con.close()
    return make_response("OK", 200)

@app.route("/historial/observaciones/<id>", methods=["POST"])
def add_observacion(id):
    if not request.is_json:
        return make_response("Bad request", 400)
    
    request_json = json.loads(request.get_json())
    observacion = request_json["observacion"]

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM historial WHERE id = "{id}"').fetchone()
    if res is None:
        con.close()
        return make_response("Not found", 404)
    
    observaciones = res[6]
    observaciones += f", {observacion}"
    cur.execute(f'UPDATE historial SET observaciones = "{observaciones}" WHERE id = "{id}"')
    con.commit()
    con.close()
    return make_response("OK", 200)

@app.route("/historial/nombre/<id>", methods=["POST"])
def update_nombre(id):
    if not request.is_json:
        return make_response("Bad request", 400)
    
    request_json = json.loads(request.get_json())
    nombre = request_json["nombre"]

    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM historial WHERE id = "{id}"').fetchone()
    if res is None:
        con.close()
        return make_response("Not found", 404)
    
    cur.execute(f'UPDATE historial SET nombre = "{nombre}" WHERE id = "{id}"')
    con.commit()
    con.close()
    return make_response("OK", 200)

if __name__ == "__main__":
    app.run(debug=True)



