import os
sciezka = 'hah/'
file = open('input.txt', 'r')
plik = file.readlines()

co_robimy = ''

def position(slowo):
    for i in range(len(slowo) - 1, -1, -1):
        if slowo[i] == "/":
            return i

for i in range(0, len(plik)):
    komenda = plik[i].strip()
    if '$' in komenda:
        if '$ ls' in komenda:
            co_robimy = 'ls'
        elif '$ cd ..' in komenda:
            sciezka = sciezka[:position(sciezka)]
        elif '$ cd' in komenda:
            co_robimy = ''
            nudy1, nudy2, folderek = komenda.split(" ")
            sciezka += '/'
            sciezka += folderek
        continue
    
    if co_robimy == 'ls':
        if 'dir' in komenda:
            kosz, folder = komenda.split(" ")
            sciezka += '/'
            sciezka += folder
            os.makedirs(sciezka)
            sciezka = sciezka[:position(sciezka)]
        else:
            size, name = komenda.split(" ")
            sciezka += '/'
            sciezka += name
            f = open(sciezka,"wb")
            f.seek(int(size) - 1)
            f.write(b"\0")
            f.close()
            sciezka = sciezka[:position(sciezka)]





        
