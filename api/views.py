# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs

from django.http import JsonResponse
from httpstatus import BAD_REQUEST, OK

from util.constants import LIMITE_MINIMO, LIMITE_MAXIMO, EXTENSO
from util.erro import NAO_INTEIRO, FORA_DO_LIMITE
from util.main import converte_numero_inteiro_para_extenso


def valida_numero(func):
    def wrapper(request, numero):
        try:
            int(numero)
        except ValueError:
            return JsonResponse(NAO_INTEIRO, status=BAD_REQUEST, json_dumps_params={'ensure_ascii': False})
        return func(request, numero)

    return wrapper


def valida_limite(func):
    def wrapper(request, numero):
        if LIMITE_MAXIMO < int(numero) or int(numero) < LIMITE_MINIMO:
            return JsonResponse(FORA_DO_LIMITE, status=BAD_REQUEST, json_dumps_params={'ensure_ascii': False})
        return func(request, numero)

    return wrapper


@valida_numero
@valida_limite
def index(request, numero=None):
    numero_em_extenso = converte_numero_inteiro_para_extenso(numero)
    return JsonResponse({EXTENSO: numero_em_extenso}, status=OK)
