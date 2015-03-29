__author__ = 'toast254'

import os
import sys
import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


class PyGameMain:
    """The Main PyMan Class - This class handles the main initialization and creating of the Game."""
    def __init__(self, width=640,height=480):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))

    def main_loop(self):
        """This is the Main Loop of the Game"""
        while 1:
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
