from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from supabase import create_client, Client

# ---------- SUPABASE ----------
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Faltan variables de entorno de Supabase")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------- FLASK ----------
app = Flask(__name__)
CORS(app)

# GET → servir el HTML (IGUAL QUE TU EJEMPLO)
@app.route("/")
def index():
    return send_from_directory(".", "index.html")

# POST → guardar en la DB (MISMA RUTA, MISMO FETCH)
@app.route("/", methods=["POST"])
def guardar():
    try:
        datos = request.json
        print("DATOS:", datos)

        nombre = datos.get("nombre")
        apellido = datos.get("apellido")
        numero_id = datos.get("numero_id")
        color = datos.get("color_favorito")

        if not all([nombre, apellido, numero_id, color]):
            return jsonify({"error": "Faltan datos"}), 400

        res = supabase.table("practica").insert({
            "nombre": nombre,
            "apellido": apellido,
            "numero_id": numero_id,
            "color_favorito": color
        }).execute()

        print("SUPABASE:", res)

        if res.error:
            return jsonify({"error": str(res.error)}), 400

        return jsonify({"ok": True})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500
