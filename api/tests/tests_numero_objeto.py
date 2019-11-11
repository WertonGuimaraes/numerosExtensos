# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from api.numero import Numero


class NumeroBaseExtensoTestCase(TestCase):
    def setUp(self):
        super(NumeroBaseExtensoTestCase, self).setUp()
        self.numero_extenso_object = Numero(0)

    def _assertEqualsNumeroETraducao(self, numero, traducao):
        numero_convertido = self.numero_extenso_object.numero_base_em_extenso(numero)
        self.assertEqual(traducao, numero_convertido)

    def test_numero_base_em_extenso__numero_zero(self):
        numero = "000"
        traducao = "zero"
        self._assertEqualsNumeroETraducao(numero, traducao)

    #
    def test_numero_base_em_extenso__numero_um(self):
        numero = "001"
        traducao = "um"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_10(self):
        numero = "010"
        traducao = "dez"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_12(self):
        numero = "012"
        traducao = "doze"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_25(self):
        numero = "025"
        traducao = "vinte e cinco"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_100(self):
        numero = "100"
        traducao = "cem"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_105(self):
        numero = "105"
        traducao = "cento e cinco"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_115(self):
        numero = "115"
        traducao = "cento e quinze"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_125(self):
        numero = "125"
        traducao = "cento e vinte e cinco"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_300(self):
        numero = "300"
        traducao = "trezentos"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_307(self):
        numero = "307"
        traducao = "trezentos e sete"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_316(self):
        numero = "316"
        traducao = "trezentos e dezesseis"
        self._assertEqualsNumeroETraducao(numero, traducao)

    def test_numero_base_em_extenso__numero_365(self):
        numero = "365"
        traducao = "trezentos e sessenta e cinco"
        self._assertEqualsNumeroETraducao(numero, traducao)


class NumeroExtensoTestCase(TestCase):
    def setUp(self):
        super(NumeroExtensoTestCase, self).setUp()
        self.numero_extenso_object = Numero(0)
        self.numero_extenso_object.numero_extenso = ""

    def test_converte_numero_inteiro_para_extenso__numero_12035(self):
        self.numero_extenso_object.numero = 12035
        numero_em_extenso = self.numero_extenso_object.converte_numero_inteiro_para_extenso()
        self.assertEqual("doze mil e trinta e cinco", numero_em_extenso)

    def test_converte_numero_inteiro_para_extenso__numero_menos_12035(self):
        self.numero_extenso_object.numero = -12035
        numero_em_extenso = self.numero_extenso_object.converte_numero_inteiro_para_extenso()
        self.assertEqual("menos doze mil e trinta e cinco", numero_em_extenso)


class ConcatenacaoExtensoTestCase(TestCase):
    def setUp(self):
        super(ConcatenacaoExtensoTestCase, self).setUp()
        self.numero_extenso_object = Numero(0)
        self.numero_extenso_object.numero_extenso = ""

    def test_add_numero_por_extenso__numero_0(self):
        self.numero_extenso_object.numero = 0
        self.numero_extenso_object._add_numero_por_extenso("zero")
        self.assertEqual("zero", self.numero_extenso_object.numero_extenso)

    # Esse teste consiste em verificar se o nome zero eh removido
    # [001, 000] - NAO deve ser retornado "mil zero", mas deve ser "mil"
    def test_add_numero_por_extenso__numero_1000(self):
        self.numero_extenso_object.numero = 1000
        self.numero_extenso_object.numero_extenso = "mil"
        self.numero_extenso_object._add_numero_por_extenso("zero")
        self.assertEqual("mil", self.numero_extenso_object.numero_extenso)

    def test_add_numero_por_extenso__numero_1010(self):
        self.numero_extenso_object.numero = 1010
        self.numero_extenso_object.numero_extenso = "mil"
        self.numero_extenso_object._add_numero_por_extenso("dez")
        self.assertEqual("mildez", self.numero_extenso_object.numero_extenso)

    def test_add_extensao_milhar__na_centena_zerada__000(self):
        centenas = ["001", "000", "001"]
        indice = 1
        self.numero_extenso_object._add_extensao_milhar(centenas[indice], len(centenas), indice)
        self.assertEqual("", self.numero_extenso_object.numero_extenso)

    def test_add_extensao_milhar__na_centena_de_milhoes_igual_a_mil__1000(self):
        centenas = ["001", "000"]
        indice = 0
        self.numero_extenso_object.numero_extenso = "um"
        self.numero_extenso_object._add_extensao_milhar(centenas[indice], len(centenas), indice)
        self.assertEqual("mil", self.numero_extenso_object.numero_extenso)

    def test_add_extensao_milhar__na_centena_de_milhoes_igual_a_um__001(self):
        centenas = ["001", "000", "000"]
        indice = 0
        self.numero_extenso_object.numero_extenso = "um"
        self.numero_extenso_object._add_extensao_milhar(centenas[indice], len(centenas), indice)
        self.assertEqual("um milhão", self.numero_extenso_object.numero_extenso)

    def test_add_extensao_milhar__na_centena_de_milhoes_maior_que_um__002(self):
        centenas = ["002", "000", "000"]
        indice = 0
        self.numero_extenso_object.numero_extenso = "dois"
        self.numero_extenso_object._add_extensao_milhar(centenas[indice], len(centenas), indice)
        self.assertEqual("dois milhoes", self.numero_extenso_object.numero_extenso)

    def test_add_concatenador_e__centena_zerada_nao_deve_ter_conector(self):
        centenas = ["000", "002"]
        self.numero_extenso_object._add_concatenador_e(centenas[0], centenas[1])
        self.assertEqual("", self.numero_extenso_object.numero_extenso)

    def test_add_concatenador_e__a_ultima_centena_nao_deve_ter_conector(self):
        centenas = ["001", "002"]
        self.numero_extenso_object._add_concatenador_e(centenas[1], "")
        self.assertEqual("", self.numero_extenso_object.numero_extenso)

    def test_add_concatenador_e__as_proximas_centenas_zeradas_nao_deve_ter_conector(self):
        centenas = ["001", "000"]
        self.numero_extenso_object._add_concatenador_e(centenas[0], "")
        self.assertEqual("", self.numero_extenso_object.numero_extenso)

    def test_add_concatenador_e__duas_centenas_nao_zeradas_deve_ter_conector(self):
        centenas = ["001", "002"]
        self.numero_extenso_object._add_concatenador_e(centenas[0], centenas[1])
        self.assertEqual(" e ", self.numero_extenso_object.numero_extenso)
