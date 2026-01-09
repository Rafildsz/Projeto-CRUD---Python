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

def listar_clientes_do_database_service():
    response = requests.get(
        DATABASE_SERVICE_URL
    )

    response.raise_for_status()
    return response.json()

def atualizar_cliente_no_database_service(cliente_id: int, cliente: dict):
    response = requests.put(
        f"{DATABASE_SERVICE_URL}/{cliente_id}",
        json=cliente
    )
    response.raise_for_status()
    return response.json()

def deletar_cliente_no_database_service(cliente_id: int):   
    response = requests.delete(
        f"{DATABASE_SERVICE_URL}/{cliente_id}"
    )
    response.raise_for_status()
    return response.json()
