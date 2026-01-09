from fastapi import FastAPI
from cliente_service.models import ClienteEntrada, ClienteCompleto
from cliente_service.service import calcular_score
from cliente_service.http_client import criar_cliente_no_database_service, listar_clientes_do_database_service, atualizar_cliente_no_database_service, deletar_cliente_no_database_service

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Cliente Service funcionando"}

@app.post("/clientes")
def criar_cliente(cliente: ClienteEntrada):

    score = calcular_score(
        saldo_cc=cliente.saldo_cc,
        correntista=cliente.correntista
    )

    cliente_completo = ClienteCompleto(
        nome=cliente.nome,
        telefone=cliente.telefone,
        saldo_cc=cliente.saldo_cc,
        correntista=cliente.correntista,
        score_credito=score
    )

    resposta = criar_cliente_no_database_service(cliente_completo.dict())

    return resposta



@app.get("/clientes")
def listar_clientes():

    clientes = listar_clientes_do_database_service()
    return clientes


@app.put("/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente: ClienteEntrada):

    score = calcular_score(
        saldo_cc=cliente.saldo_cc,
        correntista=cliente.correntista
    )

    cliente_completo = ClienteCompleto(
        nome=cliente.nome,
        telefone=cliente.telefone,
        saldo_cc=cliente.saldo_cc,
        correntista=cliente.correntista,
        score_credito=score
    )

    resposta = atualizar_cliente_no_database_service(cliente_id, cliente_completo.dict())

    return resposta

@app.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
       
    resposta = deletar_cliente_no_database_service(cliente_id)
    return resposta
