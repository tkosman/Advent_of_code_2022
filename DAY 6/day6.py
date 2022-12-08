import sys

with open('input.txt', 'r') as file:
    lines = file.readlines()

def ma_powtorzenia(x):
    for i in range(0, len(x)):
        score = 0
        for j in range(0, len(x)):
            if x[i] == x[j]:
                score += 1
        if score > 1:
            return True
    return False

for line in lines:
    szyfr = line.strip()
    
for i in range(4, len(szyfr)):
    do_sprawdzenia = szyfr[i-4:i]
    if ma_powtorzenia(do_sprawdzenia) == False:
        print(i)
        break
        