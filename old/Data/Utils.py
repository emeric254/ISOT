import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('Images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.geterror():
        print("Cannot load image:" + name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('Sons', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.geterror():
        print('Cannot load sound:' + name)
        raise SystemExit
    return sound