with open('input.txt', 'r') as file:
    lines = file.readlines()

screen = []
for _ in range(0, 240):
    screen.append('$')


sprite_position = 0
cycle = 0

def show_sprite_position():
    print("Sprite position: ", end=" ")
    for x in range(0, 40):
        if x == sprite_position or x == sprite_position + 1 or x == sprite_position + 2:
            print("#", end="")
        else:
            print(".", end="")
    print("\n______", end="\n\n")

def show_sprite():
    for i in range(1, 241):
        if i % 40 == 0:
            print(screen[i - 1], end="")
            print("")
        else:
            print(screen[i - 1], end="")
    print("\n______", end="\n\n")

for line in lines:
    komenda = line.strip()
    if 'noop' in komenda:
        show_sprite_position()
        if sprite_position == cycle % 40 or sprite_position + 1 == cycle % 40 or sprite_position + 2 == cycle % 40:
                screen[cycle] = '#'
        else:
            screen[cycle] = '.'
        cycle += 1
        show_sprite()
    else:
        show_sprite_position()
        nudy, val = komenda.split(" ")
        for _ in range(0, 2):
            if sprite_position == cycle % 40 or sprite_position + 1 == cycle % 40 or sprite_position + 2 == cycle % 40:
                screen[cycle] = '#'
            else:
                screen[cycle] = '.'
            cycle += 1
            show_sprite()
        sprite_position += int(val)