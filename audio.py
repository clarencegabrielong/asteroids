import pygame

AUDIO_ENABLED = False
shoot_sound = None
asteroid_explosion_sound = None
ship_explosion_sound = None

background_music = "assets/background_music/Star Wars VI Return of The Jedi Soundtrack - The Battle of Endor 1.mp3"
gaemover_music = "assets/background_music/Across the Stars (Love Theme from Star Wars_ Attack of the Clones).mp3"

def init():
    global AUDIO_ENABLED, shoot_sound, asteroid_explosion_sound, ship_explosion_sound
    try:
        pygame.mixer.init()
        shoot_sound = pygame.mixer.Sound("assets/sound_effects/mixkit-short-laser-gun-shot-1670.wav")
        asteroid_explosion_sound = pygame.mixer.Sound("assets/sound_effects/mixkit-arcade-game-explosion-2759.wav")
        ship_explosion_sound = pygame.mixer.Sound("assets/sound_effects/mixkit-explosion-hit-1704.wav")
        AUDIO_ENABLED = True
        play_music(background_music)
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