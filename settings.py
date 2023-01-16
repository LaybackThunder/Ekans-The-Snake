"""Place holder for states used by other classes."""

class Settings():
    
    def __init__(self):
        """Initiate attributes."""

        # Window attributes
        self.WINDOW_WIDTH = 400
        self.WINDOW_HEIGHT = 800
        self.WINDOW_DIMENTIONS = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        # Button attributes
        self.center_button = (self.WINDOW_WIDTH//2 - 50, self.WINDOW_HEIGHT//2)
