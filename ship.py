import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        #Initial

        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #Loading ship's image and get enclosing rectangle 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Put the spacecraft into the bottom every time
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal values ​​in the ship attribute center
        self.center = float(self.rect.centerx)

        #Move pointer
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update
        self.rect.centerx = self.center

    def blitme(self):
        #Draw the ship at the specified position
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx