# # Unit 9.2 - task 1
# bad_grade_count = 0
#
# for student in range(5):
#     answer = input("Кто написал произведение 'Евгений Онегин'? ")
#     if answer == "Пушкин" or answer == "пушкин":
#         print("Верно!")
#         break
#     print("Не верно! Два!")
#     bad_grade_count += 1
#
# print("Количество двоечников равно:", bad_grade_count)
#
#
# # Unit 9.2 - task 2
# while True:
#     answer = input("Ты сделал работу, которую я давал тебе вчера? ")
#     if answer == "Конечно" or answer == "Да" or answer == "Сделал":
#         print("Так-то лучше!")
#         break
#
#
# # Unit 9.2 - task 3
# name = input("Как тебя зовут? ")
# bay_elephant = input(f"{name}, купи слона! ")
# while True:
#     bay_elephant = input(f"Все говорят: {bay_elephant}! А ты купи слона! ")
#
#
# # Unit 9.3 - task 1
# for symbol in "Python":
#     print(symbol)
#
#
# # Unit 9.3 - task 2
# text = input("Введите текст: ")
# for symbol in text:
#     print(symbol * 3)
#
#
# # Unit 9.3 - task 3
# text = input("Введите текст: ")
# small_sym_count = 0
# big_sym_count = 0
#
# for sym in text:
#     if sym == "ы":
#         small_sym_count += 1
#     if sym == "Ы":
#         big_sym_count += 1
#
# print("Больших букв Ы:", big_sym_count)
# print("Маленьких букв Ы:", small_sym_count)
#
#
# # Unit 9.4 - task 1
# print("-" * 10)
# for step in range(4):
#         print("|" + "0" * 8 + "|")
# print("-" * 10)


# # Unit 9.4 - task 2
# num = int(input("Введите первое число: "))
# step = int(input("Введите шаг: "))
# summ = 0
# print("Ваш IP-адрес:", end=" ")
#
# for item in range(3):
#     summ += num
#     print(num, end=".")
#     num += step
#
# print(summ)
# print("Можете подключать компьетеры к локальной сети")
#
#
# # Unit 9.4 - task 2
# num = int(input("Введите число: "))
# print('', end="-=- ")
# for item in range(10, num + 1, 10):
#     print(item, end=" -=- ")
#
#
#_______________________ИТОГОВАЯ РАБОТА ДЛЯ СДАЧИ НА ПРОВЕРКУ_________________________________________
# # Final work - task 1
# karamba_count = 0
#
# for man in range(10):
#     word = input("Введите слово: ")
#     if word == "Карамба" or word == "карамба":
#         karamba_count += 1
#
# print("Количество человек, попавших в команду:", karamba_count)
#
#
# # Final work - task 2
# text = input("Введите текст: ")
# count = 0
#
# for sym in text:
#     count += 1
#     if sym == '*':
#         print('Символ "*" стоит на позиции:', count)
#         break
#
#
# # Final work - task 3
# rows = int(input("Введите кол-во рядов: "))
# seats = int(input("Введите кол-во сидений в ряде: "))
# meter_between_rows = int(input("Введите кол-во метров между рядами: "))
#
# print("\nСцена\n")
# nominal_string = ("=" * seats + " ") + ("*" * meter_between_rows) + (" " + "=" * seats)
# for row in range(rows):
#     print(nominal_string)
#
#
# # Final work - task 4
# point_a = 8
# point_b = 10
#
# while True:
#     print("Марсоход находится на позиции", point_a, ",", point_b, end=", ")
#     command = input("введите команду: ")
#     if command == "W" or command == "w":
#         if point_b < 20:
#             point_b += 1
#     elif command == "S" or command == "s":
#         if point_b > 0:
#             point_b -= 1
#     elif command == "A" or command == "a":
#         if point_a > 0:
#             point_a -= 1
#     elif command == "D" or command == "d":
#         if point_a < 15:
#             point_a += 1
#
#
# # Final work - task 5
# text = input("Введите текст: ")
# length = 0
# max_length = 0
#
# for sym in text:
#     if sym != " ":
#         length += 1
#     else:
#         length = 0
#     if length > max_length:
#         max_length = length
#
# print("Самое длинное слово состоит из", max_length, "букв")
#
#
# # Final work - task 6
# cow_string = input("Введите строку в формате 'abab...' - где a - cвободное стойло, b -занятое:\n")
# milk = 0
# summ_milk = 0
#
# for cow in cow_string:
#     milk += 2
#     if cow == "b":
#         summ_milk += milk
#
# print("За день было произведено", summ_milk, "литров молока.")
#
#
# # Final work - task 7
# cipher = input("Введите зашифрованное сообщение: ")
# count = 0
# start = ""
# finish = ""
#
# for letter in cipher:
#     count += 1
#     if count % 2:
#         start += letter
#     else:
#         finish = letter + finish
#
# print("Расшифрованное сообщение:", start + finish)
