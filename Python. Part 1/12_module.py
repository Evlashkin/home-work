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
# import math
#
#
# def my_distance(x, y):
#     distance = math.sqrt(x**2 + y**2)
#     print("Дистанция от Вас до указанной точки составляет:", distance)
#
#
# def between_distance(x1, y1, x2, y2):
#     distance = math.sqrt((x2 - x1)**2 + (y2 - y1))
#     print("Дистанция между указанными точками составляет:", distance)
#
#
# choise = int(input("Что Вы хотите рассчитать?\n0 - Расстояние от Вас до точки\n1 - Расстояние от точки до точки\n"))
#
# if choise == 0:
#     x = int(input("Введите значение x: "))
#     y = int(input("Введите значение y: "))
#     my_distance(x, y)
#
# elif choise == 1:
#     x1 = int(input("Введите значение x первой точки: "))
#     y1 = int(input("Введите значение y первой точки: "))
#     x2 = int(input("Введите значение x второй точки: "))
#     y2 = int(input("Введите значение y второй точки: "))
#     between_distance(x1, y1, x2, y2)
# else:
#     print("Недопустимый вариант ответа.")
#
#__________________________________________________________________________
# # Final work - task 1
# def summ_n(n):
#     summ = (1 + n) * n / 2
#     print("Сумма всех чисел от 1 до", n, "равна:", summ)
#
#
# n = int(input("Введите число N: "))
# summ_n(n)
#
#
# # Final work - task 2
# def test():
#     num = int(input("Введите целое число: "))
#     if num > 0:
#         positive()
#     elif num < 0:
#         negative()
#     else:
#         print("Вы ввели 0")
#
#
# def positive():
#     print("Положительное")
#
#
# def negative():
#     print("Отрицательное")
#
#
# test()
#
#
# # Final work - task 3
# def total_sum(n):
#     summ = 0
#     for dig in str(n):
#         summ += int(dig)
#     print("Сумма всех цифр в числе равна:", summ)
#     print()
#
#
# def maximum(n):
#     max_num = 0
#     for dig in str(n):
#         if int(dig) > max_num:
#             max_num = int(dig)
#     print("Максимальная цифра в данном числе:", max_num)
#     print()
#
#
# def minimum(n):
#     min_num = 10
#     for dig in str(n):
#         if int(dig) < min_num:
#             min_num = int(dig)
#     print("Минимальная цифра в данном числе:", min_num)
#     print()
#
#
# while True:
#     num = int(input("Введите целое число: "))
#     num = abs(num)
#     print("Какое действие совершить?")
#     print("1 - Найти сумму всех цифр числа;")
#     print("2 - Найти максимальную цифру в числе;")
#     print("3 - Найти минимальную цифру в числе")
#     act = int(input("\nВведите номер действия: "))
#     if act == 1:
#         total_sum(num)
#     elif act == 2:
#         maximum(num)
#     elif act == 3:
#         minimum(num)
#     else:
#         print("Действие с таким номером отсутствует.")
#
#
# # Final work - task 4
# def revers_num(num):
#     new_num = ""
#     for item in str(num):
#         new_num = item + new_num
#     print("Число наоборот:", new_num)
#
#
# def revers_num_without0(num):
#     new_num = ""
#     for item in str(num):
#         if item != "0":
#             new_num = item + new_num
#     print("Число наоборот:", new_num)
#
#
# num = int(input("Введите число: "))
# revers_num(num)
# print()
# revers_num_without0(num)
#
#
# # Final work - task 5
# def count_letters(text, k , n):
#     text = str.upper(text)
#     print(text)
#     count_k = 0
#     count_n = 0
#     for item in text:
#         if item == str(k):
#             count_k += 1
#         elif item == n:
#             count_n += 1
#     print(f"Количество цифр {k}: {count_k}")
#     print(f"Количество букв {n}: {count_n}")
#
#
# text = input("Введите текст: ")
# num = int(input("Какую цифру ищем? "))
# letter = input("Какую букву ищем? ")
#
# count_letters(text, num, letter)
#
#
# # Final work - task 6
# def mynod(num1, num2):
#     nod = 1
#     if num1 >= num2:
#         while True:
#             remainder = num1 % num2
#             if remainder == 0:
#                 nod = num2
#                 print("Наибольший делитель :", nod)
#                 break
#             else:
#                 num1 = num2
#                 num2 = remainder
#     else:
#         num1, num2 = num2, num1
#         mynod(num1, num2)
#
#
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
# mynod(num_1, num_2)
#
#
# # Final work - task 7
def rock_paper_scissors():
  # Здесь будет игра «Камень, ножницы, бумага»

def guess_the_number():
  # Здесь будет игра «Угадай число»

def mainMenu():
  # Здесь главное меню игры

mainMenu():
  pass