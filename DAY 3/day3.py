with open('input.txt', 'r') as file:
    lines = file.readlines()

score = 0

for line in lines:
    rucksack = line.strip()
    comp1 = rucksack[:int(len(rucksack)/2)]
    comp2 = rucksack[int(len(rucksack)/2):]
    for letter in comp1:
        if letter in comp2:
            if(ord(letter) > 95):
                score += ord(letter) - 96
            else:
                score += ord(letter) - 38
            break
print(score)