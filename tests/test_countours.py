import cv2
import numpy as np
from get_contours import get_contours


def test_get_contours():
    # Создаем тестовое изображение
    img = np.zeros((100, 100), dtype=np.uint8)
    img[30:70, 30:70] = 255

    # Получаем контуры
    contours = get_contours(img)

    # Проверяем результаты
    assert len(contours) == 1  # Ожидается один контур
    assert cv2.contourArea(contours[0]) == 1743.0
    # Ожидается площадь контура равная 1743.0

    # Проверяем длину контура
    contour_length = cv2.arcLength(contours[0], True)
    assert contour_length == 165.65685415267944
    # Ожидается длина контура равная 176.67570447921753

    # Проверяем тип возвращаемого значения
    assert isinstance(contours, (list, tuple))
    # Ожидается, что возвращаемое значение будет списком или кортежем

    # Проверяем, что контуры имеют правильный тип данных
    assert all(
        isinstance(contour, np.ndarray) for contour in contours)
    # Ожидается, что каждый контур будет массивом NumPy


# Запускаем тест
test_get_contours()
