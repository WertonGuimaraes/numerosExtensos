# -*- coding: utf-8 -*-
from util.constants import centenas, dezenas_especiais, dezenas, unidades, \
    extensoes_plural, CONCATENADOR_E, ZERO, CEM, extensoes_singular, MENOS, MIL
from util.util_check import eh_diferente_de_zero, eh_dezena_especial, digitos_multiplo_de_3, eh_negativo


class Numero(object):

    def __init__(self, numero):
        self.numero = int(numero)
        self.numero_extenso = self.converte_numero_inteiro_para_extenso()

    def _add_numero_por_extenso(self, numero_em_extenso_aux):
        if self.numero == 0 or numero_em_extenso_aux != ZERO:
            self.numero_extenso += numero_em_extenso_aux

    def _add_extensao_milhar(self, numero, total_de_centenas, indice_da_centena):
        if int(numero) == 0:
            extensao = ""
        elif int(numero) == 1:
            extensao = extensoes_singular[:total_de_centenas:][::-1][indice_da_centena]
            if extensao == MIL:
                self.numero_extenso = self.numero_extenso[:-3]
        else:
            extensao = extensoes_plural[:total_de_centenas:][::-1][indice_da_centena]

        if extensao:
            self.numero_extenso = ("%s %s" % (self.numero_extenso, extensao)).strip()

    def _add_concatenador_e(self, numero_com_tres_casas_decimais, restante_do_numero):
        if int(numero_com_tres_casas_decimais) != 0 and restante_do_numero and int(restante_do_numero) != 0:
            self.numero_extenso = "%s %s " % (self.numero_extenso, CONCATENADOR_E)

    def _add_concatenador_negativo(self, eh_negativo):
        if eh_negativo:
            self.numero_extenso = "%s %s" % (MENOS, self.numero_extenso)

    def numero_base_em_extenso(self, numero_com_tres_digitos):
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

    def converte_numero_inteiro_para_extenso(self):
        self.numero_extenso = ""
        self._add_concatenador_negativo(eh_negativo(self.numero))
        numero_absoluto = str(abs(self.numero))
        numero_padronizado = digitos_multiplo_de_3(numero_absoluto)
        total_de_iteracao = len(numero_padronizado) / 3

        for i in range(total_de_iteracao):
            numero_com_tres_casas_decimais = numero_padronizado[i * 3:(i + 1) * 3]
            restante_do_numero = numero_padronizado[(i + 1) * 3:]

            numero_em_extenso_aux = self.numero_base_em_extenso(numero_com_tres_casas_decimais)
            self._add_numero_por_extenso(numero_em_extenso_aux)
            self._add_extensao_milhar(numero_com_tres_casas_decimais, total_de_iteracao, i)
            self._add_concatenador_e(numero_com_tres_casas_decimais, restante_do_numero)
        return self.numero_extenso

#
# while True:
#     numero = raw_input("Digite um numero: ")
#     if "-5" in numero:
#         break
#     print converte_numero_inteiro_para_extenso(numero)
