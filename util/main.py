# -*- coding: utf-8 -*-
from constants import centenas, dezenas_especiais, dezenas, unidades, \
    extensoes_plural, CONCATENADOR_E, ZERO, CEM, extensoes_singular, MENOS, MIL


def digitos_multiplo_de_3(digitos):
    if len(digitos) % 3 == 0:
        return digitos
    return digitos_multiplo_de_3("0" + digitos)


def eh_dezena_especial(dezena):
    return 11 <= int(dezena) <= 19


def eh_diferente_de_zero(numero):
    return numero != 0


def numero_base_em_extenso(numero_com_tres_digitos):
    if int(numero_com_tres_digitos) == 0:
        return ZERO
    elif int(numero_com_tres_digitos) == 100:
        return CEM
    else:
        numero_por_extenso = ""
        c, d, u = [int(i) for i in numero_com_tres_digitos]
        numero_por_extenso += centenas[c]
        if c != 0 and eh_diferente_de_zero(d + u):
            numero_por_extenso = "%s %s " % (numero_por_extenso, CONCATENADOR_E)

        if eh_dezena_especial(numero_com_tres_digitos[1:]):
            numero_por_extenso += dezenas_especiais[u]
        else:
            numero_por_extenso += dezenas[d]
            if d > 1 and eh_diferente_de_zero(u):
                numero_por_extenso = "%s %s " % (numero_por_extenso, CONCATENADOR_E)
            numero_por_extenso += unidades[u]

    return numero_por_extenso


def add_numero_por_extenso(numero_por_extenso, numero_em_extenso_aux, numero):
    if int(numero) == 0 or numero_em_extenso_aux != ZERO:
        numero_por_extenso += numero_em_extenso_aux
    return numero_por_extenso


def add_extensao_milhar(numero_por_extenso, numero, total_de_centenas, indice_da_centena):
    if int(numero) == 0:
        extensao = ""
    elif int(numero) == 1:
        extensao = extensoes_singular[:total_de_centenas:][::-1][indice_da_centena]
        if extensao == MIL:
            numero_por_extenso = numero_por_extenso[:-3]
    else:
        extensao = extensoes_plural[:total_de_centenas:][::-1][indice_da_centena]

    if extensao:
        return ("%s %s" % (numero_por_extenso, extensao)).strip()
    return numero_por_extenso


def add_concatenador_e(numero_por_extenso, numero_com_tres_casas_decimais, restante_do_numero):
    if int(numero_com_tres_casas_decimais) != 0 and restante_do_numero and int(restante_do_numero) != 0:
        numero_por_extenso = "%s %s " % (numero_por_extenso, CONCATENADOR_E)
    return numero_por_extenso


def add_concatenador_negativo(numero_por_extenso, eh_negativo):
    if eh_negativo:
        numero_por_extenso = "%s %s" % (MENOS, numero_por_extenso)
    return numero_por_extenso


def eh_negativo(numero):
    return numero < 0


def converte_numero_inteiro_para_extenso(numero):
    numero = int(numero)
    r = add_concatenador_negativo("", eh_negativo(numero))

    numero = str(abs(numero))
    numero_padronizado = digitos_multiplo_de_3(numero)
    total_de_iteracao = len(numero_padronizado) / 3

    for i in range(total_de_iteracao):
        numero_com_tres_casas_decimais = numero_padronizado[i * 3:(i + 1) * 3]
        restante_do_numero = numero_padronizado[(i + 1) * 3:]

        numero_em_extenso_aux = numero_base_em_extenso(numero_com_tres_casas_decimais)
        r = add_numero_por_extenso(r, numero_em_extenso_aux, numero)
        r = add_extensao_milhar(r, numero_com_tres_casas_decimais, total_de_iteracao, i)
        r = add_concatenador_e(r, numero_com_tres_casas_decimais, restante_do_numero)

    return r

#
# while True:
#     numero = raw_input("Digite um numero: ")
#     if "-5" in numero:
#         break
#     print converte_numero_inteiro_para_extenso(numero)
