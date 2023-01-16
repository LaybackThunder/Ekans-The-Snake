import pygame, sys, pygwidgets
from settings import *

class Client():
    """Manage game states and behavior."""

    def __init__(self):
        """Initialize states."""

        # Initialize all pygame modules
        pygame.init()

        # Objects instanciate
        self.settings = Settings()
        
        # Window comes to life
        self.window = pygame.display.set_mode(self.settings.WINDOW_DIMENTIONS)
        pygame.display.set_caption("Ooooooh!") # Headline on top of window's boarders

        # Object button Instatiate
        self.o_button = pygwidgets.TextButton(self.window, self.settings.center_button, 'Click to quit', callBack=self.quit_game)

    def run_game(self):
        """The game begins."""
        while True:
            # Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

                self.o_button.handleEvent(event)
                    # Quit game when button is clicked

            # Draw 
            # draw button
            self.o_button.draw()

            # Update every surface by the frame
            pygame.display.update()
        
    def quit_game(self):
        """Quit game and window."""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    c = Client()
    c.run_game()