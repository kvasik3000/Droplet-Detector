import unittest
import cv2  # type: ignore
import os
import sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))  # noqa
from draw import draw_contours_of_drops  # type: ignore  # noqa


class TestDrawContoursOfDrops(unittest.TestCase):
    def test_draw_contours_of_drops(self):
        # Подготавливаем данные для теста
        img_path = 'save_docs/KzfBhfjYMGA.jpg'

        # Вызываем функцию, которую необходимо протестировать
        result = draw_contours_of_drops(img_path)

        # Проверяем, что результат функции - это строка с именем файла
        self.assertIsInstance(result, str)

        # Проверяем, что файл был успешно сохранен
        self.assertTrue(os.path.exists(result))

        # Проверяем, что файл является изображением
        img = cv2.imread(result)
        self.assertIsNotNone(img)

        # Преобразуем изображение в формат CV_8UC1
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Проверяем, что контуры были успешно нарисованы на изображении
        contours, _ = cv2.findContours(
            img_gray,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        self.assertGreater(len(contours), 0)


if __name__ == '__main__':
    unittest.main()
