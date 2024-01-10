# Minesweeper

import random

class Minesweeper:
    def __init__(self, size, mines_count):
        self.grid_size = size
        self.num_mines = mines_count
        self.field = [['c' for _ in range(size)] for _ in range(size)]
        self.mines = [[False for _ in range(size)] for _ in range(size)]
        self.flags_remaining = mines_count

     def display_field(self, reveal_all=False):
        print("  " + " ".join([chr(65 + i) for i in range(self.grid_size)]))
        for i in range(self.grid_size):
            print(chr(65 + i), end=" ")
            for j in range(self.grid_size):
                cell_value = self.field[i][j]
                if reveal_all and self.mines[i][j]:
                    print('\033[91m' + 'M' + '\033[0m', end=" ")  # Red for revealed mines
                elif cell_value == 'F':
                    print('\033[93m' + cell_value + '\033[0m', end=" ")  # Yellow for flags
                elif cell_value == '.':
                    print('\033[94m' + cell_value + '\033[0m', end=" ")  # Blue for revealed empty cells
                elif cell_value.isdigit():
                    self.print_colored_number(int(cell_value))
                else:
                    print('\033[92m' + cell_value + '\033[0m', end=" ")  # Green for covered cells
            print()
       

    def print_colored_number():


    def place_mines():


    def reveal_location():


    def place_flag():


    def check_win():


    def count_adjacent_mines():


    def play_game():
        
              

if __name__ == "__main__":
    print("Choose the field:")
    print("1. 10-by-10 with 12 mines")
    print("2. 15-by-15 with 18 mines")
    print("3. 20-by-20 with 24 mines")

    choice = input("Enter the option number (1, 2, or 3): ")

    if choice == '1':
        game = Minesweeper(10, 12)
    elif choice == '2':
        game = Minesweeper(15, 18)
    elif choice == '3':
        game = Minesweeper(20, 24)
    else:
        print("Invalid choice. Exiting.")
        exit(0)

    game.play_game()


