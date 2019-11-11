def digitos_multiplo_de_3(digitos):
    if len(digitos) % 3 == 0:
        return digitos
    return digitos_multiplo_de_3("0" + digitos)


def eh_dezena_especial(dezena):
    return 11 <= int(dezena) <= 19


def eh_diferente_de_zero(numero):
    return numero != 0


def eh_negativo(numero):
    return numero < 0
