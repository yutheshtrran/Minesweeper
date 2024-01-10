#Minesweeper

# Group Members
# 21/ENG/009 - A.Harishan
# 21/ENG/131 - S.Yutheshtrran
# 21/ENG/132 - S.Geerthiga

import random

class Minesweeper:

    # 21/ENG/131 - S.Yutheshtrran
    def __init__(self, size, mines_count):
        self.grid_size = size
        self.num_mines = mines_count
        self.field = [['c' for _ in range(size)] for _ in range(size)]
        self.mines = [[False for _ in range(size)] for _ in range(size)]
        self.flags_remaining = mines_count
    # 21/ENG/131 - S.Yutheshtrran
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

    # 21/ENG/132 - S.Geerthiga
    def print_colored_number(self, number):
        colors = {
            1: '\033[33m',  # Orange for 1
            2: '\033[95m',  # Pink for 2
            3: '\033[97m',  # White for 3
            4: '\033[94m',  # Blue for 4
            5: '\033[35m',  # Magenta for 5

        }
        print(colors.get(number, '') + str(number) + '\033[0m', end=" ")

    # 21/ENG/009 - A.Harishan
    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if not self.mines[row][col]:
                self.mines[row][col] = True
                mines_placed += 1
                
    # 21/ENG/132 - S.Geerthiga
    def reveal_location(self, row, col):
        if self.mines[row][col]:
            print("Game Over! You hit a mine.")
            self.field[row][col] = '\033[91m' + 'M' + '\033[0m' 
            self.display_field(reveal_all=True)  
            exit(0)

        if self.field[row][col] == 'c':
            adjacent_mines = self.count_adjacent_mines(row, col)
            if adjacent_mines == 0:
                self.field[row][col] = '.'
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_row, new_col = row + i, col + j
                        if 0 <= new_row < self.grid_size and 0 <= new_col < self.grid_size:
                            self.reveal_location(new_row, new_col)
            else:
                self.field[row][col] = str(adjacent_mines)
    # 21/ENG/131 - S.Yutheshtrran
    def place_flag(self, row, col):
        if self.field[row][col] == 'c':
            self.field[row][col] = 'F'
            self.flags_remaining -= 1
        else:
            print("Invalid move. You can only place a flag on a covered location.")
    # 21/ENG/131 - S.Yutheshtrran
    def check_win(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.mines[i][j] and self.field[i][j] != 'F':
                    return False
        return True

    # 21/ENG/009 - A.Harishan
    def count_adjacent_mines(self, row, col):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row, new_col = row + i, col + j
                if 0 <= new_row < self.grid_size and 0 <= new_col < self.grid_size:
                    if self.mines[new_row][new_col]:
                        count += 1
        return count

    # 21/ENG/009 - A.Harishan &&  21/ENG/132 - S.Geerthiga
    def play_game(self):
        self.place_mines()

        while True:
            self.display_field()

            move = input("Enter move (e.g., ABF for flag, ABR for reveal): ").upper()

            if len(move) != 3:
                print("Invalid move. Please enter a valid move.")
                continue

            row, col = ord(move[0]) - ord('A'), ord(move[1]) - ord('A')

            if not (0 <= row < self.grid_size and 0 <= col < self.grid_size):
                print("Invalid move. Please enter a valid move.")
                continue


            action = move[2]

            if action == 'F':
                self.place_flag(row, col)
            elif action == 'R':
                self.reveal_location(row, col)
            else:
                print("Invalid move. Please enter a valid move.")
                continue

            if self.check_win():
                print("Congratulations! You won!")
                self.display_field(reveal_all=True)  
                break

# 21/ENG/131 - S.Yutheshtrran
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
