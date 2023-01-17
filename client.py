import pygame, sys, pygwidgets
from settings import *

class Client():
    """Manage game states and behavior."""

    def __init__(self, callBack=None):
        """Initialize states."""

        # Initialize all pygame modules
        pygame.init()

        # Call back
        #self.callBack = callBack

        # Objects instanciate
        self.settings = Settings()
        
        # Window comes to life
        self.window = pygame.display.set_mode(self.settings.WINDOW_DIMENTIONS)
        pygame.display.set_caption("Ooooooh!") # Headline on top of window's boarders

        # Object button Instatiate
        self.inst_botton(self.settings.OCEAN_GREEN, self.color_switch)

    def run_game(self):
        """The game begins."""
        while True:
            # Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

                self.o_button.handleEvent(event)
                    # change background & text color when button is clicked

            # Draw
            # Draw background
            self.window.fill(self.settings.bg_color)

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
        # Change bg_color to BLACK if bg_color is BLACK
        if not self.settings.is_BLACK:
            self.settings.bg_color = self.settings.BLACK
            self.settings.is_BLACK = True
            # Change text color from BLACK to OCEAN_GREEN
            self.inst_botton(self.settings.OCEAN_GREEN, self.color_switch)

        # Change bg_color to OCEAN_GREEN if bg_color is BLACK
        elif self.settings.is_BLACK:
            self.settings.bg_color = self.settings.OCEAN_GREEN
            self.settings.is_BLACK = False
            # Change text color from OCEAN_GREEN to BLACK
            self.inst_botton(self.settings.BLACK, self.color_switch) 

    def inst_botton(self, color, callBack=None):
        """Instantiate button when method is called in the middle of the window."""
        self.o_button = pygwidgets.TextCheckBox(self.window, self.settings.center_button, 
                                                'Click to change color', textColor=color,
                                                callBack=callBack)


if __name__ == "__main__":
    c = Client()
    c.run_game()