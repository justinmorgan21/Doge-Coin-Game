import pygame
import random
import numpy
import pygame.surfarray as surfarray


class Coin(pygame.sprite.Sprite):
    """ This class represents the target coins to collect. """
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, is_bomb, is_life):
        super().__init__()        
        self.is_bomb = is_bomb
        self.is_life = is_life
        if not is_bomb:
            if is_life:
                self.image = pygame.image.load("life.png").convert_alpha()
                self.speed = 7
                self.point_value = 0
            else:
                random_coin = random.randrange(6)
        
                if random_coin == 0:
                    self.image = pygame.image.load("Dogecoin black.png").convert_alpha()
                    self.speed = 2
                    self.point_value = 10
                elif random_coin == 1:
                    self.image = pygame.image.load("Dogecoin blue.png").convert_alpha()
                    self.speed = 3
                    self.point_value = 25           
                elif random_coin == 2:
                    self.image = pygame.image.load("Dogecoin yellow.png").convert_alpha()
                    self.speed = 4
                    self.point_value = 50            
                elif random_coin == 3:
                    self.image = pygame.image.load("Dogecoin teal.png").convert_alpha()
                    self.speed = 5
                    self.point_value = 75            
                elif random_coin == 4:
                    self.image = pygame.image.load("Dogecoin purple.png").convert_alpha()
                    self.speed = 6
                    self.point_value = 100            
                else:
                    self.image = pygame.image.load("Dogecoin green.png").convert_alpha()
                    self.speed = 8
                    self.point_value = 150     
        else:
            self.image = pygame.image.load("Dogecoin BOMB.png").convert_alpha()
            self.speed = 7
            self.point_value = -400
        
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.SCREEN_WIDTH - 50)
        self.rect.y = random.randrange(-30, 0)    
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 700 and not self.is_bomb and not self.is_life:
            self.rect.x = random.randrange(self.SCREEN_WIDTH - 50)
            self.rect.y = random.randrange(-30, 0)                        
            