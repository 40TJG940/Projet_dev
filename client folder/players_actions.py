import pygame

BLACK = (49, 51, 56)
RED = (171, 28, 24)
YELLOW = (248, 214, 72)

class Player:
    def __init__(self, name, player_id, screen, square_size, width):
        self.name = name
        self.id = player_id
        self.screen = screen
        self.square_size = square_size
        self.width = width
        self.column = 0 if player_id == 1 else 6

    def handle_action(self, event):
        if self.id == 1:
            self.handle_player1_action(event)
        else:
            self.handle_player2_action(event)

    def handle_player1_action(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and self.column > 0:
                self.column -= 1
            elif event.key == pygame.K_d and self.column < 6:
                self.column += 1
        self.update_display(RED)

    def handle_player2_action(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.column > 0:
                self.column -= 1
            elif event.key == pygame.K_RIGHT and self.column < 6:
                self.column += 1
        self.update_display(YELLOW)

    def update_display(self, color):
        posx = self.column * self.square_size + self.square_size // 2
        pygame.draw.rect(self.screen, BLACK, (0, 0, self.width, self.square_size))
        pygame.draw.circle(self.screen, color, (posx, int(self.square_size/2)), self.square_size//2 - 5)
        pygame.display.update()
