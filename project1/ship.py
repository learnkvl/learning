import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self,ai_game):
        
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        #store the decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
         #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """update the ships position based on themovement flag""" 
        if self.moving_right:
           self.x += self.settings.ship_speed
        if self.moving_left:
           self.x -= self.settings.ship_speed
              
        #update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        