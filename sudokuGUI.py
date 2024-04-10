import pygame
from sudoku import Sudoku
import sys


class GUI:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.sudoku.generate()
        self.screen_width = 500
        self.screen_height = 500
        self.cell_size = self.screen_width // 9
        self.selected_cell = None
        self.font = None
        self.init_pygame()

    def init_pygame(self):
        pygame.init()
        self.font = pygame.font.SysFont("comicsans", 40)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Sudoku")

    def draw_board(self):
        for i in range(9):
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    pygame.draw.rect(
                        self.screen,
                        (135, 206, 250),
                        (
                            j * self.cell_size,
                            i * self.cell_size,
                            self.cell_size * 3,
                            self.cell_size * 3,
                        ),
                        3,
                    )  # 3x3
                else:
                    pygame.draw.rect(
                        self.screen,
                        (135, 206, 250),
                        (
                            j * self.cell_size,
                            i * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                        1,
                    ) 
                if self.sudoku.board[i][j] != 0:
                    text = self.font.render(
                        str(self.sudoku.board[i][j]), True, ((0, 0, 0))
                    )
                    self.screen.blit(
                        text,
                        (
                            j * self.cell_size
                            + self.cell_size // 2
                            - text.get_width() // 2,
                            i * self.cell_size
                            + self.cell_size // 2
                            - text.get_height() // 2,
                        ),
                    )

    def draw_selected_cell(self):
        if self.selected_cell:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                (
                    self.selected_cell[1] * self.cell_size,
                    self.selected_cell[0] * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                ),
                3,
            )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = y // self.cell_size
                    col = x // self.cell_size
                    self.selected_cell = (row, col)
                if event.type == pygame.KEYDOWN:
                    if event.key in range(pygame.K_1, pygame.K_9 + 1):
                        if self.selected_cell and self.sudoku.board[row][col] == 0:
                            number = int(chr(event.key))
                            if self.sudoku.solved_board[row][col] == number:
                                text_color = (0, 0, 0) 
                                self.sudoku.board[row][col] = number
                                text = self.font.render(str(number), True, text_color)
                                self.screen.blit(text, (col * self.cell_size + self.cell_size // 2 - text.get_width() // 2, row * self.cell_size + self.cell_size // 2 - text.get_height() // 2))
                                pygame.display.update()

            self.screen.fill((255, 255, 255))
            self.draw_board()
            self.draw_selected_cell()
            pygame.display.update()
    


if __name__ == "__main__":
    sudoku = Sudoku()
    gui = GUI(sudoku)
    gui.run()
