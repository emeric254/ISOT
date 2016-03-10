__author__ = 'toast254'

import sys
import pygame
from Data import Map

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


class PyGameMain:
    """The Main PyMan Class - This class handles the main initialization and creating of the Game."""

    def __init__(self, width=800, height=600):
        """Initialize"""
        #
        # Initialize PyGame
        pygame.init()
        # Set the window Size
        self.width = width
        self.height = height
        # Create the Screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        #
        bak = Map.Map()
        for z in range(len(bak)):
            for y in range(len(bak.carte[z])):
                for x in range(len(bak.carte[z][y])):
                    if isinstance(bak.carte[z][y][x], pygame.Surface):
                        self.screen.blit(bak.carte[z][y][x], (140 * 1/2 * (x-y + 4.5), 140 * 1/4 * (x+y-z*2 + 6)))

    @classmethod
    def main_loop(self):
        """This is the Main Loop of the Game"""
        #
        while 1:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("mouse pressed")
                elif event.type == pygame.MOUSEBUTTONUP:
                    print("mouse released")


if __name__ == "__main__":
    MainWindow = PyGameMain()
    MainWindow.main_loop()
