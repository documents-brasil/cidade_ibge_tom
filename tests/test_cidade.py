import pytest
from cidade_ibge_tom import info_cidade


def test_info_cidade_ibge_5222302():
    cidade = info_cidade(codigo='5222302')
    esperado = {'ibge': '5222302', 'tom': '1068', 'nome': 'Vila Propício-GO'}
    assert cidade == esperado


def test_info_cidade_tom_1068():
    cidade = info_cidade(codigo='1068')
    esperado = {'ibge': '5222302', 'tom': '1068', 'nome': 'Vila Propício-GO'}
    assert cidade == esperado


def test_info_cidade_ibge_erro():
    cidade = info_cidade(codigo='5222300')
    esperado = {}
    assert cidade == esperado


def test_info_cidade_tom_erro():
    cidade = info_cidade(codigo='9999')
    esperado = {}
    assert cidade == esperado


def test_info_cidade_sao_paulo():
    cidade = info_cidade(codigo='3550308')
    esperado = {'ibge': '3550308', 'tom': '7107', 'nome': 'São Paulo-SP'}
    assert cidade == esperado


def test_info_cidade_brasilia():
    cidade = info_cidade(codigo='5300108')
    esperado = {'ibge': '5300108', 'tom': '9701', 'nome': 'Brasília-DF'}
    assert cidade == esperado


def test_info_cidade_codigo_vazio():
    cidade = info_cidade(codigo='')
    esperado = {}
    assert cidade == esperado


def test_info_cidade_sem_parametro():
    cidade = info_cidade()
    esperado = {}
    assert cidade == esperado


@pytest.mark.parametrize(
    "codigo,esperado",
    [
        ("1100015", {'ibge': '1100015', 'tom': '0033', 'nome': "Alta Floresta D'Oeste-RO"}),
        ("0033", {'ibge': '1100015', 'tom': '0033', 'nome': "Alta Floresta D'Oeste-RO"}),
    ]
)
def test_info_cidade_parametrizado(codigo, esperado):
    cidade = info_cidade(codigo=codigo)
    assert cidade == esperado
