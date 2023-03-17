# # Unit 2.1 - task 1
# numbers_list = [3, 7, 5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers_list.append(number)
#     print('Текущий список чисел:', numbers_list)
#     for i in numbers_list:
#         print(i ** 2, i ** 3, i ** 4)
#     print()
#
#
# # Unit 2.1 - task 2
# numbers = []
# for num in range(0, 101):
#     numbers.append(num)
# print(numbers)
#
#
# # Unit 2.1 - task 3
# workersID_list = []
# workers_count = int(input("Какое количество сотрудников? "))
# for _ in range(0, workers_count):
#     worker_id = int(input("Введите ID сотрудника: "))
#     workersID_list.append(worker_id)
# worker_found = int(input("Какой ID ищем? "))
# if worker_found in workersID_list:
#     print("Сотрудник на рабочем месте.")
# else:
#     print("Сотрудник не работает.")
#
#
# # Unit 2.2 - task 1
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = nums_list[0]
# minimum = nums_list[0]
#
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#     if minimum > i:
#         minimum = i
#
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)
#
#
# # Unit 2.2 - task 2
# numbers_list = []
# count_num = int(input("Введите количество чисел: "))
#
# for _ in range(count_num):
#     new_num = int(input("Введите число: "))
#     numbers_list.append(new_num)
#
# div = int(input("Введите делитель: "))
# index_sum = 0
#
# for i in range(count_num):
#     if numbers_list[i] % div == 0:
#         print(f"Индекс числа {numbers_list[i]}: {i}")
#         index_sum += i
#
# print("Сумма индексов:", index_sum)
#
#
# # Unit 2.2 - task 3
# dogs_score = []
# N = int(input('Кол-во собак в списке: '))
#
# for _ in range(N):
#     score = int(input('Очередной балл собаки: '))
#     dogs_score.append(score)
#
# maximum = dogs_score[0]
# minimum = dogs_score[0]
# max_i = 0
# min_i = 0
#
#
# for i in range(N):
#     if maximum < dogs_score[i]:
#         maximum = dogs_score[i]
#         max_i = i
#     if minimum > dogs_score[i]:
#         minimum = dogs_score[i]
#         min_i = i
#
# print("До дебага:", dogs_score)
# dogs_score[max_i], dogs_score[min_i] = dogs_score[min_i], dogs_score[max_i]
# print("Дебаг произведен:", dogs_score)
#
#
# # Unit 2.3 - task 1
# string = list(input("Введите строку: "))
# count_replace = 0
# print("Исправленная строка: ", end='')
# for sym in string:
#     if sym == ":":
#         sym = ";"
#         count_replace += 1
#     print(sym, end="")
# print("\nКоличество замен:", count_replace)
#
#
# # Unit 2.3 - task 2
# string = input("Введите строку: ")
# sym = int(input("Номер символа: "))
#
# print("Символ слева:", string[sym - 2])
# print("Символ справа:", string[sym])
#
# if string[sym-1] == string[sym - 2] and string[sym-1] == string[sym]:
#     print("Есть два таких же символа")
# elif string[sym-1] == string[sym - 2] or string[sym-1] == string[sym]:
#     print("Есть ровно один такой же символ")
# else:
#     print("Одинаковых символов нет")
#
#
# # Unit 2.3 - task 3
# words = []
# text = []
# count_w_in_t = [0, 0, 0]
# for i in range(3):
#     word = input(f"Введите {i + 1} слово: ")
#     words.append(word)
#
# print()
# while True:
#     word_from_text = input("Слово из текста: ")
#     if word_from_text == "end":
#         break
#     text.append(word_from_text)
#
# for word in text:
#     if word == words[0]:
#         count_w_in_t[0] += 1
#     elif word == words[1]:
#         count_w_in_t[1] += 1
#     elif word == words[2]:
#         count_w_in_t[2] += 1
#
# print()
# print("Подсчет слов в тексте:")
# print(words[0], ":", count_w_in_t[0])
# print(words[1], ":", count_w_in_t[1])
# print(words[2], ":", count_w_in_t[2])
#
#
# # Unit 2.4 - task 1
