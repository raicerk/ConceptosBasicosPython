# -*- coding: utf-8 -*-

def average_temperatures(temperatures):
    sum_of_temperatures = 0

    for temp in temperatures:
        sum_of_temperatures += float(temp)

    return sum_of_temperatures / len(temperatures)

    

if __name__ == "__main__":
    temperatures = [21, 24, 24, 22, 20, 23, 24]

    average = average_temperatures(temperatures)

    print('La temperatura promedio es: {}'.format(average))