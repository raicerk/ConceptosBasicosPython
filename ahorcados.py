# -*- coding_ utf-8 -*-

import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''','''

    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''    

    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''  

    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputados',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- * --- * ---')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word,tries)
        current_letter = str(input('Escoge una letra: '))

        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] ==  current_letter:
                letter_indexes.append(idx)

                


if __name__ == "__main__":
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()    
    