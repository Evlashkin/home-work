# # Unit 11.2 - task 1
# bet = float(input("Сколько ставим? "))
# k = float(input("Какой коэффициент? "))
#
# win = round(bet * k, 2)
#
# print("В положительном случае, Ваш выигрыш составит:", win)
#
#
# # Unit 11.2 - task 2
# age = int(input("Введите возраст: "))
# temp = float(input("Введите температуру тела: "))
# k = 1.5
#
# present = round(k * age * temp, 2)
#
# print("Сумма подарка составляет:", present)
#
#
# # Unit 11.2 - task 3
# height = float(input("Введите рост: "))
# weight = float(input("Введите вес: "))
#
# bmi = round(weight / height**2, 2)
#
# if bmi < 18.5:
#     print("Недостаточная масса тела. BMI =", bmi)
# elif bmi < 25:
#     print("Нормальная масса тела. BMI =", bmi)
# elif bmi < 30:
#     print("Избыточная масса тела. BMI =", bmi)
# else:
#     print("Ожирение.  BMI =", bmi)
#
#
# # Unit 11.3 - task 1
# chatle = int(input("Введите количество чатлов: "))
#
# cr = chatle / 2200
#
# print("Это", cr, "CR")
# print("Можно купить", int(cr * 2), "кораблей")
#
#
# # Unit 11.3 - task 2
# print("Введите местоположение фигуры в метрах")
# x = float(input("По горизонтали: "))
# y = float(input("По вертикали: "))
#
# if x > 0.8 or y > 0.8:
#     print("Клетки с такой координатой не существует")`
# else:
#     xSquare = int(x * 10)
#     ySquare = int(y * 10)
#     print(f"Фигура находится в клетке ({xSquare}, {ySquare})")
#
#
# # Unit 11.3 - task 3
# print("Введите местоположение фигуры в метрах")
# x = float(input("По горизонтали: "))
# y = float(input("По вертикали: "))
#
# if x > 0.8 or y > 0.8:
#     print("Клетки с такой координатой не существует")
# else:
#     xSquare = int(x * 10)
#     ySquare = int(y * 10)
#     xtemp = (50 - int(x * 1000 % 100))/1000
#     ytemp = (50 - int(y * 1000 % 100))/1000
#     print(f"Фигура находится в клетке ({xSquare}, {ySquare})")
#     print(f"Поправьте положение фигуры на ({xtemp}, {ytemp})")
#
#
# # Unit 11.4 - task 1
# import math
#
# a = float(input("Введите значение длины стороны a: "))
# b = float(input("Введите значение длины стороны b: "))
# c = float(input("Введите значение длины стороны c: "))
# p = (a + b + c) / 2     # Полупериметр треугольника абс
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print("Площадь трегольника равна:", s)
#
#
# # Unit 11.4 - task 2
# import math
#
# x = 0
# y = 0
# while True:
#     distance = float(input("Какое расстояние прошел игрок: "))
#     angle = float(input("Какой угол: "))
#     angle *= math.pi / 180
#     new_x = round(distance * math.cos(angle), 1)
#     new_y = round(distance * math.sin(angle), 1)
#     x += new_x
#     y += new_y
#     print(f"Новые координаты: ({x}, {y})")
#
#
# # Unit 11.4 - task 3
# import math
#
# num = float(input("Введите вещественное число: "))
# print("округляет вниз", math.floor(num))
# print("округляет вверх", math.ceil(num))
# print("берет модуль числа", abs(num))
# print("извлекает квадратный корень", math.sqrt(num))
# print("возводит экспоненту в степень, равную числу", math.exp(num))
# print("считает натуральный логарифм числа", math.log(num, 4))
# print("считает логарифм числа по основанию 2", math.log2(num))
# print("считает логарифм числа по основанию 10", math.log10(num))
# print("считает синус и косинус числа", math.sin(num), math.cos(num))
# if num == int(num):
#     print("Факториал: ", math.factorial(num))
#
#__________________________________________________________________________
# # Final work - task 1
# price = float(input("Сколько стоит товар в евро? "))
# price_usd = price * 1.25
# price_rub = round(price_usd * 60.87, 2)
# print("Стоимость товара в рублях:", price_rub)
#
#
# # Final work - task 2
# import math
#
# n = int(input("Введите количество чисел: "))
#
# for item in range(n):
#     num = float(input("Введите число: "))
#     if num > 0:
#         num = math.ceil(num)
#         print(f"x = {num} log(x) =", math.log(num))
#     elif num < 0:
#         num = math.floor(num)
#         print(f"x = {num} exp(x) =", math.exp(num))
#
#
# # Final work - task 3
# import math
#
# size = int(input("Укажите размер файла для скачивания: "))
# speed = int(input("Какова скорость вашего соединения: "))
# time = math.ceil(size / speed)
# downloads = 0
# for sec in range(1, time + 1):
#     if downloads + speed <= size:
#         downloads += speed
#     else:
#         downloads = size
#     perc = math.ceil(downloads / size * 100)
#     print(f"Прошло {sec} сек. Скачано {downloads} из {size} Мб ({perc}%)")
#
#
# # Final work - task 4
# num = float(input("Введите положительное действительное число: "))
# print("Первая цифра после десятичной точки:", int(num * 10) % 10)
#
#
# # Final work - task 5
# import math
#
# rPlanet = float(input("Введите радиус теоретически возможной планеты, км: "))
# vEarth = 10.8321 * 10**11
# vPlanet = (4 / 3) * math.pi * rPlanet**3
# if vEarth > vPlanet:
#     print("Объём планеты Земля больше в", round(vEarth / vPlanet, 3), "раз")
# elif vEarth < vPlanet:
#     print("Объём планеты Земля меньше в", round(vPlanet / vEarth, 3), "раз")
#
#
# # Final work - task 6
# import math
#
# print("Введите местоположение коня:")
# x = float(input("x: "))
# y = float(input("y: "))
#
# print("\nВведите местоположение точки на доске:")
# new_x = float(input("x: "))
# new_y = float(input("y: "))
#
# if 0 <= x <= 0.8 and 0 <= y <= 0.8 and 0 <= new_x <= 0.8 and 0 <= new_y <= 0.8:
#     x = int(x * 10) % 10
#     y = int(y * 10) % 10
#     new_x = int(new_x * 10) % 10
#     new_y = int(new_y * 10) % 10
#
#     print(f"Конь в клетке({x}, {y})", end=". ")
#     print(f"Точка в клетке({new_x}, {new_y})")
#
#     first_cathetus = abs(x - new_x)
#     second_cathetus = abs(y - new_y)
#     hypotenuse = math.sqrt(first_cathetus**2 + second_cathetus**2)
#
#     if hypotenuse == 2.23606797749979:
#         print("Да, конь может ходить в эту точку.")
#     else:
#         print("Нет, конь не может ходить в эту точку")
#
# else:
#     print("Координаты выходят за пределы шахматной доски. Размеры доски (0,8 x 0,8)")
#
#
# # # Final work - task 7
# first_num = float(input("Введите первое число: "))
# second_num = float(input("Введите второе число: "))
#
# summ = first_num + second_num
# diff = abs(first_num - second_num)
# maximum = (summ + diff) / 2
#
# print("Наибольшее число:", maximum)
