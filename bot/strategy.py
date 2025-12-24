def simple_decision(price: float):
    """
    Şimdilik sadece örnek:
    fiyat çift sayıysa AL 😄
    """
    if int(price) % 2 == 0:
        return "BUY"
    return "HOLD"
