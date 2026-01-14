from cliente_service.models import ClienteEntrada, ClienteCompleto

def calcular_score(saldo_cc: float, correntista: bool) -> int:
    score = 0

    if saldo_cc <= 0:
        return 0.0

    score = saldo_cc * 0.1

    if correntista:
        score += 200

    if score > 1000:
        score = 1000

    return score
