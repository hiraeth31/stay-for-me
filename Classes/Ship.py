import pygame.draw

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.shipImg = None

    def draw(self, window):
        window.blit(self.shipImg, (self.x, self.y))

    def getWidth(self):
        return self.shipImg.get_width()
    def getHeight(self):
        return self.shipImg.get_height()
