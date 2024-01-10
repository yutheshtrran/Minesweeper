# Minesweeper

import random

class Minesweeper:
    def __init__(self, size, mines_count):
        self.grid_size = size
        self.num_mines = mines_count
        self.field = [['c' for _ in range(size)] for _ in range(size)]
        self.mines = [[False for _ in range(size)] for _ in range(size)]
        self.flags_remaining = mines_count

    def display_field():
       

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

