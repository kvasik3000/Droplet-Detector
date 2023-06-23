# Droplet-Detector
![Build Status](https://github.com/kvasik3000/Droplet-Detector/actions/workflows/python-app.yml/badge.svg?branch=main)

![droplet](https://github.com/kvasik3000/Droplet-Detector/assets/124969658/c1928e58-414d-49ef-97dd-20d10441bfd5)


## Введение
Перед нашей командой стояла задача создать простой в использовании проект, который будет рисовать контуры капель. Также было необходимо написать код для подсчёта пикселей каждой капли и добавить возможность сохранять данные в виде таблицы. Эта работа позволила нам глубже изучить компьютерное зрение с помощью библиотек **OpenCV2** в Python, научиться работать в команде и дала возможность создать собственного телеграмм-бота.

### Работу выполнили студенты из группы 21932:

- [Квас Андрей](https://github.com/kvasik3000)
- [Некрасова Анна](https://github.com/NekrasovaAnn)
- [Белькова Ксения](https://github.com/didilovu)

## Обнаружение контуров

Для корректного обнаружения контуров капель мы использовали **Canny Edge**. Это алгоритм, состоящий из 4 основных шагов:

1. Уменьшение шума с помощью гауссовского сглаживания.
2. Вычисление градиента изображения с помощью фильтра Собеля.
3. Применение Non-Max Suppression для простого подавления локальных минимумов.
4. Применения пороговой обработки с Гистерезисом, которая создает 2 пороговых значения T_upper и T_lower, которые используются в функции Canny().

Для наглдяности покажем работу алгоритма на следующем изображении капель:

![разг](https://github.com/kvasik3000/Droplet-Detector/assets/124969658/32e768ae-bb56-4cb3-b32c-61f6f3158c25)


## Расчёт площади

Для того, чтобы правильно считалась площадь, была необходима отрисовка замкнутых контуров капель. Это и была следующая проблема, с которой мы столкнулись. Для ее решения мы последовательлно применяли несколько функций:

1. Уменьшение шума с помощью медианного сглаживания.
2. Увелечение резкости изображения с помощью 2D фильтра
3. Маска Собеля для выделения контуров.
4. Размытие Гаусса для уменьшения шума.
5. Обнаружение контуров с помощью Canny.
6. Получение массива внешних контуров с помощью findContours.
7. Закрашиваниие контуров с помощью fillPoly.
8. Повторяем с шага 1 для получившейся маски.
9. Сложение двух получившихся масок.
10. Отрисовка контуров на картикне.

Для подсчета площади капли в пикселях использовалась функция contourArea, которая считает пиксели в замкнутом контуре.

В итоге, мы пришли к следующим результатам:

![разг2](https://github.com/kvasik3000/Droplet-Detector/assets/124969658/7904d768-380c-4ff6-be3d-87fbaf159be0)


## Отрисовка контуров на входном изображении

В конце программы у нас имеются входное изображение и маска с контурами этого изображения. С помощью функции bitwise_and(img, img, mask=mask) из библиотеки **OpenCV2** мы рисуем маску прямо на входном изображении и выводим это как итог.

## Телеграмм-бот

Для взаимодействия пользователя и телеграмм-бота мы использовали библиотеку **Telebot**. Бот запускается с помощью команды /start, после чего он нас приветствует и просит ввести команду Help. Далее мы можем увидеть список команд в определённой последовательности для корректной работы. Наш бот не очень разговорчивый, поэтому если вы попытаетесь поговорить с ним на отдалённые темы, у вас ничего не выйдет.


![Без имени](https://github.com/kvasik3000/Droplet-Detector/assets/124969658/ff7c0fff-05f0-4ddb-8bc3-4225ed99166e)


## DockerHub 
- https://hub.docker.com/repository/docker/nekrasovaanna/droplet-detector/general
Команда для начала работы проекта
- docker run nekrasovaanna/droplet-detector

## Источники

- https://www.geeksforgeeks.org/python-opencv-canny-function/
- https://opencvguide.readthedocs.io/_/downloads/en/latest/pdf/
- https://pytba.readthedocs.io/ru/latest/index.html
