# # Unit 5.2 - task 1
# x = int(input("Введите значение координаты X: "))
# y = int(input("Введите значение координаты Y: "))
#
# if x < y:
#     print("X меньше Y")
# else:
#     if x == y:
#         print("X равен Y")
#     else:
#         print("X больше Y")
#
#
# # Unit 5.2 - task 2
# course = 75000
# bank = int(input("Сколько денег на счету? "))
#
# if bank >= course:
#     bank -= course
#     print("Курс успешно приобретен!")
#     if bank < 5000:
#         bank += 1000
#         print("Сделана скидка")
# else:
#     print("Не хватает денег на счету")
#
# print("Ваш счет:", bank)
# print("Хорошего дня!")
#
#
# # Unit 5.2 - task 3
# cheese = 60
# ice_cream = 20
# money = int(input("Сколько денег дала мама? "))
# if money >= cheese:
#     print("Денег на сыр хватило.")
#     money -= cheese
#     if money >= ice_cream:
#         print("И на мороженое тоже.")
#         money -= ice_cream
# else:
#     print("Денег маловато")
#
#
# # Unit 5.3 - task 1
# x = int(input("Введите значение координаты X: "))
# y = int(input("Введите значение координаты Y: "))
#
# if x < y:
#     print("X меньше Y")
# elif x == y:
#     print("X равен Y")
# else:
#     print("X больше Y")
#
#
# # Unit 5.3 - task 2
# salary = int(input("Введите Вашу зарплату: "))
# if salary > 0:
#     if salary < 10000:
#         tax = salary * 13 / 100
#     elif salary < 50000:
#         tax = salary * 20 / 100
#     else:
#         tax = salary * 30 / 100
#     print("Сумма налога составляет:", tax, "рублей.")
# else:
#     print("Зарплата не может иметь отрицательное значение")
#
#
# # Unit 5.3 - task 3
# coin_1 = int(input("Введите вес первой монеты: "))
# coin_2 = int(input("Введите вес второй монеты: "))
# coin_3 = int(input("Введите вес третьей монеты: "))
#
# if coin_1 < coin_2:
#     print("Первая монета фальшивая")
# elif coin_1 == coin_2:
#     print("Третья монета фальшивая")
# else:
#     print("Вторая монета фальшивая")
#
#
# # Unit 5.4 - task 1.1
# year_of_issue = int(input("Введите год выпуска: "))
# speed_count = int(input("Введите количество скоростей: "))
#
# if year_of_issue >= 2018 and speed_count >= 24:
#     print("Этот велик подходит!")
# else:
#     print("Этот не подходит!")
#
# # Unit 5.4 - task 1.2
# year_of_issue = int(input("Введите год выпуска: "))
# speed_count = int(input("Введите количество скоростей: "))
#
# if year_of_issue < 2018 or speed_count < 24:
#     print("Этот велик не подходит!")
# else:
#     print("Этот велик подходит!")
#
#
# # Unit 5.4 - task 2
# total_score = int(input("Введите общий балл по 3-м экзаменам: "))
# medal = int(input("Введите 1 если имеете золотую медаль; введите 0 - если нет: "))
#
# if total_score > 280 and medal == 1:
#     print("Поздравляем, Вы поступили!")
# else:
#     print("К сожалению, Вы не поступили!")
#
#
# # Unit 5.4 - task 3
# temperature = int(input("Введите значение температуры в градусах Цельсия: "))
#
# if 0 <= temperature <= 100:
#     print("Мы в допуске. Все нормально!")
# else:
#     print("Опасность! Температура вышла за пределы допуска!")
