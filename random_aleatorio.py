# -*- coding: utf-8 -*-
import random

def run():

    maxim_random = int(input('Ingresa el número maximo a buscar: '))
    number_found = False
    random_number = random.randint(0,maxim_random)

    while not number_found:
        number = int(input('Intenta un número: '))

        if number == random_number:
            print('Felicidades. Encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')

if __name__ == "__main__":
    run()