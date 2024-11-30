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
                font = pygame.font.Font(None, 74)
                text = font.render(str(num), True, BLACK)
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #перемещение  по полю
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

            if event.key == pygame.K_DOWN and\
                    (event.mod & pygame.KMOD_SHIFT):
                    if numbers[y][x] == 0:
                        numbers[y][x], numbers[y-1][x] = numbers[y-1][x], numbers[y][x]

            if event.key == pygame.K_LEFT and\
                    (event.mod & pygame.KMOD_SHIFT):
                    if numbers[y][x] == 0:
                        numbers[y][x], numbers[y][x+1] = numbers[y][x+1], numbers[y][x]

            if event.key == pygame.K_RIGHT and\
                    (event.mod & pygame.KMOD_SHIFT):
                if numbers[y][x] == 0:
                        numbers[y][x], numbers[y][x-1] = numbers[y][x-1], numbers[y][x]

    screen.fill(WHITE)
    draw_grid(x, y)
    pygame.display.flip()







