# # Unit 3.2- task 1
# zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
# zoo.insert(1, 'bear')
# zoo.remove('elephant')
# print(zoo)
# print(f"Лев сидит в клетке №{zoo.index('lion') + 1}")
# print(f"Обезьяна сидит в клетке №{zoo.index('monkey') + 1}")


# Unit 3.2- task 2
# work_and_salary_list = []
#
#
# def workers_and_salary(n):
#     for worker in range(1, n + 1):
#         salary = int(input(f"Зарплата {worker} сотрудника: "))
#         work_and_salary_list.append(salary)
#
#     count_zero = 0
#     for i in work_and_salary_list:
#         if i == 0:
#             count_zero += 1
#     for _ in range(count_zero):
#         work_and_salary_list.remove(0)
#
#
# worker_count = int(input("Кол-во сотрудников: "))
#
# workers_and_salary(worker_count)
#
# print("Осталось сотрудников:", len(work_and_salary_list))
# print("Зарплаты:", work_and_salary_list)
# print("Минимальная зарплата сотрудников:", min(work_and_salary_list))
# print("Максимальная зарплата сотрудников:", max(work_and_salary_list))


# Unit 3.2- task 3
# def rating(total_list):
#
#     my_list = []
#
#     while True:
#         print("Ваш текущий топ фильмов:", my_list)
#         film = input("Название фильма: ")
#         if film not in total_list:
#             print("Такого фильма нет нашем сайте")
#             continue
#         print("Команды: добавить, вставить, удалить, выйти")
#         command = input("Введите команду: ")
#
#         if command == "добавить":
#             if film in my_list:
#                 print("Данный фильм уже есть в Вашем списке.")
#             else:
#                 my_list.append(film)
#         elif command == "вставить":
#             if film in my_list:
#                 print("Данный фильм уже есть в Вашем списке.")
#             else:
#                 place = int(input("Введите номер места в Вашем топе: "))
#                 my_list.insert(place - 1, film)
#         elif command == "удалить":
#             if film in my_list:
#                 my_list.remove(film)
#             else:
#                 print("Этого фильма нет в Вашем списке.")
#         elif command == "выйти":
#             break
#         else:
#             "Команда отсутствует!"
#
# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня',
#     'Проклятый остров', 'Начало', 'Матрица'
# ]
#
# rating(films)


# Unit 3.3- task 1
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
#
# main.extend(first_company)
# main.extend(second_company)
# main.extend(third_company)
#
# print("Общий список задач:", main)
# print("Количество невыполненных задач:", main.count(0))


# Unit 3.3 - task 2
# first_msg = input("Первое сообщение: ")
# second_msg = input("Второе сообщение: ")
#
# first_count_sym = first_msg.count("!") + first_msg.count("?")
# second_count_sym = second_msg.count("!") + second_msg.count("?")
#
# if first_count_sym > second_count_sym:
#     print("Третье сообщение:", first_msg + second_msg)
# elif first_count_sym < second_count_sym:
#     print("Третье сообщение:", second_msg + first_msg)
# else:
#     print("Ой")

# Unit 3.3 - task 3
# pacs_count = int(input("Кол-во пакетов: "))
# pac_list = []
# decod_list = []
# bad_pac = 0
# for i_pac in range(1, pacs_count + 1):
#     print("\nПакет номер", i_pac)
#     for i_bit in range(1, 5):
#         bit = int(input(f"{i_bit} бит: "))
#         pac_list.append(bit)
#     if pac_list.count(-1) <= 1:
#         decod_list.extend(pac_list)
#     else:
#         bad_pac += 1
#         print("Много ошибок в пакете.")
#     pac_list = []
#
# print("\nПолученное сообщение:", decod_list)
# print("Кол-во ошибок в сообщении:", decod_list.count(-1))
# print("Кол-во потерянных пакетов:", bad_pac)


# Unit 3.4 - task 1
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i_list in matrix:
#     for element in i_list:
#         print(element, end="    ")
#     print()


# Unit 3.4 - task 2
# participants = int(input("Кол-во участников: "))
# commands = int(input("Кол-во человек в команде: "))
# part_list = []
# num = 1
#
# for _ in range(participants // commands):
#     command = list(range(num, num + 4))
#     part_list.append(command)
#     num += 4
#
# print("Общий список команд:", part_list)


# Unit 3.4 - task 3
# def good_add():
#     good = []
#     fruit = input("Новый фрукт: ")
#     price = float(input("Цена: "))
#     good.append(fruit)
#     good.append(price)
#     goods.append(good)
#     print("Новый ассортимент:", goods)
#
#
# def price_up(perc):
#     for good in goods:
#         good[1] *= (1 + (perc / 100))
#         good[1] = round(good[1], 2)
#     print("Новый ассортимент с увел. ценой:", goods)
#
#
# goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
#
# good_add()
# price_up(8)


