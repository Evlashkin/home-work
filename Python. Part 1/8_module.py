# # Unit 8.2 - task 1
# n = int(input("Введите значение N: "))
# for digit in range(1, (n // 2) + 1):
#     print("(", digit, "* 2 )^3 =", (digit * 2)**3)
#
#
# # Unit 8.2 - task 2
# total_hours = int(input("Введите количество часов в наблюдении: "))
# amoeba = 1
#
# for hours in range(1, (total_hours // 3) + 1):
#     amoeba *= 2
#     print(f"Прошло часов: {hours * 3}")
#     print(f"Клеток: {amoeba}")
#     print(f"Часов до конца эксперимента: {total_hours - hours * 3}")
#     print()
# print("Эксперимент завершен")
#
#
# # Unit 8.2 - task 3
# n = int(input("Введите значение N: "))
# for num in range(1, (n // 2) + n % 2 + 1):
#     print(num * 2 - 1,"^2  =", (num * 2 - 1)**2)
#
#
# # Unit 8.3 - task 1
# n = int(input("Введите значение N: "))
#
# for num in range(1, n + 1, 2):
#     print(num, "^3 =", num**3)
#
#
# # Unit 8.4 - task 2
# n = int(input("Введите значение N: "))
# summ = 0
#
# for num in range(1, n + 1, 5):
#     print(num)
#     summ += num
#
# print("Сумма:", summ)
#
#
# # Unit 8.4 - task 3
# wake_up = int(input("Во сколько Саша проснулся?"))
# water = 0
# calories = 0
#
# for hour in range(wake_up, 23, 3):
#     print(f"Сейчас {hour} часов.")
#     water += 1
#     food = int(input("Сколько Саша поглотил калорий? "))
#     calories += food
#     print()
#
# print(f"За время своего бодровствования Саша выпил {water} воды и уничтожил {calories} калорий!")
#
#
# # Unit 8.5 - task 1
# seconds = int(input("Введите количество секунд: "))
# for second in range(seconds, 0, -1):
#     print(second)
# print("Я иду искать!")
#
#
# # Unit 8.5 - task 2
# total_solders = int(input("Введите количество солдат: "))
# total_push_ups = 0
#
# for solder in range(total_solders - 4, 0, -4):
#     print(solder, "- номер солдата")
#     mil_rules = int(input("Введите количество правил в уставе: "))
#     answer = int(input("Боец! Сколько правил в уставе? "))
#     if answer != mil_rules:
#         push_ups = 10 * solder
#         total_push_ups += push_ups
#         print("Боец это не верно! Упал-отжался", push_ups, "раз!")
#
# print("Всего отжиманий было проивзедено:", total_push_ups)
#
#
# # Unit 8.5 - task 3
# seconds = int(input("Введите количество секунд: "))
#
# for second in range(seconds - seconds % 2, 0, -2):
#     print(second)
#
#
#_______________________ИТОГОВАЯ РАБОТА ДЛЯ СДАЧИ НА ПРОВЕРКУ_________________________________________
# # Final work - task 1
# buckwheat = 100
# month = 0
#
# for weight in range(buckwheat - 4, -1, -4):
#     month += 1
#     print("Через", month, "месяцев. Количество гречки будет равно:", weight, "кг.")
#
# print("Гречка закончилась!")


# # Final work - task 2
# debtors = int(input("Сколько всего должников? "))
# total_debt = 0
#
# for num_debt in range(0, debtors+1, 5):
#     print("Должник с номером:", num_debt,)
#     debt = int(input("Сколько Вы должны? "))
#     total_debt += debt
#
# print("Общая сумма долга:", total_debt)


# # Final work - task 3
# reverse_timer = int(input("Укажите время разогрева в секундах: "))
# for time in range(reverse_timer, -1, -1):
#     print("Оставшееся время до окончания приготовления:", time)
#     if time == 0:
#         print("Ваша еда готова, осторожно горячo!")
#         break
#     ready = int(input("Прервать режим разогрева? (0 - нет, 1 - да)" ))
#     if ready:
#         print("Ваша еда готова, можете забрать. Таймер был прерван на", reverse_timer - time, "секунде после начала.")
#         break


# # Final work - task 4
# a = int(input("Введите значение координаты a: "))
# b = int(input("Введите значение координаты b: "))
# c = int(input("Введите число с, которому должны быть кратны выбираемые числа: "))
# count = 0
# summ = 0
#
# for num in range(a - a % c, b + 1, c):
#     if num != 0:
#         print(num)
#         count += 1
#         summ += num
#
# print("Среднее арифметическое равно:", summ / count)


# # Final work - task 5
# start_segment = int(input("Введите начало отрезка: "))
# finish_segment = int(input("Введите конец отрезка: "))
# step = int(input("Введите шаг: "))
#
# for num in range(finish_segment, start_segment - 1, step):
#     y = num**3 + 2 * num**2 - 4 * num + 1
#     print("В точке", num, "функция равна", y)


# # Final work - task 6
# educational_grant = int(input("Введите стипендию: "))
# expenses = int(input("Введите расходы на проживание: "))
# summ_debt = 0
# for month in range(1, 10 + 1):
#     debt = expenses - educational_grant
#     summ_debt += debt
#     print(month, "месяц траты", expenses, "не хватает", summ_debt)
#     expenses += expenses * 3 / 100
#
# print("Нужно попросить у родителей", summ_debt, "рублей")
#
#
# # Final work - task 7
# n = int(input("Введите натуральное число N: "))
# summ = 0
# print("При N =", n, "элементы выражения будут равны:")
#
# for num in range(0, n):
#     print("n =", num)
#     elem = (-1)**num * 1 / (2**num)
#     print("elem = (-1) **", num, "* 1/2 **", num, "=", elem)
#     summ += elem
# print("Сумма равна:", summ)


# Final work - task 8
boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество девочек: "))
people = ""

if boys > 2 * girls or girls > 2 * boys:
    people = "нет решения"
else:
    if boys == girls:
        for human in range(1, boys + girls + 1, 2):
            people += "BG"
    elif boys > girls:
        while boys > girls:
            people += "BGB"
            boys -= 2
            girls -= 1
        for human in range(1, boys + girls + 1, 2):
            people += "BG"
    else:
        while boys < girls:
            people += "GBG"
            boys -= 1
            girls -= 2
        for human in range(1, boys + girls + 1, 2):
            people += "GB"

print("Ответ:", people)
