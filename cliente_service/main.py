from fastapi import FastAPI
from cliente_service.models import Cliente
from cliente_service.service import calcular_score
from cliente_service.http_client import criar_cliente_no_database_service

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Cliente Service funcionando"}

@app.post("/clientes")
def criar_cliente(cliente: Cliente):
    cliente_dict = cliente.dict()

    criar_cliente_no_database_service(cliente_dict)

    score = calcular_score(
        saldo_cc=cliente.saldo_cc,
        correntista=cliente.correntista
    )

    return {
        "mensagem": "Cliente recebido com sucesso",
        "nome": cliente.nome,
        "score_credito": score
    }
