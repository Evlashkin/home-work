# # Unit 6.2 - task 1
# number = int(input("Введите число: "))
# summ = 0
#
# while number != 0:
#     summ += number
#     number = int(input("Введите число: "))
#
# print("Сумма всех введенных чисел составляет:", summ)
#
#
# # Unit 6.2 - task 2
# password = int(input("Введите пароль: "))
#
# while password != 235:
#     password = int(input("Вы ввели неверный пароль. Попробуйте еще раз: "))
#
# print("Пароль верный! Добро пожаловать!")
#
#
# # Unit 6.2 - task 3
# balance = 0
#
# while balance < 500000:
#     money = int(input("Какую сумму отложить? "))
#     balance += money
#
# print("Ты накопил нужную сумму! Можно ехать в салон за машиной. Накоплено:", balance)
#
#
# # Unit 6.3 - task 1
# temperature = int(input("Скалько градусов сейчас на улице? "))
# sum_meter = 0
#
# while temperature > 15:
#     sum_meter += 20
#     temperature -= 2
#     if temperature <= 15:
#         break
#     sum_meter += 10
# print(f"Спортсмен пробежал {sum_meter} метров")
#
#
# # Unit 6.3 - task 2
# number = int(input("Введите натуральное число: "))
# summ = 0
# while number != 0:
#     last_num = number % 10
#     if last_num == 5:
#         print("Обнаружен разрыв!")
#         break
#     summ += last_num
#     number //= 10
# print("Сумма чисел равна:", summ)
#
#
# # Unit 6.3 - task 3
# balance = int(input("Введите стартовую сумму: "))
#
# while balance != 0 and balance < 10000:
#     coube = int(input("Сколько выпало на кубике? "))
#     if coube == 3:
#         print("Вы все проиграли!")
#         balance = 0
#         break
#     balance += 500
#     print("Вы выиграли 500 рублей!")
# print("Игра закончена.")
# print(f"Итого осталось {balance} рублей")
#
#
# # Unit 6.4 - task 1
# count = 10
# while count >= 0:
#     if count == 0:
#         print(count)
#         print('Время вышло!')
#         break
#     else:
#         print(count)
#         count -= 1
#
#
# # Unit 6.4 - task 2
# work = True
# while work:
#     work = int(input("Продолжаем работать? 1/0 "))
# if not work:
#     print("Приложение закрывается...")
# print("Работа завершена")
#
#
# # Unit 6.4 - task 3
# code = 130716
# while True:
#     print("Комьютер заблокирован. Вернешь скейт - скажу код разблокировки!")
#     code_request = int(input("Введи код, подлый ты ублюдок: "))
#     if code_request == code:
#         print("Код верный. Завершаю работу...")
#         break
#
#
# # Unit 6.5 - task 1 - мой вариант решния
# text = "Я - программист"
# how_mach = int(input("Сколько раз вывести текст на экран? "))
# while how_mach:
#     print(text)
#     how_mach -= 1
#
# # Unit 6.5 - task 1 - так хочет заказчик
# text = "Я - программист"
# how_mach = int(input("Сколько раз вывести текст на экран? "))
# count = 0
# while count != how_mach:
#     print(text)
#     count += 1
#
#
# # Unit 6.5 - task 2
# how_much = int(input("Сколько раз Вам напомнить? "))
#
# while how_much:
#     print("Вы хотели не забыть о чем-то!")
#     how_much -= 1
#
#
# # Unit 6.5 - task 2
# bags_count = int(input("Сколько у вас мешков?"))
# count = 0
# total_weight = 0
#
# while count != bags_count:
#     weight = int(input("Введите вес мешка: "))
#     total_weight += weight
#     count += 1
#     print(f"Вы уже взвесили {count} мешков из {bags_count}")
# print(f"Общий вес мешков составляет: {total_weight}.")
