from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from database_service.database.database import engine, Base, SessionLocal
from database_service.models.models import Cliente
from database_service.schemas.schemas import ClienteCreate, ClienteUpdate, ClienteUpdateUnit
from cliente_service.service.service import calcular_score


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




@app.post("/clientes", status_code=status.HTTP_201_CREATED)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):

    try:
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
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e
        ) 

    return novo_cliente




@app.get("/clientes", status_code=status.HTTP_200_OK)
def listar_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes




@app.get("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def buscar_cliente(cliente_id: int, db: Session = Depends(get_db)):

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    return cliente




@app.put("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def atualizar_cliente(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    cliente_db = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    cliente_db.nome = cliente.nome
    cliente_db.telefone = cliente.telefone
    cliente_db.correntista = cliente.correntista
    cliente_db.score_credito = cliente.score_credito
    cliente_db.saldo_cc = cliente.saldo_cc

    db.commit()

    return {"mensagem": "Cliente atualizado com sucesso"}



@app.patch("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def atualizar_cliente_parcial(cliente_id: int, cliente: ClienteUpdateUnit, db: Session = Depends(get_db)):
    cliente_db = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    if cliente.nome is not None:
        cliente_db.nome = cliente.nome

    if cliente.telefone is not None:
        cliente_db.telefone = cliente.telefone

    if cliente.correntista is not None:
        cliente_db.correntista = cliente.correntista

    if cliente.score_credito is not None:
        cliente_db.score_credito = cliente.score_credito

    if cliente.saldo_cc is not None:
        cliente_db.saldo_cc = cliente.saldo_cc

    if cliente_db.correntista is False:
        cliente_db.saldo_cc = 0.0

    if cliente_db.saldo_cc <= 0:
        cliente_db.score_credito = 0.0
    else:
        score_credito = calcular_score(cliente_db.saldo_cc)
        cliente_db.score_credito = score_credito

    db.commit()

    return {"mensagem": "Cliente atualizado com sucesso"}



@app.delete("/clientes/{cliente_id}", status_code=status.HTTP_200_OK)
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    if cliente.saldo_cc != 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não é possível deletar um cliente com saldo na conta corrente"
        )

    db.delete(cliente)
    db.commit()

    return {"mensagem": "Cliente deletado com sucesso"}



