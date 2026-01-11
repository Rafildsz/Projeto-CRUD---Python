from sqlalchemy import Column, Integer, String, Float, Boolean
from database_service.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(Integer)
    correntista = Column(Boolean)
    score_credito = Column(Float)
    saldo_cc = Column(Float)
