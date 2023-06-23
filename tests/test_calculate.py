import numpy as np
import pytest
import sys
sys.path.append('..')
from calculate import calculate_area, get_sum, update_sum  # type: ignore


@pytest.fixture
def example_contours():
    # Создаем пример контуров для тестирования
    contour1 = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
    contour2 = np.array([[2, 2], [2, 3], [3, 3], [3, 2]])
    contour3 = np.array([[4, 4], [4, 5], [5, 5], [5, 4]])
    contours = [
        contour1,  # Капля 1
        contour2,  # Капля 2
        contour3  # Капля 3
    ]
    return contours


def test_calculate_area(example_contours):
    expected_area = 3.0
    area = calculate_area(example_contours)
    assert area == expected_area


def test_update_sum():
    new_value = 50
    update_sum(new_value)
    assert get_sum() == new_value
