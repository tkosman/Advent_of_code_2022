with open('input.txt', 'r') as file:
    lines = file.readlines()

score = 0
i = 0
    

for line in lines:
    if i == 0:
        rucksack1 = line.strip()
        i += 1
    elif i == 1:
        rucksack2 = line.strip()
        i += 1
    elif i == 2:
        rucksack3 = line.strip()
        i = 0
        for letter in rucksack1:
            if letter in rucksack2 and letter in rucksack3:
                if(ord(letter) > 95):
                    score += ord(letter) - 96
                else:
                    score += ord(letter) - 38
                break
            
        
print(score)