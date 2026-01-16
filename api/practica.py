from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from supabase import create_client, Client

# ---------- SUPABASE CLIENT ----------
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise Exception("Faltan variables de entorno de Supabase")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------- FLASK APP ----------
app = Flask(__name__)
CORS(app)

# ---------- GET: SERVIR HTML ----------
@app.route("/", methods=["GET"])
def index():
    return send_from_directory(".", "index.html")

# ---------- POST: GUARDAR EN DB ----------
@app.route("/", methods=["POST"])
def guardar():
    try:
        data = request.json
        print("DATA RECIBIDA:", data)

        nombre = data.get("nombre")
        apellido = data.get("apellido")
        numero_id = data.get("numero_id")
        color = data.get("color_favorito")

        if not all([nombre, apellido, numero_id, color]):
            return jsonify({
                "ok": False,
                "error": "Faltan datos"
            }), 400

        res = supabase.table("practica").insert({
            "nombre": nombre,
            "apellido": apellido,
            "numero_id": numero_id,
            "color_favorito": color
        }).execute()

        print("SUPABASE RESPONSE:", res)

        if res.error:
            return jsonify({
                "ok": False,
                "error": res.error.message if hasattr(res.error, "message") else str(res.error)
            }), 400

        return jsonify({
            "ok": True,
            "data": res.data
        })

    except Exception as e:
        print("ERROR BACKEND:", str(e))
        return jsonify({
            "ok": False,
            "error": str(e)
        }), 500
