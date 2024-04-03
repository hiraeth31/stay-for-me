import random
import pygame
import sys
from Theme.Button import Button
from Classes.Enemy import Enemy
from Classes.Learn import *
from Classes.Player import *
from Classes.Ship import *

pygame.init()

# region settings
width, height = 960, 704
surface = pygame.Surface((width, height), pygame.SRCALPHA)
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Theme/Fonts/Allods.ttf", size)

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

def collide(obj1, obj2): # столкновение объектов
    offsetX = obj2.x - obj1.x
    offsetY = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offsetX, offsetY)) != None

def drawPauseMenu():
    pygame.draw.rect(surface, (128, 128, 128, 150), [0, 0, width, height])
    screen.blit(surface, (0, 0))
    learn = Learn()
    word, meaning = learn.wordChoose()

    # Создаем текстовую поверхность для слова и значения
    word_surface = get_font(75).render(word, True, (255, 255, 255))
    meaning_surface = get_font(75).render(meaning, True, (255, 255, 255))

    # Определяем координаты для вывода текста
    word_pos = (width // 2 - word_surface.get_width() // 2, height // 2 - 50)
    meaning_pos = (width // 2 - meaning_surface.get_width() // 2, height // 2 + 50)

    # Выводим текст на экран
    screen.blit(word_surface, word_pos)
    screen.blit(meaning_surface, meaning_pos)

    pygame.display.update() # обновить дисплей не забыть




def Play():
    run = True
    global paused
    paused = False
    FPS = 60
    score = 0
    goal = 3
    playerSpeed = 5
    enemies = []
    enemySpeed = 1
    hearts = 15
    lost = False
    lostCount = 0
    clock = pygame.time.Clock()

    player = Player(width/2 - playerShip.get_width()/2, height - playerShip.get_height()) # снизу посередине

    def redraw_window():
        screen.blit(backgroundGame, (0, 0))

        scoreLabel = get_font(40).render(f"Очки: {score}", 1, (255, 0, 0))
        heartLabel = get_font(40).render(f"Жизни: {hearts}", 1, (255, 0, 0))

        screen.blit(scoreLabel, (10,10))
        screen.blit(heartLabel, (10, scoreLabel.get_height()))

        for enemy in enemies:
            enemy.draw(screen)

        player.draw(screen)

        if lost:
            lostLabel = get_font(60).render("Вы проиграли :(", 1, (255, 0, 0))
            screen.blit(lostLabel, (width/2 - lostLabel.get_width()/2, 350)) # здесь возможно с положением надписи поиграться надо

        pygame.display.update()


    while run:
        clock.tick(FPS)

        if paused == False:
            redraw_window()

            if score >= 10 : # для теста с LEARN
                drawPauseMenu()
                paused = True

        if hearts <= 0:
            lost = True
            lostCount += 1

        if lost:
            if lostCount > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) < 20:  # creating enemies подправить координаты спавна ниже!!!
            enemy = Enemy(random.randrange(50, width-50), random.randrange(-1500, -100), random.choice(["type1", "type2", "type3"]))
            enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if paused == False:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and player.x - playerSpeed > 0:
                player.x -= playerSpeed # left direction
            if keys[pygame.K_d] and player.x + playerSpeed + player.getWidth() < width: # не забыть
                player.x += playerSpeed # right direction
            if keys[pygame.K_w] and player.y - playerSpeed > 0:
                player.y -= playerSpeed # up direction
            if keys[pygame.K_s] and player.y + playerSpeed + player.getHeight() < height: # не забыть
                player.y += playerSpeed # down direction

            for enemy in enemies[:]:
                enemy.move(enemySpeed)
                if enemy.y + enemy.getHeight() > height:
                    score += 5
                    enemies.remove(enemy)
                if collide(enemy, player): # столкновение игрока и препятствия
                    hearts -= 1
                    enemies.remove(enemy)


def Options():
    pass

if __name__ == "__main__":
    MainMenu()
