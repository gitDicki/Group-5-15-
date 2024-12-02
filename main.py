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

font = pygame.font.Font(None, 28)

def endgame(game):
    rows, cols = len(game), len(game[0])

    for i in range(rows):
        for j in range(cols - 1):
            if game[i][j] >= game[i][j + 1]:
                return 1

    for i in range(rows - 1):
        if game[i][cols - 1] >= game[i + 1][0]:
            return 1
    return 0

def draw_popup_message(message, color=WHITE):#Это для окна
    # Создание поверхности для текста
    text_surface = font.render(message, True, color)

    # Размеры текстовой поверхности
    text_rect = text_surface.get_rect(center=(200, 200))

    # Отрисовка прямоугольника фона
    popup_rect = pygame.Rect(10, 10, 380, 380)
    pygame.draw.rect(screen, BLACK, popup_rect)

    # Отрисовка текста
    screen.blit(text_surface, text_rect)

#функция для отрисовки клеток
def draw_grid(x2, y2):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = numbers[row][col]
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            
            #определяем цвет квадрата
            if row == y2 and col == x2:
                color = CHET  #цвет выделенного квадрата
            else:
                color = GRAY if num is not None else WHITE
            
            #отрисовка квадратов
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            
            #отрисовка числа
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.load("слава гойде.mp3")
            pygame.quit()
            sys.exit()

        
        #перемещение по полю
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y != 0:
                    y -= 1
                    print(numbers[y][x])    
            if event.key == pygame.K_DOWN:
                if y != 3:
                    y += 1
                    print(numbers[y][x])
            if event.key == pygame.K_LEFT:
                if x != 0:
                    x -= 1
                    print(numbers[y][x])
            if event.key == pygame.K_RIGHT:
                if x != 3:
                    x += 1
                    print(numbers[y][x])



            if event.key == pygame.K_UP and\
                    (event.mod & pygame.KMOD_SHIFT):
                    if numbers[y][x] == 0:
                        numbers[y][x], numbers[y+1][x] = numbers[y+1][x], numbers[y][x]
                        if endgame(numbers) == 0:
                            draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                            pygame.display.flip()  # Обновление экрана
                            pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                            screen.fill(BLACK)  # Очистка экрана после задержки
                            pygame.display.flip()
                            sys.exit()
                    else:
                        draw_popup_message("Так эту ячейку не сдвинешь!", GREEN)
                        pygame.display.flip()  # Обновление экрана
                        pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                        screen.fill(BLACK)  # Очистка экрана после задержки
                        pygame.display.flip()

            if event.key == pygame.K_DOWN and\
                    (event.mod & pygame.KMOD_SHIFT):
                    if numbers[y][x] == 0:
                        numbers[y][x], numbers[y-1][x] = numbers[y-1][x], numbers[y][x]
                        if endgame(numbers) == 0:
                            draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                            pygame.display.flip()  # Обновление экрана
                            pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                            screen.fill(BLACK)  # Очистка экрана после задержки
                            pygame.display.flip()
                            sys.exit()
                    else:
                        draw_popup_message("Так эту ячейку не сдвинешь!", GREEN)
                        pygame.display.flip()  # Обновление экрана
                        pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                        screen.fill(BLACK)  # Очистка экрана после задержки
                        pygame.display.flip()

            if event.key == pygame.K_LEFT and\
                    (event.mod & pygame.KMOD_SHIFT):
                    if numbers[y][x] == 0:
                        numbers[y][x], numbers[y][x+1] = numbers[y][x+1], numbers[y][x]
                        if endgame(numbers) == 0:
                            draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                            pygame.display.flip()  # Обновление экрана
                            pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                            screen.fill(BLACK)  # Очистка экрана после задержки
                            pygame.display.flip()
                            sys.exit()
                    else:
                        draw_popup_message("Так эту ячейку не сдвинешь!", GREEN)
                        pygame.display.flip()  # Обновление экрана
                        pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
                        screen.fill(BLACK)  # Очистка экрана после задержки
                        pygame.display.flip()

            if event.key == pygame.K_RIGHT and\
                    (event.mod & pygame.KMOD_SHIFT):
                if numbers[y][x] == 0:
                        numbers[y][x], numbers[y][x-1] = numbers[y][x-1], numbers[y][x]
                        if endgame(numbers) == 0:
                            draw_popup_message("ПОБЕДА!! ГОЙДА!! ГОЛ!!", RED)
                            pygame.display.flip()  # Обновление экрана
                            pygame.time.delay(1500)  # Задержка перед исчезновением сообщения
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
