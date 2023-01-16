import pygame, sys
from settings import *

class Client():
    """Manage game states and behavior."""

    def __init__(self):
        """Initialize states."""

        # Objects instanciate
        self.settings = Settings()

        # Window comes to life
        self.window = pygame.display.set_mode(self.settings.WINDOW_DIMENTIONS)
        pygame.display.set_caption("Ooooooh!") # Headline on top of window's boarders

    def run_game(self):
        """The game begins."""
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