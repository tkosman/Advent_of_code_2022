with open('input.txt', 'r') as file:
    lines = file.readlines()

grid =[]

for line in lines:
    linia = line.strip()
    droga = [x[0] for x in linia]
    grid.append(droga)

def count_scenic(x, y):
    #count top
    top = 0
    for i in range(x - 1, -1, -1):
        top += 1 
        if grid[i][y] >= grid[x][y]:
            break
    #count bot
    bot = 0
    for i in range(x + 1, len(grid)): 
        bot += 1 
        if grid[i][y] >= grid[x][y]:
            break
    #count right
    right = 0
    for i in range(y + 1, len(grid)): 
        right += 1 
        if grid[x][i] >= grid[x][y]:
            break
    #count left
    left = 0
    for i in range(y - 1, -1, -1): 
        left += 1 
        if grid[x][i] >= grid[x][y]:
            break
    
    return top * bot * right * left

maks = 0

for x in range(0, len(grid)):
    for y in range(0, len(grid)):
        wynik = count_scenic(x, y)
        if wynik > maks:
            maks = wynik
print(maks)
        


