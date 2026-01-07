import requests
from cliente_service.models import Cliente

DATABASE_SERVICE_URL = "http://127.0.0.1:8001"

def criar_cliente_no_database_service(cliente: dict):
    response = requests.post(
        f"{DATABASE_SERVICE_URL}/clientes",
        json=cliente
    )

    response.raise_for_status()
    return response.json()