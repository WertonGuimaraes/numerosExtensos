# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views import View
from httpstatus import BAD_REQUEST, OK
from django.views.generic import ListView

from util.constants import LIMITE_MINIMO, LIMITE_MAXIMO, EXTENSO
from util.erro import NAO_INTEIRO, FORA_DO_LIMITE
from api.numero import Numero


def valida_numero(func):
    def wrapper(self, request, numero):
        try:
            int(numero)
        except ValueError:
            return JsonResponse(NAO_INTEIRO, status=BAD_REQUEST, json_dumps_params={'ensure_ascii': False})
        return func(self, request, numero)

    return wrapper


def valida_limite(func):
    def wrapper(self, request, numero):
        if LIMITE_MAXIMO < int(numero) or int(numero) < LIMITE_MINIMO:
            return JsonResponse(FORA_DO_LIMITE, status=BAD_REQUEST, json_dumps_params={'ensure_ascii': False})
        return func(self, request, numero)

    return wrapper


class NumeroView(View):
    @valida_numero
    @valida_limite
    def get(self, request, numero, *args, **kwargs):
        numero = Numero(numero)
        return JsonResponse({EXTENSO: numero.numero_extenso}, status=OK, json_dumps_params={'ensure_ascii': False})
