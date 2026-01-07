from cliente_service.models import Cliente

def calcular_score(saldo_cc: float, correntista: bool) -> int:
    score = 0

    if correntista:
        score += 200

    if saldo_cc >= 1000:
        score += 300
    elif saldo_cc >= 500:
        score += 150
    else:
        score += 50

    return score
