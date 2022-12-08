with open('input.txt', 'r') as file:
    lines = file.readlines()

score = 0
i = 0

for line in lines:
    i = i + 1
    section1, section2 = line.strip().split(",")
    elf1_start, elf1_end = section1.split("-")
    elf2_start, elf2_end = section2.split("-")

    #wszedzie inty musza byc
    if int(elf1_start) <= int(elf2_start) <= int(elf1_end) or int(elf1_start) <= int(elf2_end) <= int(elf1_end):
        score += 1
        print(i)

print(score)