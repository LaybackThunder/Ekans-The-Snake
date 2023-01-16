import pygame, sys
from random import choice, randrange

class Client():
    """Manage game states and behavior."""

    def __init__(self):
        """Initialize states."""
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 800

        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Ooooooh!")

    def run_game(self):
        """Game begins."""

        while True:

            # Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.quit_game()
            # Draw 
            pygame.display.update()
        
    def quit_game(self):
        """Quit game and window."""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    c = Client()
    c.run_game()