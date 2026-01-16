def calcular_score(saldo_cc: float) -> int:
    score = 0

    if saldo_cc <= 0:
        return 0.0

    score = saldo_cc * 0.1

    if score > 1000:
        score = 1000

    return score

def cliente_correntista(correntista: bool, saldo_cc: float) -> float:

    if correntista == False:
        return 0.0
    
    return saldo_cc