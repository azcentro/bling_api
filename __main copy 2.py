from fastapi import FastAPI, HTTPException
from bling_client import BlingClient
import requests
import os

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("BLING_ACCESS_TOKEN")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Produtos com Bling!"}

@app.get("/products")
def list_products():
    try:
        products = BlingClient.list_products()
        return products
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products_V3")
def list_products_v3():
    url = "https://api.bling.com.br/Api/v3/produtos"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

@app.get("/products/{product_id}")
def get_product(product_id: str):
    try:
        product = BlingClient.get_product(product_id)
        return product
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=400, detail=str(e))
