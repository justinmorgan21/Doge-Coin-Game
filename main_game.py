"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
""" 
import pygame
import random
from coin import Coin
from player import Player
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (200, 0, 200)
YELLOW = (200, 200, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

def init_coins(coins, all_sprites):
    for i in range(6):
        coin = Coin(SCREEN_WIDTH, SCREEN_HEIGHT, False, False)
        coins.add(coin)
        all_sprites.add(coin)
 
def main():    
    
    pygame.init()
     
    # Set the width and height of the screen [width, height]
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)
    
    hit_sound = pygame.mixer.Sound("hit.ogg")    
     
    pygame.display.set_caption("Doge Coin Collector")
    background_image = pygame.image.load("background2.jpg").convert()
    
    pygame.mixer.music.load('Darude-Sandstorm.ogg')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()    
    
    coins = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    init_coins(coins, all_sprites)
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    all_sprites.add(player)
    
    score = 0
    lives = 3
    
    game_timer = 0
    bomb_timer = 0
    life_timer = 0
    
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
     
        # --- Game logic should go here
            
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)
     
        # --- Drawing code should go here
        #x = int(pygame.time.get_ticks()) / 1000
        font = pygame.font.SysFont('Calibri', 25, True, False)
        score_text = font.render("SCORE: " + str(score), True, RED)
        lives_text = font.render("LIVES: " + str(lives), True, RED)
        
        screen.blit(background_image, [0, 0])
        if lives > 0:
            screen.blit(score_text, [25, 10])
            screen.blit(lives_text, [25, 45])
        
            all_sprites.draw(screen)
            coins.update()
            player.update()
        
            # See if the player block has collided with anything.
            coins_hit_list = pygame.sprite.spritecollide(player, coins, True) 
        
            for coin in coins_hit_list:
                hit_sound.play()
                score += coin.point_value
                if coin.is_life:
                    lives += 1
                    life_timer = 0
                elif coin.is_bomb:
                    lives -= 1  
                    if lives == 0:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('Ace Combat Assault Horizon Legacy - Track 24 - Credits.ogg')
                        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
                        pygame.mixer.music.play()  
                    bomb_timer = 0
                else:
                    new_coin = Coin(SCREEN_WIDTH, SCREEN_HEIGHT, False, False)
                    new_coin.speed += (game_timer / 600) * 2
                    coins.add(new_coin)
                    all_sprites.add(new_coin)
            
            game_timer += 1
            bomb_timer += random.randrange(4)
            life_timer += random.randrange(4)
            
            if game_timer % 600 == 0:
                for coin in coins:
                    coin.speed += 2
            
            if bomb_timer > 300:
                bomb = Coin(SCREEN_WIDTH, SCREEN_HEIGHT, True, False)
                bomb.speed += (game_timer / 600) * 2
                coins.add(bomb)
                all_sprites.add(bomb)
                bomb_timer = 0
            if life_timer > 800:
                life = Coin(SCREEN_WIDTH, SCREEN_HEIGHT, False, True)
                life.speed += (game_timer / 600) * 2
                coins.add(life)
                all_sprites.add(life)
                life_timer = 0
        
        else:          
            final_text = font.render("GAME OVER", True, RED)
            score_text = font.render("SCORE: " + str(score), True, RED)
            screen.blit(final_text, [SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2 - 30])
            screen.blit(score_text, [SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2])
            
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()
    
    
    

if __name__ == "__main__":
    main()