

def run():
    counter = 0
    with open('aleph.txt','r',encoding='UTF8') as f:
        #print(f.readlines())
        for line in f:
            counter += line.count('Beatriz')
    print('Beatriz se encuentra {} en el texto'.format(counter))

if __name__ == "__main__":
    run()

