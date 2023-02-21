# # Unit 12.2 - task 1
# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
#
#
# while True:
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting()
#     print('Следующий.\n')
#
#
# # Unit 12.2 - task 2
# def count_item():
#     a = int(input())
#     b = int(input())
#     print("Всего", a + b, "шт.")
#
#
# print("Сколько мешков рыбы и мяса?")
# count_item()
#
# print("\nСколько буханок белого и чёрного хлеба?")
# count_item()
#
# print("\nСколько вёдер воды и молока?")
# count_item()
#
#
# # Unit 12.2 - task 3
# def contactData():
#     surname = "Фамилия: Иванов"
#     name = "Имя: Василий"
#     street = "Улица: Пушкина"
#     house = "Дом: 32"
#     print("", surname, '\n', name, '\n', street, '\n', house, "\n")
#
# contactData()
# contactData()
# contactData()
#
#
# # Unit 12.3 - task 1
# def aboutWater(price):
#     print("Название: КлирВотер")
#     print("Производитель: ВодЗавод")
#     print("Цена:", price)
#     print()
#
#
# aboutWater(25)
# aboutWater(30)
# aboutWater(40)
#
#
# # Unit 12.3 - task 2
# import math
#
#
# def area(radius):
#     s = 4 * math.pi * radius**2
#     print("Площадь равна =", s)
#
#
# def volume(radius):
#     v = 4 * math.pi * radius**3 / 3
#     print("Объем равен =", v)
#
#
# r = 7000
# area(r)
# volume(r)
#
#
# # Unit 12.3 - task 3
# def is_prime(num):
#     if num > 1:
#         count = 0
#         for digit in range(1, num + 1):
#             if num % digit == 0:
#                 count += 1
#             if count == 3:
#                 print(f'Число {num} не является простым')
#                 break
#         if count == 2:
#             print(f"Число {num} простое")
#
#     else:
#         print(f"Число {num} не является простым")
#     print()
#
#
# total_nums = int(input("Введите количество чисел: "))
# for item in range(total_nums):
#     num = int(input("Введите число: "))
#     is_prime(num)
#
#
# # Unit 12.4 - task 1
# def arith_mean(a, b):
#     summ = (a + b) * (b - a + 1) / 2
#     result = summ / (b - a + 1)
#     print("Среднее:", result)
#
#
# left = int(input("Введите левую границу: "))
# right = int(input("Введите правую границу: "))
#
# if left < right:
#     arith_mean(left, right)
# else:
#     print("Правая граница должна быть больше левой.")
#
#
# # Unit 12.4 - task 2
# def post(surname, name, country, city, street, house, flat):
#     print("Фамилия:", surname)
#     print("Имя:", name)
#     print("Страна:", country)
#     print("Город:", city)
#     print("Улица:", street)
#     print("Дом:", house)
#     print("Квартира:", flat)
#     print()
#
#
# post("Евлашкин", "Александр", "Россия", "Москва", "Яблочкова", "37", "26")
# post("Минаев", "Дмитрий", "Россия", "Рязань", "Михайловское ш.", "24", "21")
# post("Прошкин", "Владимир", "Россия", "Рязань", "Михайловское ш.", "31", "2")
#
#
# # Unit 12.4 - task 3
import math


def my_distance(x, y):
    distance = math.sqrt(x**2 + y**2)
    print("Дистанция от Вас до указанной точки составляет:", distance)


def between_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1))
    print("Дистанция между указанными точками составляет:", distance)


choise = int(input("Что Вы хотите рассчитать?\n0 - Расстояние от Вас до точки\n1 - Расстояние от точки до точки\n"))

if choise == 0:
    x = int(input("Введите значение x: "))
    y = int(input("Введите значение y: "))
    my_distance(x, y)

elif choise == 1:
    x1 = int(input("Введите значение x первой точки: "))
    y1 = int(input("Введите значение y первой точки: "))
    x2 = int(input("Введите значение x второй точки: "))
    y2 = int(input("Введите значение y второй точки: "))
    between_distance(x1, y1, x2, y2)
else:
    print("Недопустимый вариант ответа.")
