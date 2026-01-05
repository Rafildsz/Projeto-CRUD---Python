from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"mensagem": "API do Banco funcionando"}

from pydantic import BaseModel

class Cliente(BaseModel):
    nome: str
    telefone: int
    correntista: bool
    saldo_cc: float

@app.post("/clientes")
def criar_cliente(cliente: Cliente):
    return {
        "mensagem": "Cliente recebido com sucesso",
        "cliente": cliente
    }
