# a<16: não vota
# 16 <= a < 18 and a > 70: Opcional
# a>=18: Obrigatorio

def votos(ano):
    idade=2022-ano
    if idade < 16:
        return f'Com {idade} anos o voto é nulo'
    elif 70> idade >= 18:
        return f'Com {idade} anos o voto é obrigatorio'
    else:
        return f'Com {idade} anos o voto é opcional'

       
a = int(input('Digite seu ano de nascimento: '))
print(votos(a))
