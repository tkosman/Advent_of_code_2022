with open('input.txt', 'r') as file:
    lines = file.readlines()
stacks = [
['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
['L', 'P', 'T', 'V', 'H', 'C', 'G'],
['D', 'C', 'Z', 'F'],
['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
['P', 'W', 'C'],
['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
['V', 'W', 'G', 'B', 'D'],
['N', 'J', 'S', 'Q', 'H', 'W'],
['R', 'C', 'Q', 'F', 'S', 'L', 'V']
]
# stacks =[
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]

read = False
for line in lines:
    if read:
        move, times, z, where_pop_not, do, where_append_not = line.strip().split(" ")
        where_pop = int(where_pop_not)
        where_append = int(where_append_not)
        where_pop -= 1
        where_append -= 1
        times_new = -int(times) 
        for i in range(times_new, 0, 1):
            stacks[where_append].append(stacks[where_pop][i])
            del stacks[where_pop][i]
                     

    if line.strip() == "":
        read = True

for i in range(0, len(stacks)):
    print(stacks[i][-1], end="")