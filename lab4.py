import pygame
from pygame.draw import *

# === Инициализация === #
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

# === Цвета === #
BG_COLOR = (255, 255, 255)
HARE_COLOR = (200, 200, 200)
EYE_WHITE = (255, 255, 255)
EYE_PUPIL = (0, 0, 0)
NOSE_COLOR = (255, 0, 0)
WHISKER_COLOR = (0, 0, 0)

# === Конфигурация зайца === #
HARE_CONFIG = {
    "width": 200,
    "height": 400,
    "body_height_ratio": 2 / 3,
    "head_size_ratio": 1 / 4,
    "ear_height_ratio": 1 / 2,
    "ear_width_ratio": 1 / 6,
    "eye_size_ratio": 1 / 6,
    "pupil_ratio": 1 / 2,
    "nose_ratio": 1 / 10,
    "leg_height_ratio": 1 / 16,
    "whisker_count": 3,
    "whisker_spacing": 1 / 10,
}


# === Функции === #
def draw_hare(surface, x, y, config, color):
    width = config["width"]
    height = config["height"]

    body_height = height * config["body_height_ratio"]
    body_width = width / 2
    head_size = height * config["head_size_ratio"]
    ear_height = height * config["ear_height_ratio"]
    ear_width = width * config["ear_width_ratio"]
    eye_size = head_size * config["eye_size_ratio"]
    pupil_size = eye_size * config["pupil_ratio"]
    nose_size = head_size * config["nose_ratio"]
    leg_height = height * config["leg_height_ratio"]
    whisker_count = config["whisker_count"]
    whisker_spacing = head_size * config["whisker_spacing"]

    # Тело
    draw_body(surface, x, y + body_height / 3, body_width, body_height, color)

    # Голова
    head_y = y - head_size / 2
    draw_head(surface, x, head_y, head_size, color)

    # Уши
    ear_y = y - height / 2 + ear_height
    draw_ear(surface, x - ear_width, ear_y, ear_width, ear_height, color)
    draw_ear(surface, x + ear_width, ear_y, ear_width, ear_height, color)

    # Глаза
    eye_y = head_y + head_size / 8
    draw_eye(surface, x - head_size / 4, eye_y, eye_size, pupil_size)
    draw_eye(surface, x + head_size / 4, eye_y, eye_size, pupil_size)

    # Нос
    nose_y = head_y + head_size / 3
    circle(surface, NOSE_COLOR, (int(x), int(nose_y)), int(nose_size))

    # Ноги
    leg_y = y + body_height / 2 - leg_height / 2
    draw_leg(surface, x - body_width / 2, leg_y, body_width / 4, leg_height, color)
    draw_leg(surface, x + body_width / 2, leg_y, body_width / 4, leg_height, color)

    # Усы
    whisker_y = head_y + head_size / 2.5
    for i in range(-1, 2):
        offset = i * whisker_spacing
        # Левый ус
        line(surface, WHISKER_COLOR,
             (x - head_size / 8, whisker_y),
             (x - head_size / 2, whisker_y + offset), 1)
        # Правый ус
        line(surface, WHISKER_COLOR,
             (x + head_size / 8, whisker_y),
             (x + head_size / 2, whisker_y + offset), 1)


def draw_body(surface, x, y, width, height, color):
    points = [
        (x - width / 2, y + height / 5),
        (x + width / 2, y + height / 5),
        (x + width / 4, y - height / 2 + 30),
        (x - width / 4, y - height / 2 + 30),
    ]
    polygon(surface, color, points)

def draw_head(surface, x, y, size, color):
    points = [
        (x - size / 2, y + size / 2),
        (x + size / 2, y + size / 2),
        (x + size / 2, y - size / 2),
        (x - size / 2, y - size / 2),
    ]
    polygon(surface, color, points)

def draw_ear(surface, x, y, width, height, color):
    points = [(x, y - height), (x - width / 2, y), (x + width / 2, y)]
    polygon(surface, color, points)

def draw_leg(surface, x, y, width, height, color):
    points = [
        (x - width / 2, y),
        (x + width / 2, y),
        (x + width / 2, y + height),
        (x - width / 2, y + height),
    ]
    polygon(surface, color, points)

def draw_eye(surface, x, y, eye_size, pupil_size):
    circle(surface, EYE_WHITE, (int(x), int(y)), int(eye_size))
    circle(surface, EYE_PUPIL, (int(x), int(y)), int(pupil_size))


# === Главный цикл === #
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(BG_COLOR)


    draw_hare(screen, 200, 200, HARE_CONFIG, HARE_COLOR)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
