from fastapi import FastAPI, status
from cliente_service.models.models import ClienteEntrada, ClienteCompleto
from cliente_service.service.service import calcular_score, cliente_correntista
from cliente_service.http_client.http_client import criar_cliente_no_database_service, listar_clientes_do_database_service, atualizar_cliente_no_database_service, deletar_cliente_no_database_service, listar_cliente_do_database_service_com_id,atualizar_cliente_parcial_no_database_service

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Cliente Service funcionando"}




@app.post("/clientes", status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: ClienteEntrada):

    saldo_corrigido = cliente_correntista(
        correntista=cliente.correntista,
        saldo_cc=cliente.saldo_cc
    )

    score = calcular_score(
        saldo_cc=saldo_corrigido
    )

    cliente_completo = ClienteCompleto(
        nome=cliente.nome,
        telefone=cliente.telefone,
        saldo_cc=saldo_corrigido,
        correntista=cliente.correntista,
        score_credito=score
    )

    resposta = criar_cliente_no_database_service(cliente_completo.dict())

    return resposta


@app.get("/clientes", status_code=status.HTTP_200_OK)
def listar_clientes():

    clientes = listar_clientes_do_database_service()
    return clientes




@app.get("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def buscar_cliente(cliente_id: int):

    cliente = listar_cliente_do_database_service_com_id(cliente_id)
    return cliente    


@app.get("/clientes/score/{cliente_id}", status_code=status.HTTP_200_OK)
def buscar_score(cliente_id: int):

    cliente = listar_cliente_do_database_service_com_id(cliente_id)
    return {"score_credito": cliente["score_credito"], 
            "nome": cliente["nome"]
            }



@app.put("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def atualizar_cliente(cliente_id: int, cliente: ClienteEntrada):

    saldo_corrigido = cliente_correntista(
        correntista=cliente.correntista,
        saldo_cc=cliente.saldo_cc
    )
    score = calcular_score(
        saldo_cc=saldo_corrigido
    )

    cliente_completo = ClienteCompleto(
        nome=cliente.nome,
        telefone=cliente.telefone,
        saldo_cc=saldo_corrigido,
        correntista=cliente.correntista,
        score_credito=score
    )

    resposta = atualizar_cliente_no_database_service(cliente_id, cliente_completo.dict())

    return resposta

@app.patch("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def atualizar_cliente_parcial(cliente_id: int, cliente: dict):
       
    resposta = atualizar_cliente_parcial_no_database_service(cliente_id, cliente)
    return resposta



@app.delete("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def deletar_cliente(cliente_id: int):
       
    resposta = deletar_cliente_no_database_service(cliente_id)
    return resposta
