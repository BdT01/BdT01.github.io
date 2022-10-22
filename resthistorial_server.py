#!usr/bin/env python3

from flask import Flask, make_response, request
from resthistorial.historialApi import Historial
import sqlite3
import json

from flask_cors import CORS, cross_origin


app = Flask("restHistorial")
app.config['CORS_HEADERS'] = 'Content-Type'

HISTORIAL = Historial()
DATABASE = "pacientes.db"


@app.route("/historial/<id>", methods=["GET", "PUT", "POST"])
@cross_origin()
def get_historial(id):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()

    if request.method == "GET":
        res = cur.execute(
            f'SELECT * FROM historial WHERE id = "{id}"').fetchone()
        if res is None:
            con.close()
            return make_response("Not found", 404)

        HISTORIAL.id = res[0]
        HISTORIAL.fecha = res[1]
        HISTORIAL.hora = res[2]
        HISTORIAL.tratamientos = res[3].split(", ")
        HISTORIAL.problemas = res[4].split(", ")
        HISTORIAL.observaciones = res[5].split(", ")
        HISTORIAL.nombre = res[6]
        HISTORIAL.alergias = res[7].split(", ")
        HISTORIAL.enfermedades = res[8].split(", ")
        HISTORIAL.medicamentos = res[9].split(", ")
        HISTORIAL.cirugias = res[10].split(", ")
        HISTORIAL.otros = res[11].split(", ")
        con.close()
        return make_response(json.dumps(HISTORIAL.get_historial()), 200)

    elif request.method == "PUT":
        if not request.is_json:
            return make_response("Bad request", 400)

        request_json = request.get_json()

        if id != request_json["id"]:
            return make_response("Bad request", 400)
        
        print(request_json)

        nombre = request_json["nombre"]
        # fecha = request_json["fecha"]
        fecha = "22/10/2022"
        # hora = request_json["hora"]
        hora = "13:59:00"

        alergias =", ".join(request_json["alergias"])
        enfermedades = ", ".join(request_json["enfermedades"])
        medicamentos = ", ".join(request_json["medicamentos"])
        cirugias = ", ".join(request_json["cirugias"])
        otros = ", ".join(request_json["otros"])

        tratamientos = ", ".join(request_json["tratamientos"])
        problemas = ", ".join(request_json["problemas"])
        observaciones = ", ".join(request_json["observaciones"])

        cur.execute(
            f'INSERT INTO historial VALUES ("{id}", "{fecha}", "{hora}", "{alergias}","{enfermedades}", "{medicamentos}","{cirugias}","{otros}","{tratamientos}", "{problemas}", "{observaciones}", "{nombre}")')
        con.commit()

        con.close()
        return make_response("OK", 200)

    elif request.method == "POST":
        if not request.is_json:
            return make_response("Bad request", 400)

        # request_json = json.loads(request.get_json())
        request_json = request.get_json()
        print(request_json)

        if id != request_json["id"]:
            return make_response("Bad request", 400)

        nombre = request_json["nombre"]
        # fecha = request_json["fecha"]
        # hora = request_json["hora"]
        fecha = "22/10/2022"
        hora = "13:59:00"



        alergias =", ".join(request_json["alergias"])
        enfermedades = ", ".join(request_json["enfermedades"])
        medicamentos = ", ".join(request_json["medicamentos"])
        cirugias = ", ".join(request_json["cirugias"])
        otros = ", ".join(request_json["otros"])

        tratamientos = ", ".join(request_json["tratamientos"])
        problemas = ", ".join(request_json["problemas"])
        observaciones = ", ".join(request_json["observaciones"])

        # print(observaciones)

        cur.execute(
            f'UPDATE historial SET fecha = "{fecha}", hora = "{hora}", alergias = "{alergias}", enfermedades = "{enfermedades}", medicamentos = "{medicamentos}", cirugias = "{cirugias}", otros = "{otros}", tratamientos = "{tratamientos}", problemas = "{problemas}", observaciones = "{observaciones}", nombre = "{nombre}" WHERE id = "{id}"')
        con.commit()

        con.close()
        return make_response("OK", 200)




if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
