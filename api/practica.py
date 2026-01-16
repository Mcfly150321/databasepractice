from flask import Flask, request, jsonify
from flask_cors import CORS
from api import restdb

app = Flask(__name__)
CORS(app)

@app.route("/api/practica", methods=["POST"])
def crear_practica():
    datos = request.json
    r = restdb.crear(datos)
    return jsonify(r.json()), r.status_code


@app.route("/api/practica", methods=["GET"])
def listar_practica():
    r = restdb.listar()
    return jsonify(r.json()), r.status_code


@app.route("/api/practica/<id>", methods=["GET"])
def obtener_practica(id):
    r = restdb.obtener(id)
    return jsonify(r.json()), r.status_code


@app.route("/api/practica/<id>", methods=["PATCH"])
def editar_practica(id):
    r = restdb.editar(id, request.json)
    return jsonify(r.json()), r.status_code


@app.route("/api/practica/<id>", methods=["DELETE"])
def borrar_practica(id):
    r = restdb.borrar(id)
    return "", r.status_code
