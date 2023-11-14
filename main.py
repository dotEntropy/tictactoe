import math
import numpy as np
import sys


class Main:
    def __init__(self) -> None:
        pass
        n = 1
        column = (n-1) % 3
        row = math.floor((n-1) / 3)

        self.grid = np.zeros((3, 3), dtype=np.int8)
        self.grids_covered = []
        self.turn = 1 
    
    def run(self) -> None:
        self.ask_player_names()
        while not self.is_won():
            self.turn += 1
            n = self.ask_user_input()
            # put 1 on the specified location
            column = (n-1) % 3
            row = math.floor((n-1) / 3)
            self.grid[row][column] = 1
        # when won
        self.display_win_text()
    
    def is_won(self) -> bool:
        # check rows
        max_row = np.max([sum([self.grid[row][col] for col in range(3)]) for row in range(3)])
        # check columns
        max_column = np.max([sum([self.grid[row][col] for row in range(3)]) for col in range(3)])
        # sum diagonal / 
        diagonal_slash_total = sum([self.grid[row][col] for row, col in zip(range(3), range(2, -1, -1))])
        # sum diagonal \ 
        diagonal_bslash_total = sum([self.grid[cell][cell] for cell in range(3)])
        # check diagonal
        max_diagonal = np.max([diagonal_slash_total, diagonal_bslash_total])
        # check all
        return np.max([max_row, max_column, max_diagonal]) == 3

    def current_player(self) -> str:
        player_index = (self.turn) % 2
        return self.player_names[player_index]
    
    def display_win_text(self) -> None:
        user_input = input(f"\n{self.current_player()} won! Enter [R] to restart.\n{self.get_grid_display()}    ")
        if user_input.lower() == 'r':
            main = Main()
            main.run()
    
    def get_grid_display(self) -> str:
        column_separator = ' | '
        row_separator = '\n---------\n'
        rows = [column_separator.join(map(str, self.grid[row])) for row in range(3)]
        return row_separator.join(rows)
    
    def ask_user_input(self) -> int:
        guide_display_text = f"\n[player: {self.current_player()}] Enter digits from 1 to 9. Start from left to right, top to bottom.\n"
        display_text = f"{guide_display_text}\n{self.get_grid_display()}"
        while True:
            user_input = input(f"{display_text}    ")
            # check if input is an integer, 1-9 inclusive, and if specific grid is already covered
            if user_input.isdigit() and 10 > int(user_input) > 0 and int(user_input) not in self.grids_covered: 
                self.grids_covered.append(int(user_input))
                return int(user_input)
    
    def ask_player_names(self):
        player1_name = input("\n[Enter your name] Player 1: ")
        player2_name = input("[Enter your name] Player 2: ")
        self.player_names = (player1_name, player2_name)


if __name__ == '__main__':
    try:
        main = Main()
        main.run()
    except KeyboardInterrupt:
        sys.exit()
