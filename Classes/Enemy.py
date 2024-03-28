import os
import pygame
from Classes.Ship import Ship

currentDir = os.path.dirname(__file__)
# enemies sprites
enemyShip1 = pygame.image.load(os.path.join(currentDir, "../Images/Sprites/Enemies/Enemy1.png"))
enemyShip2 = pygame.image.load(os.path.join(currentDir, "../Images/Sprites/Enemies/Enemy2.png"))
enemyShip3 = pygame.image.load(os.path.join(currentDir, "../Images/Sprites/Enemies/Enemy3.png"))



class Enemy(Ship):
    enemyType = {
        "type1": enemyShip1,
        "type2": enemyShip2,
        "type3": enemyShip3
    }
    def __init__(self, x, y, typeName, health=100):
        super().__init__(x, y, health)
        self.shipImg = self.enemyType[typeName]
        self.mask = pygame.mask.from_surface(self.shipImg)
        self.maxHealth = health

    def move(self, speed):
        self.y += speed