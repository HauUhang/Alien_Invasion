import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        #Intial 
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Initial Place -- Top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Save place
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #trun right or left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x