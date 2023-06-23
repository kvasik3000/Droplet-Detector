import cv2  # type: ignore
from do_xslx import do_df
from typing import List


sum_area_s: float = 0


def get_sum() -> float:
    """
    Возвращает текущую сумму площадей.
    """
    return sum_area_s


def update_sum(new_value: float) -> None:
    """
    Обновляет значение суммы площадей.

    Args:
        new_value: Новое значение суммы площадей (тип: float).
    """
    global sum_area_s
    sum_area_s = new_value


def calculate_area(contours: List[List[float]]) -> float:
    """
    Вычисляет общую площадь для заданных контуров.

    Args:
        contours: Список контуров (тип: List[List[float]]).

    Returns:
        Общая площадь (тип: float).
    """
    all_area: float = 0

    for contour in contours:
        all_area += cv2.contourArea(contour)
    do_df(contours)
    update_sum(all_area)
    return all_area
