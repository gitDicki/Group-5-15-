# 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

import pygame
import sys
import random
from random import shuffle
import numpy as np

pygame.init()

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
CHET = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BRIGHT_BLUE = (0, 191, 255)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
BROWN = (139, 69, 19)
OLIVE = (128, 128, 0)
GOLD = (218, 165, 32)
LIME = (0, 255, 0)
PINK = (255, 0, 255)
MRAMOR = (250, 235, 215)
STEEL = (70, 130, 180)
DARKGREEN = (0, 100, 0)
ANGEL = (100, 149, 237)
Colors = [RED, ORANGE, YELLOW, GREEN, BRIGHT_BLUE, BLUE, PURPLE,
          BROWN, OLIVE, GOLD, LIME, PINK, MRAMOR, STEEL, DARKGREEN, ANGEL]
random.shuffle(Colors)
font = pygame.font.Font(None, 28)
pygame.mixer.init()
move_sound = pygame.mixer.Sound("talk.mp3")
move_sound.set_volume(0.5)
shift_sound = pygame.mixer.Sound("enderman_teleport.mp3")
shift_sound.set_volume(0.25)
win_sound = pygame.mixer.Sound("Звук case_reveal_legendary_01.mp3")
win_sound.set_volume(0.25)


def endgame(game, ideal):
    fail = 0
    for i in range(4):
        for j in range(4):
            if game[i][j] != ideal[i][j]:
                fail += 1
    return fail


def draw_popup_message(message, color=WHITE):  # Это для окна
    # Создание поверхности для текста
    text_surface = font.render(message, True, color)

    # Размеры текстовой поверхности
    text_rect = text_surface.get_rect(center=(200, 200))

    # Отрисовка прямоугольника фона
    popup_rect = pygame.Rect(10, 10, 380, 380)
    pygame.draw.rect(screen, BLACK, popup_rect)

    # Отрисовка текста
    screen.blit(text_surface, text_rect)


# функция для отрисовки клеток
def draw_grid(x2, y2):
    counter = 0
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = numbers[row][col]
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            color = Colors[counter] if num != 0 else WHITE
            counter += 1
            # определяем цвет квадрата
            if row == y2 and col == x2:
                color = CHET  # цвет выделенного квадрата

            # отрисовка квадратов
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

            # отрисовка числа
            if num is not None:
                if num != 0:
                    font = pygame.font.Font(None, 74)
                    text = font.render(str(num), True, BLACK)
                    text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text, text_rect)
                else:
                    font = pygame.font.Font(None, 74)
                    text = font.render('=)', True, BLACK)
                    text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text, text_rect)


def start():
    game = np.zeros((4, 4), dtype=int)  # Формируем массив 4 на 4 с типом int
    count = 0
    sum = []
    for i in range(16):  # Генерируем 16 рандомных чисел и записываем их в sum=[]
        sum.append(count)
        count += 1
    random.shuffle(sum)  # Перемешиваем эти 16 чисел
    count = 0
    for i in range(4):  # Присваиваем эти числа к ячейкам массива
        for j in range(4):
            game[i][j] = sum[count]
            count += 1
    zero = [0, 0]
    for i in range(4):  # Ищем нолик в матрице
        for j in range(4):
            if game[i][j] == 0:
                zero[0] = i
                zero[1] = j
    return game


numbers = start()

x = 0
y = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра '15'")
pygame.mixer.music.load("слава гойде тихо.mp3")
pygame.mixer.music.play(-1)

ideal = [[0] * 4 for row in range(4)]
count = 1
for i in range(4):
    for j in range(4):
        ideal[i][j] = count
        count += 1
ideal[3][3] = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.load("слава гойде.mp3")
            pygame.quit()
            sys.exit()

        # перемещение по полю
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y != 0:
                    y -= 1
                    move_sound.play()
                    print(numbers[y][x])
            if event.key == pygame.K_DOWN:
                if y != 3:
                    y += 1
                    move_sound.play()
                    print(numbers[y][x])
            if event.key == pygame.K_LEFT:
                if x != 0:
                    x -= 1
                    move_sound.play()
                    print(numbers[y][x])
            if event.key == pygame.K_RIGHT:
                if x != 3:
                    x += 1
                    move_sound.play()
                    print(numbers[y][x])

            if event.key == pygame.K_UP and \
                    (event.mod & pygame.KMOD_SHIFT):
                if 0 == 0:
                    numbers[y][x], numbers[y + 1][x] = numbers[y + 1][x], numbers[y][x]
                    shift_sound.play()
                    if endgame(numbers, ideal) == 0:
                        win_sound.play()
                        draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                        pygame.display.flip()  # Обновление экрана
                        pygame.time.delay(2500)  # Задержка перед исчезновением сообщения
                        screen.fill(BLACK)  # Очистка экрана после задержки
                        pygame.display.flip()
                        sys.exit()
                else:
                    draw_popup_message("Так эту ячейку не сдвинешь!", GREEN)
                    pygame.display.flip()  # Обновление экрана
                    pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                    screen.fill(BLACK)  # Очистка экрана после задержки
                    pygame.display.flip()

            if event.key == pygame.K_DOWN and \
                    (event.mod & pygame.KMOD_SHIFT):
                if 0 == 0:
                    numbers[y][x], numbers[y - 1][x] = numbers[y - 1][x], numbers[y][x]
                    shift_sound.play()
                    if endgame(numbers, ideal) == 0:
                        win_sound.play()
                        draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                        pygame.display.flip()  # Обновление экрана
                        pygame.time.delay(2500)  # Задержка перед исчезновением сообщения
                        screen.fill(BLACK)  # Очистка экрана после задержки
                        pygame.display.flip()
                        sys.exit()
                else:
                    draw_popup_message("Так эту ячейку не сдвинешь!", GREEN)
                    pygame.display.flip()  # Обновление экрана
                    pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                    screen.fill(BLACK)  # Очистка экрана после задержки
                    pygame.display.flip()

            if event.key == pygame.K_LEFT and \
                    (event.mod & pygame.KMOD_SHIFT):
                if 0 == 0:
                    numbers[y][x], numbers[y][x + 1] = numbers[y][x + 1], numbers[y][x]
                    shift_sound.play()
                    if endgame(numbers, ideal) == 0:
                        win_sound.play()
                        draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                        pygame.display.flip()  # Обновление экрана
                        pygame.time.delay(2500)  # Задержка перед исчезновением сообщения
                        screen.fill(BLACK)  # Очистка экрана после задержки
                        pygame.display.flip()
                        sys.exit()
                else:
                    draw_popup_message("Так эту ячейку не сдвинешь!", GREEN)
                    pygame.display.flip()  # Обновление экрана
                    pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                    screen.fill(BLACK)  # Очистка экрана после задержки
                    pygame.display.flip()

            if event.key == pygame.K_RIGHT and \
                    (event.mod & pygame.KMOD_SHIFT):
                if 0 == 0:
                    numbers[y][x], numbers[y][x - 1] = numbers[y][x - 1], numbers[y][x]
                    shift_sound.play()
                    if endgame(numbers, ideal) == 0:
                        win_sound.play()
                        draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                        pygame.display.flip()  # Обновление экрана
                        pygame.time.delay(2500)  # Задержка перед исчезновением сообщения
                        screen.fill(BLACK)  # Очистка экрана после задержки
                        pygame.display.flip()
                        sys.exit()
                else:
                    draw_popup_message("Так эту ячейку не сдвинешь!", GREEN)
                    pygame.display.flip()  # Обновление экрана
                    pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                    screen.fill(BLACK)  # Очистка экрана после задержки
                    pygame.display.flip()

    screen.fill(WHITE)
    draw_grid(x, y)
    pygame.display.flip()
