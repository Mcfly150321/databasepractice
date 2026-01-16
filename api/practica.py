from flask import Flask, request, jsonify
from flask_cors import CORS
from api.supabase_client import supabase

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def crear_registro():
    data = request.json

    nombre = data.get("nombre")
    apellido = data.get("apellido")
    numero_id = data.get("numero_id")
    color = data.get("color_favorito")

    if not all([nombre, apellido, numero_id, color]):
        return jsonify({"error": "Faltan datos"}), 400

    response = supabase.table("practica").insert({
        "nombre": nombre,
        "apellido": apellido,
        "numero_id": numero_id,
        "color_favorito": color
    }).execute()

    return jsonify({
        "ok": True,
        "inserted": response.data
    })
