import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# Функция для создания видео с бегущей строкой
def create_birthday_video_opencv():
    # Текст поздравления
    text = "Привет"

    # Размеры видео (ширина x высота)
    width, height = 100, 100

    # Задаём параметры - видеопоток с частотой 24 кадра в секунду
    out = cv2.VideoWriter("birthday_video_opencv.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 60, (width, height))

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
        font = ImageFont.truetype("Dudka.ttf", 75)
        draw = ImageDraw.Draw(pil_frame)
        draw.text((x, y/2), text, font=font)
        frame = np.asarray(pil_frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


        # Тут запишем кадр
        out.write(frame)

    # Закроем тут видеопоток
    out.release()

# Создаём видео 
create_birthday_video_opencv()