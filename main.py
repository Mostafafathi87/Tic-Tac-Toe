grid = [" " for x in range(9)]
def print_grid():
    r1 = "| {} | {} | {} |".format(grid[0], grid[1], grid[2])
    r2 = "| {} | {} | {} |".format(grid[3], grid[4], grid[5])
    r3 = "| {} | {} | {} |".format(grid[6], grid[7], grid[8])


    print()
    print(r1)
    print(r2)
    print(r3)
    print()

def player_move(symbol):
    if symbol == "X":
        number = 1
    elif symbol == "O":
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if grid[choice - 1] == " ":
        grid[choice - 1] = symbol
    else:
        print()
        print("That space is already taken!")
def is_victory(icon):
    if (grid[0] == icon and grid[1] == icon and grid[2] == icon) or \
       (grid[3] == icon and grid[4] == icon and grid[5] == icon) or \
       (grid[6] == icon and grid[7] == icon and grid[8] == icon) or \
       (grid[0] == icon and grid[3] == icon and grid[6] == icon) or \
       (grid[1] == icon and grid[4] == icon and grid[7] == icon) or \
       (grid[2] == icon and grid[5] == icon and grid[8] == icon) or \
       (grid[0] == icon and grid[4] == icon and grid[8] == icon) or \
       (grid[2] == icon and grid[4] == icon and grid[6] == icon):
        return True
    else:
        return False
def is_draw():
    if " " not in grid:
        return True
    else:
        return False
while True:
    print_grid()
    player_move("X")
    print_grid()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_grid()
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break



