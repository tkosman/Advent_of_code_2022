with open('input.txt', 'r') as file:
    lines = file.readlines()

grid =[]



for line in lines:
    linia = line.strip()
    droga = [x[0] for x in linia]
    grid.append(droga)

def is_visible(x, y):
    bot = True
    top = True
    right = True
    left = True
    # #is visible from top
    for i in range(0, x):
        # print("top: ", i, y, "TO ",grid[i][y])
        if grid[i][y] >= grid[x][y]:
            top = False
    for i in range(len(grid) - 1, x, -1):
        if grid[i][y] >= grid[x][y]:
            # print("bot ", i, y, "TO ",grid[i][y])
            bot = False
    #is visible from left
    for i in range(0, y):
        if grid[x][i] >= grid[x][y]:
            # print("left: ", x, i, "TO ",grid[x][i])
            left = False    
     #is visible from right
    for i in range(len(grid) - 1, y, -1):
        if grid[x][i] >= grid[x][y]:
            # print("right: ", x, i, "TO ",grid[x][i])
            right = False
    
    if top == bot == right == left == False:
        return False
    return True

score = 4 * len(grid) - 4

for x in range(1, len(grid)-1):
    for y in range(1, len(grid)-1):
        if is_visible(x, y):
            score += 1
print(score)

