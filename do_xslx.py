import pandas as pd
import cv2  # type: ignore
from openpyxl import Workbook
from typing import List
from pandas.core.frame import DataFrame


num_of_table: int = 0


def get_num() -> int:
    """
    Возвращает текущее значение переменной num_of_table.

    Возвращает:
    - int: Текущее значение переменной num_of_table.
    """
    return num_of_table


def update_num(new_value: int) -> None:
    """
    Обновляет значение переменной num_of_table.

    Аргументы:
    - new_value (int): Новое значение для переменной num_of_table.
    """
    global num_of_table
    num_of_table = new_value


def do_df(contours: List) -> DataFrame:
    """
    Создает DataFrame на основе переданных контуров.

    Аргументы:
    - contours (List): Список контуров.

    Возвращает:
    - DataFrame: Созданный DataFrame.
    """
    len_contours = len(contours)
    df = pd.DataFrame()
    column_name = "Площадь капли"  # Добавляем название столбца
    for i in range(len_contours):
        row_name = f"Капля {i + 1}"  # Генерируем название строки
        value = cv2.contourArea(contours[i])  # Генерируем значение для столбца
        df.loc[row_name, column_name] = value  # Добавляем строку в датафрейм
    to_excel(df)
    return df


def to_excel(data: DataFrame) -> None:
    """
    Сохраняет DataFrame в файл формата Excel.

    Аргументы:
    - data (DataFrame): DataFrame для сохранения в файл.
    """
    global num_of_table
    workbook = Workbook()
    sheet = workbook.active  # Получаем активный лист
    print(sheet)
    workbook.save(f'excel/new{num_of_table}.xlsx')  # Сохраняем рабочую книгу в файл
    data.to_excel(f'excel/new{num_of_table}.xlsx')
    num_of_table += 1
    update_num(num_of_table)
