from fastapi import FastAPI, HTTPException
from bling_client import BlingClient

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

@app.get("/products/{product_id}")
def get_product(product_id: str):
    try:
        product = BlingClient.get_product(product_id)
        return product
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=400, detail=str(e))
