unidades = ["", "um", "dois","tres", "quatro","cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
dezenas_especiais = ["", "onze", "doze", "treze", "cartoze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove"]
centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seicentos", "oitocentos", "novecentos"]

extensoes_singular = ["", " mil", " milhao"]
extensoes_plural = ["", " mil", " milhoes"]

def digitos_multiplo_de_3(digitos):
    if len(digitos)%3 == 0:
        return digitos
    return digitos_multiplo_de_3("0" + digitos)

def separa_em_centenas(string):
    #import re
    #re.findall('...', 'string')

    #from textwrap import wrap
    #wrap(string, 3)

    return [string[i:i+3] for i in range(0, len(string), 3)]

def eh_dezena_especial(dezena):
    return 11 <= int(dezena) <= 19

def ainda_exite_numero(numero):
    return numero != 0

def numero_em_extenso(numero):
    if int(numero) == 0:
        return "zero"
    elif int(numero) == 100:
        return "cem"
    else:
        numero_por_extenso = ""
        c, d, u = [int(i) for i in numero]
        numero_por_extenso += centenas[c] if c != 0 else ""
        numero_por_extenso += " e " if c != 0 and ainda_exite_numero(d+u) else ""

        if eh_dezena_especial(numero[1:]):
            numero_por_extenso += dezenas_especiais[u]
        else:
            numero_por_extenso += dezenas[d] if d != 0 else ""
            numero_por_extenso += " e " if d > 1 and ainda_exite_numero(u) else ""
            numero_por_extenso += unidades[u] if u != 0 else ""

    return numero_por_extenso

def extensao(numero, total_de_centenas):
    if int(numero) == 0:
        extensao = ""
    elif int(numero) == 1:
        extensao = extensoes_singular[:total_de_centenas:][::-1][i]
    else:
        extensao = extensoes_plural[:total_de_centenas:][::-1][i]
    return extensao


while True:
    r = ""
    entrada = str(int(raw_input("Digite um numero: ")))
    if "-" in entrada:
        break

    entrada_padronizada = digitos_multiplo_de_3(entrada)
    entrada_padronizada_split = separa_em_centenas(entrada_padronizada)

    for i in range(len(entrada_padronizada_split)):
        n = entrada_padronizada_split[i]
        numero_em_extenso_aux = numero_em_extenso(n)
        r += "" if n != "" and numero_em_extenso_aux == "zero" and len(entrada_padronizada_split) != 1 else numero_em_extenso_aux

        r += extensao(n, len(entrada_padronizada_split))


        restante = entrada_padronizada[(i + 1) * 3:]
        r += " e " if numero_em_extenso_aux != "zero" and restante.strip() != "" and int(restante) != 0 else ""


    print r



