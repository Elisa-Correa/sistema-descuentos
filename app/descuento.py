def validar_tipo(total):
    if not isinstance(total, (int, float)):
        raise TypeError("El total debe ser un número")


def validar_valor(total):
    if total < 0:
        raise ValueError("El total no puede ser negativo")


def calcular_descuento(total):
    validar_tipo(total)
    validar_valor(total)

    if total > 20000:
        return total * 0.30
    elif total > 10000:
        return total * 0.20
    elif total > 5000:
        return total * 0.10
    elif total > 1000:
        return total * 0.05
    else:
        return 0


def calcular_total_con_descuento(total):
    descuento = calcular_descuento(total)
    return total - descuento


def obtener_porcentaje_descuento(total):
    if total > 20000:
        return 30
    elif total > 10000:
        return 20
    elif total > 5000:
        return 10
    elif total > 1000:
        return 5
    else:
        return 0

