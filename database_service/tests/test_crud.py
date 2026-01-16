from fastapi.testclient import TestClient
from database_service.app.main import app

client = TestClient(app)

def test_criar_cliente():
    response = client.post(
        "/clientes",
        json={
            "nome": "João Teste",
            "telefone": "11999999999",
            "correntista": True,
            "score_credito": 700,
            "saldo_cc": 1500.0
        }
    )

    assert response.status_code == 200
    assert response.json()["mensagem"] == "Cliente criado com sucesso"


def test_listar_clientes():
    response = client.get("/clientes")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_atualizar_cliente():
    response = client.put(
        "/clientes/1",
        json={
            "nome": "João Atualizado",
            "telefone": "11888888888",
            "correntista": False,
            "score_credito": 650,
            "saldo_cc": 900.0
        }
    )

    assert response.status_code == 200
    assert response.json()["mensagem"] == "Cliente atualizado com sucesso"


def test_deletar_cliente():
    response = client.delete("/clientes/1")

    assert response.status_code == 200
    assert response.json()["mensagem"] == "Cliente deletado com sucesso"
