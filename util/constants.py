# coding=utf-8
unidades = ("", "um", "dois", u"três", "quatro", "cinco", "seis", "sete", "oito", "nove")
dezenas = ("", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa")
dezenas_especiais = ("", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove")
centenas = ("", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos",
            "novecentos")
extensoes_singular = ("", "mil", u"milhão")
extensoes_plural = ("", "mil", "milhoes")

ZERO = "zero"
CEM = "cem"
MIL = "mil"

CONCATENADOR_E = "e"
MENOS = "menos"

LIMITE_MAXIMO = 99999
LIMITE_MINIMO = -99999

ERRO = "erro"
EXTENSO = "extenso"
MESSAGEM_ERRO_FORA_DO_LIMITE = u"Só são aceitos números inteiros entre %d e %d." % (LIMITE_MINIMO, LIMITE_MAXIMO)
MESSAGEM_ERRO_NUMERO_NAO_INTEIRO = u"O valor recebido não é um inteiro."
