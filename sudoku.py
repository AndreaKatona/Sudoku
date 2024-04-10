import random
from copy import deepcopy


class Sudoku:

    def __init__(self):

        self.board = [[0] * 9 for _ in range(9)]
        self.solved = None

    def print_board(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")

            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    def find_empty_location(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(self, num, position):

        # Check row
        for i in range(len(self.board[0])):
            if self.board[position[0]][i] == num and position[1] != i:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][position[1]] == num and position[0] != i:
                return False

        # Check box
        box_x = position[1] // 3
        box_y = position[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != position:
                    return False

        return True

    def solve_sudoku(self):

        find = self.find_empty_location()
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.is_valid(num, (row, col)):
                self.board[row][col] = num

                if self.solve_sudoku():
                    return True

                self.board[row][col] = 0

        return False

    def generate(self):

        row = random.randint(0, 8)
        col = random.randint(0, 8)
        self.board[row][col] = random.randint(0, 8)

        self.solve_sudoku()

        self.solved_board = deepcopy(self.board)

        for _ in range(40):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while self.board[row][col] == 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            self.board[row][col] = 0


# if __name__ == "__main__":
#     # Sudoku board (0 represents empty spots)
#     game = Sudoku()
#     game.generate()
#     print("Original Sudoku Board:")
#     game.print_board(game.board)
#     print("Solved Sudoku Board:")
#     game.print_board(game.solved_board)
