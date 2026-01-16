from cliente_service.service.service import calcular_score

def test_score_correntista_saldo_alto():
    score = calcular_score(saldo_cc=2000)
    assert score == 200

def test_score_nao_correntista_saldo_medio():
    score = calcular_score(saldo_cc=600)
    assert score == 60

def test_score_correntista_saldo_baixo():
    score = calcular_score(saldo_cc=200)
    assert score == 250

def test_score_nao_correntista_saldo_baixo():
    score = calcular_score(saldo_cc=100)
    assert score == 25