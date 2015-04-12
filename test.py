__author__ = 'toast254'

import os
import sys
import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


def load_image(name, colorkey=None):
    fullname = os.path.join('Images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:" + name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('Sons', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Cannot load sound:' + name)
        raise SystemExit
    return sound


class PyGameMain:
    """The Main PyMan Class - This class handles the main initialization and creating of the Game."""

    def __init__(self, width=640, height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))

        background = [
            [
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)],
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)],
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)]
            ],
            [
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)],
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)],
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)]
            ],
            [
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)],
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)],
                [load_image("cube.png", -1), load_image("cube.png", -1), load_image("cube.png", -1)]
            ]
        ]

        for z in range(len(background)):
            for y in range(len(background[z])):
                for x in range(len(background[z][y])):
                    self.screen.blit(background[z][y][x], (140 * 1/2 * (x-y +3), 140 * 1/4 * (x+y-z*2 +3)))

    def main_loop(self):
        """This is the Main Loop of the Game"""
        while 1:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse pressed")
                elif event.type == pygame.MOUSEBUTTONUP:
                    print("mouse released")


if __name__ == "__main__":
    MainWindow = PyGameMain()
    MainWindow.main_loop()
