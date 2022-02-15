#VALIDAÇÃO
def valida_int(pergunta,min,max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
        return x


