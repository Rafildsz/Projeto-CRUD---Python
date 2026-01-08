import requests
from cliente_service.models import ClienteEntrada, ClienteCompleto

DATABASE_SERVICE_URL = "http://127.0.0.1:8001/clientes"

def criar_cliente_no_database_service(cliente: dict):
    response = requests.post(
        DATABASE_SERVICE_URL,
        json=cliente
    )
    response.raise_for_status()
    return response.json()
