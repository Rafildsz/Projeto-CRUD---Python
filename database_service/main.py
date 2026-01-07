from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database_service.database import engine, Base, SessionLocal
from database_service.models import Cliente
from database_service.schemas import ClienteCreate, ClienteUpdate


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

@app.get("/clientes")
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes



@app.put("/clientes/{cliente_id}")
def atualizar_cliente(
    cliente_id: int,
    cliente: ClienteUpdate,
    db: Session = Depends(get_db)
):
    cliente_db = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente_db:
        return {"erro": "Cliente não encontrado"}
    
    cliente_db.nome = cliente.nome
    cliente_db.telefone = cliente.telefone
    cliente_db.correntista = cliente.correntista
    cliente_db.score_credito = cliente.score_credito
    cliente_db.saldo_cc = cliente.saldo_cc

    db.commit()

    return {"mensagem": "Cliente atualizado com sucesso"}

@app.delete("/clientes/{cliente_id}")
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        return {"erro": "Cliente não encontrado"}

    db.delete(cliente)
    db.commit()

    return {"mensagem": "Cliente deletado com sucesso"}


