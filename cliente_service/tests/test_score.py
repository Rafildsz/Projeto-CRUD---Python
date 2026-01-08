from cliente_service.service import calcular_score

def test_score_correntista_saldo_alto():
    score = calcular_score(saldo_cc=2000, correntista=True)
    assert score == 500

def test_score_nao_correntista_saldo_medio():
    score = calcular_score(saldo_cc=600, correntista=False)
    assert score == 150

def test_score_correntista_saldo_baixo():
    score = calcular_score(saldo_cc=200, correntista=True)
    assert score == 250

def test_score_nao_correntista_saldo_baixo():
    score = calcular_score(saldo_cc=100, correntista=False)
    assert score == 25