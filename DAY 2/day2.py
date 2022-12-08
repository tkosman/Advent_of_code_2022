def wynik(wrog, ja):
    #remis
    if (wrog == 'A' and ja == 'X') or (wrog == 'B' and ja == 'Y') or (wrog == 'C' and ja == 'Z'):
        return 'remis'
    #ja win
    elif (wrog == 'A' and ja == 'Y') or (wrog == 'B' and ja == 'Z') or (wrog == 'C' and ja == 'X'):
        return 'win'
    #ja lost
    else:
        return 'lost'

def punkty(znak):
    if znak == 'X':
        return 1
    elif znak == 'Y':
        return 2
    elif znak == 'Z':
        return 3

with open('input.txt', 'r') as file:
    lines = file.readlines()

score = 0;

for line in lines:
    wrog, ja = line.strip().split(" ")
    if wynik(wrog, ja) == 'win':
        score += 6
        score += punkty(ja)
    elif wynik(wrog, ja) == 'remis':
        score += 3
        score += punkty(ja)
    elif wynik(wrog, ja) == 'lost':
        score += punkty(ja)

print(score)