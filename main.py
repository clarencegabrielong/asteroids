import pygame

import audio

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from shot import Shot

def game_over(screen, final_score):
    game_over_font = pygame.font.Font(FONT_PATH, 60)
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 65))

    score_font = pygame.font.Font(FONT_PATH, 40)
    score_text = score_font.render(f"Score:{final_score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 5))    

    prompt_font = pygame.font.Font(FONT_PATH, 28)
    prompt = prompt_font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
    prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 65))
    
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
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        screen.blit(prompt, prompt_rect)
        pygame.display.flip()

score = 0

def destroyed_asteroid(asteroid):

    if asteroid.radius == ASTEROID_MIN_RADIUS:
        return 100
    elif asteroid.radius == ASTEROID_MIN_RADIUS * 2:
        return 50 
    else:
        return 20



def main():

    pygame.init()

    audio.init()

    score_font = pygame.font.Font(FONT_PATH, 24)

    pygame.display.set_caption("Asteroids")
    icon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    background = pygame.image.load("assets/background.jpg").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    while True:

        score = 0

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        Shot.containers = (updatable, drawable, shots)

        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        asteroidfield = AsteroidField()

        dt = 0

        restart = False

        while not restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            updatable.update(dt)

            screen.blit(background, (0, 0))

            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    audio.play(audio.ship_explosion_sound)
                    audio.play_music(audio.gaemover_music)
                    if game_over(screen, score):
                        restart = True
                        audio.play_music(audio.background_music)
                    else:
                        return
                    
                for shot in shots:
                    if asteroid.collides_with(shot):
                        audio.play(audio.asteroid_explosion_sound)
                        score += destroyed_asteroid(asteroid)
                        asteroid.split()
                        shot.kill()
                

            for sprite in drawable:
                sprite.draw(screen)
            
            score_text = score_font.render(f"Score:{score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            pygame.display.flip()
            dt = clock.tick(60)/1000


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()
