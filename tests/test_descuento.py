import pytest
from app.descuento import calcular_descuento, calcular_total_con_descuento


# Casos exitosos
def test_descuento_30():
    assert calcular_descuento(25000) == 7500


def test_descuento_20():
    assert calcular_descuento(15000) == 3000


def test_descuento_10():
    assert calcular_descuento(7000) == 700


def test_descuento_5():
    assert calcular_descuento(2000) == 100


def test_sin_descuento():
    assert calcular_descuento(500) == 0


def test_total_final():
    assert calcular_total_con_descuento(10000) == 8000


#  Caso de error (tipo de dato incorrecto)
def test_error_tipo():
    with pytest.raises(TypeError):
        calcular_descuento("texto")


# Caso de error (valor negativo)
def test_error_valor():
    with pytest.raises(ValueError):
        calcular_descuento(-100)


# Caso borde
def test_descuento_borde():
    resultado = calcular_descuento(1000)
    assert resultado == 0  # límite inferior
