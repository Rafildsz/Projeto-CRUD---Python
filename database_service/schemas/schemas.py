from typing import Optional
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

class ClienteUpdateUnit(BaseModel):
    nome: Optional[str] = None
    telefone: Optional[str] = None
    correntista: Optional[bool] = None
    score_credito: Optional[int] = None
    saldo_cc: Optional[float] = None

