# # Unit 13.2 - task 1
# def summ_n(n):
#     summ = 0
#     for num in range(1, n + 1):
#         summ += num
#     return summ
#
# n = int(input("Введите число N: "))
# new_n = summ_n(n)
# print('Сумма чисел от 1 до N:', summ_n(n))
# print('Сумма чисел от 1 до суммы чисел от 1 до N: ', summ_n(new_n))
#
#
# Unit 13.2 - task 2
# def gcd(num1, num2):
#     # num1 = num2 * (num1 // num2) + num1 % num2
#     if num1 < num2:
#         num1, num2 = num2, num1
#     nod = num2
#     while num1 % num2:
#         nod = num1 % num2
#         num1 = num2
#         num2 = nod
#     return nod
#
#
# print(gcd(30, 70))
#
#
# # Unit 13.2 - task 3
# def lenght(num):
#     count = 1
#     while num // 10:
#         count += 1
#         num //= 10
#     return count
#
#
# def prioritet_task(tasks):
#     maxim = 0
#     first = 0
#     for task in range(tasks):
#         num = int(input('Введите число: '))
#         if num < 0:
#             num = 0
#         if lenght(num) > maxim:
#             maxim = lenght(num)
#             first = num
#     return first
#
#
# tasks = int(input("Введите количество задач: "))
# print("Первая задая на обработку:", prioritet_task(tasks))


# Unit 13.3 - task 1
# def must_small_num(n):
#     count = 0
#     while n != 0:
#         n /= 2
#         count += 1
#         print(n)
#     return count
#
#
# print("Количество итераций:", must_small_num(1))
#
#
# # Unit 13.3 - task 2
# def now_bigger_2(n):
#     x = 1
#     count = 0
#     while x < 2:
#         x += n
#         count += 1
#         print(x)
#     return count
#
#
# num = float(input("Введите число N в экспоненциальной форме: "))
# if 0 < num < 1:
#     print('Количство итераций для достижения 2 составляет:', now_bigger_2(num))
# else:
#     print("Формат ввода не соответствует условию.")
#
#
# # Unit 13.3 - task 3
# def float_point(num):
#     count = 0
#     mantissa = ''
#     other = ''
#     for item in str(num):
#         count += 1
#         if count == 1:
#             mantissa = item
#         else:
#             other += item
#     return str(f"{mantissa}.{other} * 10 ** {count - 1}")
#
#
# num = int(input('Введите целое число больше 10: '))
# if num > 10:
#     print(f"Формат плавующей точки: x = {float_point(num)}")
# else:
#     print('Вы ввели число, несоответствующее условиям')
#
#
# # Unit 13.3 - task 3.2
# def float_point(n):
#     count = 0
#     while n > 10:
#         count += 1
#         n /= 10
#     return str(f"{n} * 10 ** {count}")
#
#
# num = int(input('Введите любое число больше 10: '))
# if num > 10:
#     print(f"Формат плавующей точки: x = {float_point(num)}")
# else:
#     print('Вы ввели число, несоответствующее условиям')
#
#
# # Unit 13.4 - task 1
# def tax(balance, new_tax):
#     if balance + new_tax > balance:
#         print("Бюджет увеличится")
#     else:
#         print("Бюджет не изменится")
#
#
# balance = float(input("Введите бюджет страны в экспоненциальном формате: "))
# new_tax = float(input("Введите размер поступления нового налога: "))
#
# tax(balance, new_tax)
#
#
# # Unit 13.4 - task 2
# def eqv(first, second, third):
#     if round(first + second, 15) == round(third, 15):
#         return True
#     else:
#         return False
#
#
# print(eqv(1.1, 2.2, 3.3))
# print(eqv(1e-14, 1e-14, 3e-14))
#
#__________________________________________________________________________
# # Final work - task 1
# def float_point(num):
#     count = 0
#     if num >= 1:
#         while num > 10:
#             count += 1
#             num /= 10
#     else:
#         while num < 1:
#             num *= 10
#             count += 1
#     return str(f"{round(num, 15)} * 10 ** {count}")
#
#
# num = float(input("Введите положительное число: "))
# if num > 0:
#     print(float_point(num))
# else:
#     print("Введенное Вами число не является положительным.")
#
#
# # Final work - task 2
# def maximum_of_two(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
#
#
# def maximum_of_three(a, b, c):
#     temp_max = maximum_of_two(a, b)
#     if temp_max >= c:
#         return temp_max
#     else:
#         return c
#
#
# num_1 = float(input("Введите первое число: "))
# num_2 = float(input("Введите второе число: "))
# num_3 = float(input("Введите третье число: "))
#
# print("Наибольшее из трех чисел: ", maximum_of_three(num_1, num_2, num_3))
#
#
# # Final work - task 3
# def revers(num):
#     new_num = ''
#     for dig in str(num):
#         new_num = dig + new_num
#     return int(new_num)
#
#
# n = int(input('Введите первое число (N): '))
# k = int(input('Введите второе число (k): '))
#
# new_n = revers(n)
# new_k = revers(k)
# summ = new_n + new_k
# new_summ = revers(summ)
#
# print("Первое число наоборот:", new_n)
# print("Второе число наоборот:", new_k)
# print("Сумма:", summ)
# print("Сумма наоборот", new_summ)
#
#
# # Final work - task 4
# def count_numbers(num):
#     count = 0
#     for dig in str(num):
#         count += 1
#     return count
#
#
# def change_number(num):
#     digits_count = count_numbers(num)
#     last_digit = num % 10
#     first_digit = num // 10 ** (digits_count - 1)
#     between_digits = num % 10 ** (digits_count - 1) // 10
#     changed_num = last_digit * 10 ** (digits_count - 1) + between_digits * 10 + first_digit
#     return changed_num
#
#
# def main():
#     first_n = int(input("Введите первое число: "))
#     second_n = int(input("Введите второе число: "))
#
#     if count_numbers(first_n) < 3 or count_numbers(second_n) < 4:
#         print("Ошибка количество цифр в числах не соответствует условию.")
#     else:
#         print('Изменённое первое число:', change_number(first_n))
#         print('Изменённое второе число:', change_number(second_n))
#         summ = change_number(first_n) + change_number(second_n)
#         print('\nСумма чисел:', summ)
#
# main()
#
#
# # Final work - task 5
# def pendulum(start, finish):
#     count = 0
#     while start > finish:
#         start -= start * 8.4 / 100
#         count += 1
#     return count
#
#
# def main():
#     start_ampl = float(input("Введите начальную амплитуду: "))
#     finish_ampl = float(input("Введите амплитуду остановки: "))
#     print(f"Маятник считается остановившимся через {pendulum(start_ampl, finish_ampl)} колебаний")
#
#
# main()
#
#
# # Final work - task 6
# D = x ^ 3 − 3x ^ 2 − 12x + 10
# x - глубина кладки в метрах
# D - уровень опасности в условный единицах
# x > 0 and x < 4

# d = x ** 3 - 3 * x ** 2 - 12 * x + 10

start_border = 0
finish_border = 4
x = (finish_border - start_border) / 2

