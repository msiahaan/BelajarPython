import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        # self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        #self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's center.
        # self.center = float(self.rect.centerx)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)  # Draw the ship at its current location.