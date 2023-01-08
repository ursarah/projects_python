tab = ["_","_","_",
       "_","_","_",
       "_","_","_"]
jogador_atual = "X"
ganhou = None
jogo = True
cont = 0
def print_tabuleiro(tab):
       print(tab[0]+' | '+tab[1]+' | '+tab[2])       
       print(tab[3]+' | '+tab[4]+' | '+tab[5])       
       print(tab[6]+' | '+tab[7]+' | '+tab[8])
def troca_jogador(cont):
       if cont%2 == 0 or cont==0:
              jogador_atual = 'X'
              return jogador_atual
       else:
              jogador_atual = '0'
              return jogador_atual
def ganhador_linha(tab):
       global ganhou
       if tab[0] == tab[1] == tab[2] and tab[1] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
       elif tab[3] == tab[4] == tab[5] and tab[3] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
       elif tab[6] == tab[7] == tab[8] and tab[6] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
def ganhador_coluna(tab):
       global ganhou
       if tab[0] == tab[3] == tab[6] and tab[0] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
       elif tab[1] == tab[4] == tab[7] and tab[1] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
       elif tab[2] == tab[5] == tab[8] and tab[2] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
def ganhador_diagonal(tab): 
       global ganhou      
       if tab[0] == tab[4] == tab[8] and tab[0] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
       elif tab[2] == tab[4] == tab[6] and tab[2] != "_":              
              ganhou = troca_jogador(cont)
              print(f'O Jogador {ganhou} é o vencedor')
              return True
print_tabuleiro(tab)
while jogo:
       print(f'Contagem: {cont}')
       pos = int(input('Digite uma posição de 1-9: '))
       if 0 < pos <= 9 and tab[pos-1] =="_":
              tab[pos-1] = troca_jogador(cont)
              print_tabuleiro(tab)
              if jogo == ganhador_linha(tab) or jogo == ganhador_coluna(tab) or jogo == ganhador_diagonal(tab):
                     break              
              cont+=1

       else:
              print('Digite novamente!') 
       if cont == 9 and ganhou == None:
              print('Jogo empatou')
              break