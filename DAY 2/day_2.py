score = 0;

def punkty(znak):
    if znak == 'rock':
        return 1
    elif znak == 'paper':
        return 2
    elif znak == 'scisors':
        return 3

with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    wrog, strategia = line.strip().split(" ")
    #przegrana
    if strategia == 'X':
        if wrog == 'A':
            score += 3
        elif wrog == 'B':
            score += 1
        elif wrog == 'C':
            score += 2
    #wygrana
    elif strategia == 'Z':
        score += 6
        if wrog == 'A':
            score += 2
        elif wrog == 'B':
            score += 3
        elif wrog == 'C':
            score += 1
    #remis
    elif strategia == 'Y':
        score += 3
        if wrog == 'A':
            score += 1
        elif wrog == 'B':
            score += 2
        elif wrog == 'C':
            score += 3
            
            

print(score)