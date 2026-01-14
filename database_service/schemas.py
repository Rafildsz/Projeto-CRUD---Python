from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    correntista: bool
    score_credito: float
    saldo_cc: float

class ClienteUpdate(BaseModel):
    nome: str
    telefone: str
    correntista: bool
    score_credito: float
    saldo_cc: float

