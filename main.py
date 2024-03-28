import random

import pygame

from Classes.Enemy import Enemy
from Classes.Player import *
from Theme.Button import Button
import sys
from Classes.Ship import *

pygame.init()

# region settings
width, height = 960, 704

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Theme/Fonts/PixelifySans-Medium.ttf", size)

# endregion

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Меню")
background = pygame.image.load("Images/Backgrounds/WorkInProgress2.png")
backgroundGame = pygame.transform.scale(pygame.image.load("Images/Backgrounds/Map.png"), (width, height))

#region MenuFunc
def MainMenu():
    while True:
        screen.blit(background, (0, 0))

        menuMousePos = pygame.mouse.get_pos()

        menuText = get_font(100).render("Space English", True, "#b68f40")
        menuRect = menuText.get_rect(center=(480, 100))

        playButton = Button(image=None, pos=(480, 250),
                            text_input="Игра", font=get_font(75), base_color="Gray", hovering_color="#d7fcd4")
        optionsButton = Button(image=None, pos=(480, 400),
                               text_input="Настройки", font=get_font(75), base_color="Gray", hovering_color="#d7fcd4")
        quitButton = Button(image=None, pos=(480, 550),
                            text_input="Выход", font=get_font(75), base_color="Gray", hovering_color="#d7fcd4")

        screen.blit(menuText, menuRect)

        for button in [playButton, optionsButton, quitButton]:
            button.changeColor(menuMousePos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    Play()
                if optionsButton.checkForInput(menuMousePos):
                    Options()
                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
#endregion


def Play():
    run = True
    FPS = 60
    score = 0
    goal = 3
    playerSpeed = 5
    enemies = []
    enemySpeed = 1
    waveLength = 5
    clock = pygame.time.Clock()

    player = Player(300, 650)

    def redraw_window():
        screen.blit(backgroundGame, (0, 0))

        scoreLabel = get_font(40).render(f"Получено очков: {score}", 1, (255, 0, 0))
        goalLabel = get_font(40).render(f"Осталось собрать: {goal}", 1, (255, 0, 0))

        screen.blit(scoreLabel, (10,10))
        screen.blit(goalLabel, (width - scoreLabel.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(screen)

        player.draw(screen)



        pygame.display.update()
    while run:
        clock.tick(FPS)

        if len(enemies) < 20:  # creating enemies подправить координаты спавна ниже!!!
            enemy = Enemy(random.randrange(50, width-50), random.randrange(-1500, -100), random.choice(["type1", "type2", "type3"]))
            enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - playerSpeed > 0:
            player.x -= playerSpeed # left direction
        if keys[pygame.K_d] and player.x + playerSpeed + player.getWidth() < width: # не забыть
            player.x += playerSpeed # right direction
        if keys[pygame.K_w] and player.y - playerSpeed > 0:
            player.y -= playerSpeed # up direction
        if keys[pygame.K_s] and player.y + playerSpeed + player.getHeight() < height: # не забыть
            player.y += playerSpeed # down direction

        for enemy in enemies:
            enemy.move(enemySpeed)

        redraw_window()
def Options():
    pass

if __name__ == "__main__":
    MainMenu()
