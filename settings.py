
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (53, 81, 98)

        # Ship settings
        self.ship_speed_factor = 1.5
