# -*- coding: utf-8 -*-

def exchange_calculator(ammount):

    chilean_rate = 679.36
    return chilean_rate * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte dolares a pesos Chilenos')
    print('')

    ammount = float(input('Ingrese la cantidad de dolares que desea cambiar a pesos Chilenos: '))

    result = int(exchange_calculator(ammount))

    print('${} dolares son ${} pesos Chilenos'.format(ammount,result))
    print('')

if __name__ == "__main__":
    run()
    print('Final')