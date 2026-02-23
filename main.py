import pygame 
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from shot import Shot

def game_over(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    prompt_font = pygame.font.Font(None, 36)
    prompt = prompt_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  
                if event.key == pygame.K_q:
                    return False 
        
        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        screen.blit(prompt, prompt_rect)
        pygame.display.flip()

def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    pygame.display.set_caption("Asteroids")
    icon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(icon)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                if game_over(screen):
                    return main()
                else:
                    return
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            

        for sprite in drawable:
            sprite.draw(screen)
        

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
    pygame.quit()
