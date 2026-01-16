from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from api.supabase_client import supabase

app = Flask(__name__)
CORS(app)

# GET → sirve el HTML
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# POST → guarda en DB
@app.route("/", methods=["POST"])
def guardar():
    data = request.json

    nombre = data.get("nombre")
    apellido = data.get("apellido")
    numero_id = data.get("numero_id")
    color = data.get("color_favorito")

    if not all([nombre, apellido, numero_id, color]):
        return jsonify({"error": "Faltan datos"}), 400

    res = supabase.table("practica").insert({
        "nombre": nombre,
        "apellido": apellido,
        "numero_id": numero_id,
        "color_favorito": color
    }).execute()

    return jsonify({"ok": True, "data": res.data})
