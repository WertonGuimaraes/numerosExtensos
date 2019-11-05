# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from api.main import converte_numero_inteiro_para_extenso


def index(request, number=None):
    return HttpResponse(converte_numero_inteiro_para_extenso(number))
