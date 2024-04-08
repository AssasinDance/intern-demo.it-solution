import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import os

# Функция для создания видео с бегущей строкой
def scrolling_text(text):

    path = os.path.dirname(__file__) + '/'

    # Размеры видео (ширина x высота)
    width, height = 100, 100

    # Задаём параметры - видеопоток с частотой 24 кадра в секунду
    out = cv2.VideoWriter("scrolling_text.webm", cv2.VideoWriter_fourcc(*'VP80'), 60, (width, height))

    # Создаем кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Начальные координаты для бегущей строки
    x, y = width, height // 2

    # Коэффициент скорости текста
    k = 0.5

    # Пройдемся по каждому кадру
    for t in range(180):  # 10 секунд 60 кадров/сек
        # Очистка кадра
        frame.fill(0)
        pil_frame = Image.fromarray(frame)

        # Новые координаты для бегущей строки
        x -= int(k*len(text))  # Скорость бегущей строки

        # Вот тут добавим текст
        font = ImageFont.truetype(path + "Dudka.ttf", 75)
        draw = ImageDraw.Draw(pil_frame)
        draw.text((x, y/2), text, font=font)
        frame = np.asarray(pil_frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


        # Тут запишем кадр
        out.write(frame)

    # Закроем тут видеопоток
    out.release()
    