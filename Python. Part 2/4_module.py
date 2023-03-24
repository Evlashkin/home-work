# Unit 4.2 - task 1
# left_board = int(input("Левая граница: "))
# right_board = int(input("Правая граница: "))
#
# cube = [x ** 3 for x in range(left_board, right_board + 1)]
# square = [x ** 2 for x in range(left_board, right_board + 1)]
#
# print(f"Список кубов чисел в диапазоне от {left_board} до {right_board}:", cube)
# print(f"Список квадратов чисел в диапазоне от {left_board} до {right_board}:", square)


# Unit 4.2 - task 2
# string = input("Введите строку: ")
# add_sym = input("Введите дополнительный символ: ")
#
# list_with2sym = [sym * 2 for sym in string]
# list_with2sym_and_add = [sym + add_sym for sym in list_with2sym]
#
# print("Список удвоенных символов:", list_with2sym)
# print("Склейка с дополнительным символом:", list_with2sym_and_add)


# Unit 4.2 - task 3
# def price_up(price, percent):
#     return price * (1 + percent / 100)
#
#
# price_list_now = []
#
# for _ in range(5):
#     price = float(input("Цена на товар: "))
#     price_list_now.append(price)
#
# first_year_percent = float(input("Повышение на первый год: "))
# second_year_percent = float(input("Повышение на второй год: "))
#
# first_price_list = [price_up(price, first_year_percent) for price in price_list_now]
# second_price_list = [price_up(price, second_year_percent) for price in first_price_list]
#
# print("Сумма цен за каждый год:", round(sum(price_list_now), 2), round(sum(first_price_list), 2),
#       round(sum(second_price_list), 2))


# Unit 4.3 - task 1
# left_board = int(input("Введите левую границу: "))
# right_board = int(input("Введите правую границу: "))
#
# even_nums_list = [x for x in range(left_board, right_board + 1) if x % 2 == 0]
# print("Список из четных чисел:", even_nums_list)


# Unit 4.3 - task 2
# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# new_prices = [0 if x < 0 else x for x in original_prices]
# print("Список с новыми ценами:", new_prices)


# Unit 4.3 - task 3
# import random
#
# squad_1 = [random.randint(50, 80) for _ in range(10)]
# squad_2 = [random.randint(30, 60) for _ in range(10)]
# squad_3 = ["Погиб" if sum([squad_1[i], squad_2[i]]) >= 100 else "Выжил" for i in range(10)]
#
# print("Урон первого отряда", squad_1)
# print("Урон второго отряда", squad_2)
# print("Состояние третьего отряда", squad_3)


# Unit 4.4 - task 1
# import random
#
# original_prices = [random.randint(-100, 100) for _ in range(10)]
# new_prices = original_prices[:]
# new_prices = [0 if i < 0 else i for i in new_prices]
# print(original_prices)
# print(new_prices)
#
# print("Мы потеряли: ",  sum(new_prices) - sum(original_prices))


# Unit 4.4 - task 2
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
#
# print("1:", nums[:5])
# print("2:", nums[:-2])
# print("3:", nums[::2])
# print("4:", nums[1::2])
# print("5:", nums[::-1])
# print("6:", nums[::-2])


# Unit 4.4 - task 3
# import random
#
# my_list = [random.randint(-100, 100) for _ in range(random.randint(5, 20))]
# a_board = random.randint(0, 4)
# b_board = random.randint(4, len(my_list))
# print(my_list)
# print("Удалить:", a_board, "-", b_board)
# my_list = my_list[:a_board] + my_list[b_board + 1:]
# print(my_list)
