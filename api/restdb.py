import os
import requests

BASE_URL = os.environ["RESTDB_URL"] + "/practica"
API_KEY = os.environ["RESTDB_API_KEY"]

HEADERS = {
    "Content-Type": "application/json",
    "x-apikey": API_KEY
}

def crear(data):
    return requests.post(BASE_URL, json=data, headers=HEADERS)

def listar():
    return requests.get(BASE_URL, headers=HEADERS)

def obtener(doc_id):
    return requests.get(f"{BASE_URL}/{doc_id}", headers=HEADERS)

def editar(doc_id, data):
    return requests.patch(f"{BASE_URL}/{doc_id}", json=data, headers=HEADERS)

def borrar(doc_id):
    return requests.delete(f"{BASE_URL}/{doc_id}", headers=HEADERS)
