with open('tekst.txt', 'r') as file:
    lines = file.readlines()

top1 = 0
top2 = 0
top3 = 0
kal = 0

for line in lines:
    if line.strip():
        kal = kal + int(line.strip())
    else:
        if kal > top1:
            top3 = top2
            top2 = top1
            top1 = kal
        elif kal > top2:
            top3 = top2
            top2 = kal
        elif kal > top3:
            top3 = kal
        kal = 0
print(top1 + top2 + top3)