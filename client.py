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
        self.o_button = pygwidgets.TextButton(self.window, self.settings.center_button, 'Click to change color', callBack=self.color_switch)

    def run_game(self):
        """The game begins."""
        while True:
            # Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

                self.o_button.handleEvent(event)
                    # change background color when button is clicked
                    #self.color_switch()

            # Draw
            # Draw background
            self.window.fill(self.settings.bacckground_color)

            # draw button
            self.o_button.draw()

            # Update every surface by the frame
            pygame.display.update()
        
    def quit_game(self, callBack=None):
        """Quit game and window."""
        pygame.quit()
        sys.exit()

    def color_switch(self, callBack=None):
        """When called it switches between two colors."""
        if  not self.settings.is_BLACK:
            self.settings.bacckground_color = self.settings.BLACK
            self.settings.is_BLACK = True
            
        elif self.settings.is_BLACK:
            self.settings.bacckground_color = self.settings.OCEAN_GREEN
            self.settings.is_BLACK = False
                


if __name__ == "__main__":
    c = Client()
    c.run_game()