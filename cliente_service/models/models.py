from pydantic import BaseModel

class ClienteEntrada(BaseModel):
    nome: str
    telefone: str
    correntista: bool
    saldo_cc: float

class ClienteCompleto(BaseModel):
    nome: str
    telefone: str
    correntista: bool
    saldo_cc: float
    score_credito: float
