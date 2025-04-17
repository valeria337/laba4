import pygame
from pygame.draw import *

# Инициализация Pygame
pygame.init()

# Установка параметров
FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_hare(surface, x, y, width, height, color):
    """
    Рисует изменённого зайца на экране без использования эллипсов.
    surface - объект pygame.Surface
    x, y - координаты центра изображения
    width, height - ширина и высота изображения
    color - цвет, заданный в формате, подходящем для pygame.Color
    """
    body_height = height * 2 / 5  # Уменьшаем высоту тела
    body_width = width / 2

    # Рисуем тело
    draw_body(surface, x, y + body_height / 3, body_width, body_height, color)

    # Рисуем голову
    head_size = height / 3  # Увеличиваем размер головы для округленности
    draw_head(surface, x, y - head_size / 2 + 15, head_size, color)

    # Рисуем уши
    ear_height = head_size / 1.5  # Увеличим размер ушей
    ear_width = width / 8
    ear_y = y - height / 2 + ear_height  # Поднимаем уши вверх
    draw_ear(surface, x - ear_width / 2 - 15, ear_y, ear_width, ear_height, color)
    draw_ear(surface, x + ear_width / 2 + 15, ear_y, ear_width, ear_height, color)

    # Рисуем ноги
    leg_height = height / 12  # Изменяем размер ног
    leg_y = y + body_height / 2 - leg_height / 2
    draw_leg(surface, x - body_width / 4, leg_y, body_width / 4, leg_height, color)
    draw_leg(surface, x + body_width / 4, leg_y, body_width / 4, leg_height, color)

    # Добавим глаза и нос
    eye_size = head_size / 10
    draw_eyes(surface, x, y - head_size / 2 + head_size / 4, eye_size)
    draw_nose(surface, x, y - head_size / 2 + head_size / 2, eye_size / 2)


def draw_body(surface, x, y, width, height, color):
    """Рисует тело зайца в виде многоугольника"""
    points = [
        (x - width / 2, y + height / 5),
        (x + width / 2, y + height / 5),
        (x + width / 4, y - height / 2 + 40),
        (x - width / 4, y - height / 2 + 40),
    ]
    polygon(surface, color, points)


def draw_head(surface, x, y, size, color):
    """Рисует голову зайца"""
    points = [
        (x - size / 2, y + size / 2),
        (x + size / 2, y + size / 2),
        (x + size / 2, y - size / 2),
        (x - size / 2, y - size / 2)
    ]
    polygon(surface, color, points)


def draw_ear(surface, x, y, width, height, color):
    """Рисует ухо зайца"""
    points = [(x, y - height), (x - width / 2, y), (x + width / 2, y)]
    polygon(surface, color, points)


def draw_leg(surface, x, y, width, height, color):
    """Рисует ногу зайца"""
    points = [
        (x - width / 2, y),
        (x + width / 2, y),
        (x + width / 2, y + height),
        (x - width / 2, y + height)
    ]
    polygon(surface, color, points)


def draw_eyes(surface, x, y, size):
    """Рисует глаза зайца"""
    eye_color = (0, 0, 0)  # Черный цвет для глаз
    circle(surface, eye_color, (x - size - 5, y), size)  # Левый глаз
    circle(surface, eye_color, (x + size + 5, y), size)  # Правый глаз


def draw_nose(surface, x, y, size):
    """Рисует нос зайца"""
    nose_color = (255, 0, 0)  # Красный цвет для носа
    circle(surface, nose_color, (x, y), size)  # Нос


# Основной цикл программы
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Рисуем зайца
    draw_hare(screen, 200, 200, 200, 400, (200, 200, 200))

    # Обновление экрана
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
