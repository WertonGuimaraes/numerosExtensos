# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.test import TestCase
from httpstatus import OK, BAD_REQUEST
from django.test import Client

from util.constants import LIMITE_MAXIMO, LIMITE_MINIMO


class NumeroParaExtensoRequestTestCase(TestCase):

    def test_decorator_valida_numero_inteiro(self):
        numero = "1"
        mensagem_esperada = {"extenso": "um"}
        response = Client().get("/" + numero)
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(OK, response.status_code)

    def test_decorator_valida_numero_inteiro_com_uma_letra(self):
        numero = "1a"
        mensagem_esperada = {"erro": "O valor recebido não é um inteiro."}
        response = Client().get("/" + str(numero))
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(BAD_REQUEST, response.status_code)

    def test_decorator_valida_limite_numero_menor_que_o_minimo(self):
        numero = LIMITE_MINIMO - 1
        mensagem_esperada = {"erro": "Só são aceitos números inteiros entre %s e %s." % (LIMITE_MINIMO, LIMITE_MAXIMO)}
        response = Client().get("/" + str(numero))
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(BAD_REQUEST, response.status_code)

    def test_decorator_valida_limite_numero_igual_ao_minimo(self):
        numero = LIMITE_MINIMO
        mensagem_esperada = {"extenso": "menos noventa e nove mil e novecentos e noventa e nove"}
        response = Client().get("/" + str(numero))
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(OK, response.status_code)

    def test_decorator_valida_limite_numero_positivo_dentro_do_limite(self):
        numero = "92700"
        mensagem_esperada = {"extenso": "noventa e dois mil e setecentos"}
        response = Client().get("/" + str(numero))
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(OK, response.status_code)

    def test_decorator_valida_limite_numero_negativo_dentro_do_limite(self):
        numero = "-92700"
        mensagem_esperada = {"extenso": "menos noventa e dois mil e setecentos"}
        response = Client().get("/" + str(numero))
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(OK, response.status_code)

    def test_decorator_valida_limite_numero_igual_ao_maximo(self):
        numero = LIMITE_MAXIMO
        mensagem_esperada = {"extenso": "noventa e nove mil e novecentos e noventa e nove"}
        response = Client().get("/" + str(numero))
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(OK, response.status_code)

    def test_decorator_valida_limite_numero_maior_que_o_maximo(self):
        numero = LIMITE_MAXIMO + 1
        mensagem_esperada = {"erro": "Só são aceitos números inteiros entre %s e %s." % (LIMITE_MINIMO, LIMITE_MAXIMO)}
        response = Client().get("/" + str(numero))
        self.assertEqual(mensagem_esperada, json.loads(response.content))
        self.assertEqual(BAD_REQUEST, response.status_code)
