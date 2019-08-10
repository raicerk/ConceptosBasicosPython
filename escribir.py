# -*- coding: utf-8 -*-

def run():
    with open('numeros.txt','w') as f:
        for num in range(0,9):
            f.write(str(num))
    #f.close()


if __name__ == "__main__":
    run()