import requests
import json

# Claves de la API
consumer_key = ""
consumer_secret = ""

# URL de la API de WooCommerce
url = "http://woocomercetest.local/wp-json/wc/v3/products"

# Cabecera de autenticación básica (se maneja por requests automáticamente con las claves)
auth = (consumer_key, consumer_secret)

# Datos del producto (esto lo podrías leer desde un archivo o base de datos)
products = [
    {
        "name": "Producto 1",
        "sku": "SKU001",
        "description": "Descripción del producto 1",
        "regular_price": "19.99",
        "stock_quantity": 10,
        "categories": [{"name": "Categoría 1"}],
        "images": [{"src": "http://example.com/image1.jpg"}]
    },
    {
        "name": "Producto 2",
        "sku": "SKU002",
        "description": "Descripción del producto 2",
        "regular_price": "29.99",
        "stock_quantity": 5,
        "categories": [{"name": "Categoría 2"}],
        "images": [{"src": "http://example.com/image2.jpg"}]
    }
]

# Subir productos
for product in products:
    response = requests.post(url, json=product, auth=auth)

    if response.status_code == 201:
        print(f"Producto '{product['name']}' subido correctamente.")
    else:
        print(
            f"Error al subir el producto '{product['name']}': {response.status_code} - {response.text}")
