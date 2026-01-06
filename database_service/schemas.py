from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: int
    correntista: bool
    score_credito: float
    saldo_cc: float
