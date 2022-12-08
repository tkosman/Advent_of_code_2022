with open('input.txt', 'r') as file:
    lines = file.readlines()

score = 0
i = 0

for line in lines:
    section1, section2 = line.strip().split(",")
    elf1_start, elf1_end = section1.split("-")
    elf2_start, elf2_end = section2.split("-")

    #wszedzie inty musza byc
    if (elf1_start <= elf2_start and elf2_end <= elf1_end) or (elf2_start <= elf1_start and elf1_end <= elf2_end):
        print(elf1_start, elf1_end, elf2_start, elf2_end)
        score += 1

print(score)