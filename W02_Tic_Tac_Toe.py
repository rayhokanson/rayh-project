# W02 Tick Tack Toe game
# Ray Hokanson 1-11-21

# for clear screen function
import os

# create empty list for grid
grid = []


# populate grid
for y in range(9):
    grid.append(y + 1)


player = "o"

def main():

    #clear screen
    cls() 

    #print grid
    print_grid(grid)    

    # set loop counter
    x = 0
    
    # set player
    player = "o"

    while x < 10:
        if player == "o":
            player = "x"
        else:
            player = "o"
    
        # get choice
        ans = prompt_for_turn(player)

        # assign chice to square
        check_choice(ans, player, grid)

        # print grid
        print_grid(grid)    

        # check to see if user won
        check = win(grid)
        if check == "done":
            break

        # increment counter
        x += 1

        # no winner
        if x > 10 and check != "done":
            print("\nDraw game.")
            break
    
    # end of game.
    print("\nGood Game")


def print_grid(grid):
    # Print grid on screen
    cls() # Clear screen before printing grid
    print(f"{grid[0]} | {grid[1]} | {grid[2]}")
    print(" - + - + -")
    print(f"{grid[3]} | {grid[4]} | {grid[5]}")
    print(" - + - + -")
    print(f"{grid[6]} | {grid[7]} | {grid[8]}")
    print()

def prompt_for_turn(player):
    # get input from player
    ans = input(f"{player}'s turn to choose a square (1-9): ")
    return ans

def check_choice(ans, player, grid):
    # assign chice to square
    if ans == "1":
        grid[0] = player
    elif ans == "2":
        grid[1] = player
    elif ans == "3":
        grid[2] = player
    elif ans == "4":
        grid[3] = player
    elif ans == "5":
        grid[4] = player
    elif ans == "6":
        grid[5] = player
    elif ans == "7":
        grid[6] = player
    elif ans == "8":
        grid[7] = player
    elif ans == "9":
        grid[8] = player


def win(grid):
    if grid[0] == grid[1] == grid[2]: # 1, 2, 3
        print("x wins")
        return "done"
    elif grid[3] == grid[4] == grid[5]: # 4, 5, 6
        print("x wins")
        return "done"
    elif grid[6] == grid[7] == grid[8]: # 7, 8, 9
        print("x wins")
        return "done"
    elif grid[0] == grid[4] == grid[8]: # 1, 5, 9
        print("x wins")
        return "done"
    elif grid[6] == grid[4] == grid[2]: # 7, 5, 3
        print("x wins")
        return "done"
    elif grid[0] == grid[3] == grid[6]: # 1, 4, 7
        print("x wins")
        return "done"
    elif grid[1] == grid[4] == grid[7]: # 2, 5, 8
        print("x wins")
        return "done"
    elif grid[2] == grid[5] == grid[8]: # 3, 6, 9
        print("x wins")
        return "done"

def cls(): # clear screen
    os.system('cls')

if __name__ == '__main__': 
    main()
