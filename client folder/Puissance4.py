import numpy as np
import pygame
import sys
import math
import tkinter as tk
from tkinter import messagebox, simpledialog
from players_actions import Player

BLUE = (28, 69, 147)
BLACK = (49, 51, 56)
RED = (171, 28, 24)
YELLOW = (248, 214, 72)

ROW_COUNT = 6
COLUMN_COUNT = 7



class Game:
    
    def __init__(self):
        self.game_over = False
        self.turn = 0
        self.active_player = None
        self.player1 = None
        self.player2 = None
        self.myfont = None
        self.posx = None
        self.column = None
        self.SQUARESIZE = None
        self.width = None
        self.height = None
        self.RADIUS = None
        self.screen = None
        self.board = None

    def create_board(self):
        self.board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return self.board

    def drop_piece(self, row, column, piece):
        self.board[row][column] = piece

    def is_valid_location(self, column):
        return self.board[ROW_COUNT-1][column] == 0

    def get_next_open_row(self, column):
        for r in range(ROW_COUNT):
            if self.board[r][column] == 0:
                return r

    def print_board(self):
        print(np.flip(self.board, 0))

    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

    def draw_board(self):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(self.screen, BLUE, (c*self.SQUARESIZE, r*self.SQUARESIZE+self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))
                pygame.draw.circle(self.screen, BLACK, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):      
                if self.board[r][c] == 1:
                    pygame.draw.circle(self.screen, RED, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int(r*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
                elif self.board[r][c] == 2: 
                    pygame.draw.circle(self.screen, YELLOW, (int(c*self.SQUARESIZE+self.SQUARESIZE/2), self.height-int(r*self.SQUARESIZE+self.SQUARESIZE/2)), self.RADIUS)
        pygame.display.update()

    def is_board_full(self):
        return np.all(self.board != 0)

    def show_tie_popup(self):
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        messagebox.showinfo("Game Over", "It's a tie!")
        root.destroy()

    def get_usernames(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        player1_name = simpledialog.askstring("Input", "Enter Player 1 username:", parent=root)
        player2_name = simpledialog.askstring("Input", "Enter Player 2 username:", parent=root)
        root.destroy()  # Destroy the main window
        return player1_name, player2_name

    def get_username(self):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        player1_name = simpledialog.askstring("Input", "Enter Player 1 username:", parent=root)
        root.destroy()  # Destroy the main window
        return player1_name

    def init_game(self):
        self.board = self.create_board()
        self.print_board()
        self.game_over = False
        self.turn = 0

        # Initialize pygame
        pygame.init()

        # Define our screen size
        self.SQUARESIZE = 100

        # Define width and height of board
        self.width = COLUMN_COUNT * self.SQUARESIZE
        self.height = (ROW_COUNT+1) * self.SQUARESIZE

        size = (self.width, self.height)

        self.RADIUS = int(self.SQUARESIZE/2 - 5)

        self.screen = pygame.display.set_mode(size)
        # Calling function draw_board again
        self.draw_board()
        pygame.display.update()

        self.myfont = pygame.font.SysFont("arial", 75)

        self.posx = self.width // 2  # Initialize posx for drawing the moving piece
        self.column = COLUMN_COUNT // 2  # Initialize column for dropping the piece

        # Get usernames
        player1_name, player2_name = self.get_usernames()

        # Initialize players
        self.player1 = Player(player1_name, 1, self.screen, self.SQUARESIZE, self.width)
        self.player2 = Player(player2_name, 2, self.screen, self.SQUARESIZE, self.width)


    def play(self):
        while not self.game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if self.turn == 0:  # Player 1
                    self.player1.handle_action(event)
                    self.active_player = self.player1
                else:  # Player 2
                    self.player2.handle_action(event)
                    self.active_player = self.player2

                if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN)):
                    pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, self.SQUARESIZE))
                    if self.is_valid_location(self.active_player.column):
                        row = self.get_next_open_row(self.active_player.column)
                        self.drop_piece(row, self.active_player.column, 1 if self.turn == 0 else 2)

                        self.print_board()
                        self.draw_board()

                        if self.winning_move(1 if self.turn == 0 else 2):
                            label = self.myfont.render(f"{self.active_player.name} wins!!", 1, RED if self.turn == 0 else YELLOW)
                            self.screen.blit(label, (40, 10))
                            pygame.display.update()
                            pygame.time.wait(3000)
                            self.game_over = True

                        if not self.game_over and self.is_board_full():
                            self.draw_board()  # Ensure the last piece is drawn
                            self.show_tie_popup()
                            self.game_over = True

                        self.turn += 1
                        self.turn = self.turn % 2
        pygame.quit()

