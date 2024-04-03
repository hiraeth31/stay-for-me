import os
import pygame
from Classes.Ship import Ship

currentDir = os.path.dirname(__file__)

playerShip = pygame.image.load(os.path.join(currentDir, "../Images/Sprites/Allies/playerSprite.png")) # main character sprite

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.shipImg = playerShip
        self.mask = pygame.mask.from_surface(self.shipImg)
        self.maxHealth = health
