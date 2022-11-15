## Jogo da Forca

from time import sleep
from fuction import find_all_indexes,display_word



hangman_puppet = [
    """ 
         ___
        |   |
        |
        |
        |
      __|__
    """,
    """  
         ___
        |   |
        |   O
        |
        |
      __|__
    """,
    """  
         ___
        |   |
        |   O
        |   |
        |
      __|__
    """,
    """  
         ___
        |   |
        |   O
        |   |\_
        |
      __|__
    """,
    """
         ___
        |   |
        |   O
        | _/|\_
        |
      __|__
    """,
    """
         ___
        |   |
        |   O
        | _/|\_
        |    \_
      __|__
    """,
    """ 
         ___
        |   |
        |   O
        | _/|\_
        | _/ \_
      __|__
    """           
]


def start():  
  secret_word = input('Digite a palavra secreta: ')
  print('\n'*100)

    
    
  final_word = []
  wrong_guesses = []
  

  # Preencher array final_word com tracinhos
  # ['_', '_', '_', '_', '_', '_']
  for char in secret_word:
    char = '_'
    final_word.append(char)
  
  
  print(hangman_puppet[len(wrong_guesses)])
  
  while True:
    guess = input("Digite uma letra: ")


    if guess in secret_word:
      indexes = find_all_indexes(secret_word, guess)
      for index in indexes:
        final_word[index] = guess

    else:
      wrong_guesses.append(guess)
      print(f"Errou: {wrong_guesses}")
        
        
    print(hangman_puppet[len(wrong_guesses)])
    display_word(final_word)
          
    if len(wrong_guesses) == len(hangman_puppet)-1:
      print("\n\nVocê perdeu!!!\n\n")
      print(f'A palavra secreta era:')
      sleep(1)
      for p in secret_word:
        print(p, end='')
      break
          
    if secret_word == "".join(final_word):
      print("\n\nParabéns você adivinhou!!!\n\n")
      break