# Projeto-CRUD---Python com FastAPI 

## Visão Geral

Este projeto é uma aplicação CRUD (Create, Read, Update, Delete) desenvolvida em Python utilizando o FastAPI, seguindo uma arquitetura de microsserviços.

A aplicação é dividida em dois serviços independentes:

- **cliente_service**  
  Responsável pela regra de negócio, cálculo de score de crédito e comunicação com o serviço de banco de dados.

- **database_service**  
  Responsável exclusivamente pela persistência dos dados, utilizando SQLAlchemy e banco de dados relacional.

Esse modelo reflete um cenário real de sistemas distribuídos, com separação clara de responsabilidades.

---

## Score de Crédito

O score de crédito é calculado no cliente_service com base em:

- Se o cliente é correntista

- Valor do saldo em conta corrente (saldo_cc)

Essa lógica não fica no banco de dados, garantindo separação de responsabilidades.

---

## Tecnologias Utilizadas

- Python
- FastAPI
- SQLite
- Uvicorn
- SQLAlchemy
- Pydantic
- Requests
- Pytest

---

## Como Rodar o Projeto

### Acessar a pasta do projeto no terminal com:

cd Projeto-CRUD---Python

### Criar ambiente virtual (venv)

python3 -m venv venv

### Ativar venv no terminal

source venv/bin/activate

### Instalar dependencias do projeto

pip install -r requirements.txt

### Rodar as APIs - Ambas em terminais diferentes

uvicorn cliente_service.main:app --reload --port 8000

uvicorn database_service.main:app --reload --port 8001

### Executando Testes 

- **database_service (CRUD)**

pytest database_service/tests/test_crud.py

- **cliente_service (regra de negócio)**

pytest cliente_service/tests/test_score.py

---

## Funcionalidades do CRUD

Todos os endpoints devem ser acessados via cliente_service, que se comunica internamente com o database_service.

Em um terceiro terminal, separado das API's, rode os comandos abaixo:

### CREATE - Criar Cliente

curl -X POST http://127.0.0.1:8000/clientes \
-H "Content-Type: application/json" \
-d '{
  "nome": "João Silva",
  "telefone": 11999998888,
  "correntista": true,
  "saldo_cc": 8500
}'

### READ - Listar Clientes

curl http://127.0.0.1:8000/clientes

### UPDATE - Atualizar Clientes 

curl -X PUT http://127.0.0.1:8000/clientes/1 \
-H "Content-Type: application/json" \
-d '{
  "nome": "João Silva Atualizado",
  "telefone": 11911112222,
  "correntista": false,
  "saldo_cc": 400
}'

### DELETE - Deletar Cliente 

curl -X DELETE http://127.0.0.1:8000/clientes/1

---
