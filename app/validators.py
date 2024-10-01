import re
from validate_docbr import CPF

def cpf_invalido(cpf):
    validador = CPF()
    cpf_valido = validador.validate(cpf)
    return not cpf_valido


def nome_invalido(nome):
    return not nome.isalpha()


def numero_invalido(numero_celular):
    padrao = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(padrao, numero_celular)
    return not response
