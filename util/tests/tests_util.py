# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

from util.util_check import digitos_multiplo_de_3, eh_dezena_especial, eh_diferente_de_zero, eh_negativo


class NumeroPadronizadoTestCase(TestCase):
    def test_padronizar_digitos__total_de_digitos_multiplo_de_tres(self):
        digitos = "123"
        digitos_padronizados = digitos_multiplo_de_3(digitos)
        self.assertEqual(digitos, digitos_padronizados)

    def test_padronizar_digitos__total_de_digitos_nao_multiplo_de_tres(self):
        digitos = "3125"
        digitos_padronizados = digitos_multiplo_de_3(digitos)
        self.assertEqual("00" + digitos, digitos_padronizados)


class IntervaloCheckTestCase(TestCase):
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


class NumerosNulosCheckTestCase(TestCase):
    def test_numero_diferente_de_zero__numero_zero(self):
        numero = 0
        self.assertFalse(eh_diferente_de_zero(numero))

    def test_numero_diferente_de_zero__numero_zero_negativo(self):
        numero = -0
        self.assertFalse(eh_diferente_de_zero(numero))

    def test_numero_diferente_de_zero__numero_diferente_de_zero(self):
        numero = 1
        self.assertTrue(eh_diferente_de_zero(numero))


class NumerosNegativosCheckTestCase(TestCase):
    def test_eh_negativo_numero_menor_que_zero(self):
        numero = -1
        self.assertTrue(eh_negativo(numero))

    def test_eh_negativo_numero_igual_a_zero(self):
        numero = 0
        self.assertFalse(eh_negativo(numero))

    def test_eh_negativo_numero_maior_que_zero(self):
        numero = 1
        self.assertFalse(eh_negativo(numero))
