import pygame

AUDIO_ENABLED = False
shoot_sound = None
asteroid_explosion_sound = None
ship_explosion_sound = None

def init():
    global AUDIO_ENABLED, shoot_sound, asteroid_explosion_sound, ship_explosion_sound
    try:
        pygame.mixer.init()
        shoot_sound = pygame.mixer.Sound("assets/sound_effects/mixkit-short-laser-gun-shot-1670.wav")
        asteroid_explosion_sound = pygame.mixer.Sound("assets/asteroid_explosion.ogg")
        ship_explosion_sound = pygame.mixer.Sound("assets/ship_explosion.ogg")
        pygame.mixer.music.load("assets/background_music.ogg")
        pygame.mixer.music.play(-1)
        AUDIO_ENABLED = True
    except pygame.error:
        print("No audio device found, running without sound")

def play(sound):
    if AUDIO_ENABLED and sound:
        sound.play()

def play_music(path):
    if AUDIO_ENABLED:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)

def stop_music():
    if AUDIO_ENABLED:
        pygame.mixer.music.stop()