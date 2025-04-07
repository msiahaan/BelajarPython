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
        # Movement flag.
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.center += self.settings.ship_speed
        # Update rect object from self.center.
        # self.rect.centerx = self.center
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)  # Draw the ship at its current location.