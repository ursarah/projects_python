def leiaInt(text):
    while True:
        a= input(text)
        if a.isnumeric():
            return a
        else:
            print('ERRO! Digite novamente um numero inteiro.\n')
n = leiaInt('Escreva um numero: ')
print('\n'+'-='*30)
print(f'Voce digitou: {n}')