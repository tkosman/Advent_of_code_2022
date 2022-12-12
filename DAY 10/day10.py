with open('input.txt', 'r') as file:
    lines = file.readlines()

cycles = 0
x = 1
strength = 0
cycle_before = -1

def test_cycles():
    if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
        global strength, cycle_before
        if cycles != cycle_before:
            strength += x * cycles
            print(cycles,x, x * cycles)
        cycle_before = cycles

for line in lines:
    if line[:2] == 'no':
        test_cycles()
        cycles +=1
    else:
        comend, value = line.strip().split(" ")
        cycles += 1
        test_cycles()
        cycles += 1
        test_cycles()
        x += int(value)

print(strength)