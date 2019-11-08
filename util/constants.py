# coding=utf-8
unidades = ("", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove")
dezenas = ("", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa")
dezenas_especiais = ("", "onze", "doze", "treze", "cartoze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove")
centenas = ("", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seicentos", "setecentos", "oitocentos",
            "novecentos")
extensoes_singular = ("", "mil", "milhao")
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
MESSAGEM_ERRO_FORA_DO_LIMITE = u"Só é aceitado números inteiros entre %d e %d." % (LIMITE_MINIMO, LIMITE_MAXIMO)
MESSAGEM_ERRO_NUMERO_NAO_INTEIRO = u"O valor recebido não é um inteiro."
