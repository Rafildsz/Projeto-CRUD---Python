import requests
from fastapi import HTTPException, status

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

def listar_cliente_do_database_service_com_id(cliente_id: int):
    response = requests.get(
        f"{DATABASE_SERVICE_URL}/{cliente_id}"
    )

    if response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    
    return response.json()

def atualizar_cliente_no_database_service(cliente_id: int, cliente: dict):
    response = requests.put(
        f"{DATABASE_SERVICE_URL}/{cliente_id}",
        json=cliente
    )

    if response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    
    response.raise_for_status()
    return response.json()

def deletar_cliente_no_database_service(cliente_id: int):   
    response = requests.delete(
        f"{DATABASE_SERVICE_URL}/{cliente_id}"
    )

    if response.status_code == 404:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )
    
    response.raise_for_status()
    return response.json()
