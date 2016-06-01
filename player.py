import pygame
class Player(pygame.sprite.Sprite):
    """ This class represents the target coins to collect. """
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__()
        self.image = pygame.image.load("new coin purse 2.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2
        self.rect.y = SCREEN_HEIGHT - 70
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        pygame.joystick.init()
        self.joystick_count = pygame.joystick.get_count()
    
    def update(self):
        # As long as there is a joystick
        if self.joystick_count != 0:
         
            joystick = pygame.joystick.Joystick(0)
            joystick.init()            
            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            horiz_axis_pos = joystick.get_axis(0)
            vert_axis_pos = joystick.get_axis(1)
         
            # Move x according to the axis. We multiply by 10 to speed up the movement.
            # Convert to an integer because we can't draw at pixel 3.5, just 3 or 4.
            x_move = int(horiz_axis_pos * 15)
            if abs(x_move) > 3:
                self.rect.x += x_move
            #y_coord = y_coord + int(vert_axis_pos * 10)  
            
        if self.rect.x + self.rect.width > self.SCREEN_WIDTH:
            self.rect.x = self.SCREEN_WIDTH - self.rect.width
        elif self.rect.x < 0:
            self.rect.x = 0
            