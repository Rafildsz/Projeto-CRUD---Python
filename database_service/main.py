from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models import Cliente
from schemas import ClienteCreate


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"mensagem": "API do Banco funcionando"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clientes")
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    novo_cliente = Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        correntista=cliente.correntista,
        score_credito=cliente.score_credito,
        saldo_cc=cliente.saldo_cc
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return {"mensagem": "Cliente criado com sucesso"}
  