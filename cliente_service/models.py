from pydantic import BaseModel

class Cliente(BaseModel):
    nome: str
    telefone: int
    correntista: bool
    saldo_cc: float
