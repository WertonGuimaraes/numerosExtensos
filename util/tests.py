# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from util.main import digitos_multiplo_de_3, eh_dezena_especial, eh_diferente_de_zero, numero_base_em_extenso, \
    add_numero_por_extenso, add_extensao_milhar, add_concatenador_e, converte_numero_inteiro_para_extenso


class NumeroPadronizadoTestCase(TestCase):
    def test_padronizar_digitos__total_de_digitos_multiplo_de_tres(self):
        digitos = "123"
        digitos_padronizados = digitos_multiplo_de_3(digitos)
        self.assertEqual(digitos, digitos_padronizados)

    def test_padronizar_digitos__total_de_digitos_nao_multiplo_de_tres(self):
        digitos = "3125"
        digitos_padronizados = digitos_multiplo_de_3(digitos)
        self.assertEqual("00" + digitos, digitos_padronizados)


class IntervaloTestCase(TestCase):
    def test_dezena_especial__numero_inferior_ao_intervalo(self):
        numero = 10
        self.assertFalse(eh_dezena_especial(numero))

    def test_dezena_especial__numero_inferior_dentro_do_intervalo(self):
        numero = 11
        self.assertTrue(eh_dezena_especial(numero))

    def test_dezena_especial__numero_dentro_do_intervalo(self):
        numero = 15
        self.assertTrue(eh_dezena_especial(numero))

    def test_dezena_especial__numero_superior_dentro_do_intervalo(self):
        numero = 19
        self.assertTrue(eh_dezena_especial(numero))

    def test_dezena_especial__numero_superior_ao_intervalo(self):
        numero = 20
        self.assertFalse(eh_dezena_especial(numero))

    def test_numero_diferente_de_zero__numero_zero(self):
        numero = 0
        self.assertFalse(eh_diferente_de_zero(numero))

    def test_numero_diferente_de_zero__numero_zero_negativo(self):
        numero = -0
        self.assertFalse(eh_diferente_de_zero(numero))

    def test_numero_diferente_de_zero__numero_diferente_de_zero(self):
        numero = 1
        self.assertTrue(eh_diferente_de_zero(numero))


class NumeroExtensoTestCase(TestCase):
    def test_numero_base_em_extenso__numero_zero(self):
        numero = "000"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("zero", numero_em_extenso)

    def test_numero_base_em_extenso__numero_um(self):
        numero = "001"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("um", numero_em_extenso)

    def test_numero_base_em_extenso__numero_10(self):
        numero = "010"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("dez", numero_em_extenso)

    def test_numero_base_em_extenso__numero_12(self):
        numero = "012"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("doze", numero_em_extenso)

    def test_numero_base_em_extenso__numero_25(self):
        numero = "025"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("vinte e cinco", numero_em_extenso)

    def test_numero_base_em_extenso__numero_100(self):
        numero = "100"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("cem", numero_em_extenso)

    def test_numero_base_em_extenso__numero_105(self):
        numero = "105"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("cento e cinco", numero_em_extenso)

    def test_numero_base_em_extenso__numero_115(self):
        numero = "115"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("cento e quinze", numero_em_extenso)

    def test_numero_base_em_extenso__numero_125(self):
        numero = "125"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("cento e vinte e cinco", numero_em_extenso)

    def test_numero_base_em_extenso__numero_300(self):
        numero = "300"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("trezentos", numero_em_extenso)

    def test_numero_base_em_extenso__numero_307(self):
        numero = "307"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("trezentos e sete", numero_em_extenso)

    def test_numero_base_em_extenso__numero_316(self):
        numero = "316"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("trezentos e dezeseis", numero_em_extenso)

    def test_numero_base_em_extenso__numero_365(self):
        numero = "365"
        numero_em_extenso = numero_base_em_extenso(numero)
        self.assertEqual("trezentos e sessenta e cinco", numero_em_extenso)

    def test_converte_numero_inteiro_para_extenso__numero_12035(self):
        numero = "12035"
        numero_em_extenso = converte_numero_inteiro_para_extenso(numero)
        self.assertEqual("doze mil e trinta e cinco", numero_em_extenso)


class ConcatenacaoExtensoTestCase(TestCase):
    def test_add_numero_por_extenso__numero_0(self):
        numero_em_extenso = add_numero_por_extenso("", "zero", "0")
        self.assertEqual("zero", numero_em_extenso)

    # Esse teste consiste em verificar se o nome zero eh removido
    # [001, 000] - NAO deve ser retornado "um mil zero", mas deve ser "um mil"
    def test_add_numero_por_extenso__numero_1000(self):
        numero_em_extenso = add_numero_por_extenso("um mil ", "zero", "1000")
        self.assertEqual("um mil ", numero_em_extenso)

    def test_add_numero_por_extenso__numero_1010(self):
        numero_em_extenso = add_numero_por_extenso("um mil ", "dez", "1010")
        self.assertEqual("um mil dez", numero_em_extenso)

    def test_add_extensao_milhar__na_centena_zerada__000(self):
        centenas = [001, 000, 001]
        indice = 1
        extensao = add_extensao_milhar("", centenas[indice], len(centenas), indice)
        self.assertEqual("", extensao)

    def test_add_extensao_milhar__na_centena_de_milhoes_igual_a_um__001(self):
        centenas = ["001", "000", "000"]
        indice = 0
        extensao = add_extensao_milhar("", centenas[indice], len(centenas), indice)
        self.assertEqual(" milhao", extensao)

    def test_add_extensao_milhar__na_centena_de_milhoes_maior_que_um__002(self):
        centenas = ["002", "000", "000"]
        indice = 0
        extensao = add_extensao_milhar("", centenas[indice], len(centenas), indice)
        self.assertEqual(" milhoes", extensao)

    def test_add_concatenador_e__centena_zerada_nao_deve_ter_conector(self):
        centenas = ["000", "002"]
        extensao = add_concatenador_e("", centenas[0], centenas[1])
        self.assertEqual("", extensao)

    def test_add_concatenador_e__a_ultima_centena_nao_deve_ter_conector(self):
        centenas = ["001", "002"]
        extensao = add_concatenador_e("", centenas[1], "")
        self.assertEqual("", extensao)

    def test_add_concatenador_e__as_proximas_centenas_zeradas_nao_deve_ter_conector(self):
        centenas = ["001", "000"]
        extensao = add_concatenador_e("", centenas[0], "")
        self.assertEqual("", extensao)

    def test_add_concatenador_e__duas_centenas_nao_zeradas_deve_ter_conector(self):
        centenas = ["001", "002"]
        extensao = add_concatenador_e("", centenas[0], centenas[1])
        self.assertEqual(" e ", extensao)
