# # Unit 1.4 - task 1
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{j} * {i} = {i * j}", end="\t")
#     print()


# # Unit 1.4 - task 2
# print("Hello World! I am here!")
# num_a = int(input("Введите первое число: "))
# num_b = int(input("Введите второе число: "))
# operator = input("Ввдетите операцию: ")
# if operator == "+":
# 	result = num_a + num_b
# 	print(f"Результат вычисления: {result}")
# elif operator == "-":
# 	result = num_a - num_b
# 	print(f"Результат вычисления: {result}")
# elif operator == "*":
# 	result = num_a * num_b
# 	print(f"Результат вычисления: {result}")
# elif operator == "/":
# 	if num_b != 0:
# 		result = num_a / num_b
# 		print(f"Результат вычисления: {result}")
# 	else:
# 		print("На 0 делить нельзя!")
# else:
# 	print("Вы ввели недопустимую операцию")


# # Unit 1.4 - task 3
# op = input("Выберите операцию: ")
# result = 0
# flag = True
# expr = ""
#
# while (op != "+") and (op != "-") and (op != "*") and (op != "/"):
#     op = input("Выберите операцию: ")
# operand = int(input("Сколько операндов? "))
# first_num = float(input(f"Введите операнд 1: "))
# result = first_num
# expr = str(first_num)
#
# for item in range(2, operand + 1):
#     num = float(input(f"Введите операнд {item}: "))
#     expr += (" " + op + " " + str(num))
#
#     if op == "+":
#         result += num
#     elif op == "-":
#         result -= num
#     elif op == "*":
#         result *= num
#     else:
#         if num != 0:
#             result /= num
#         else:
#             print("На 0 делить нельзя!")
#             flag = False
#             break
#
# if flag:
#     print(f"Результат вычисления: {expr} = ", result)


# # Unit 1.5 - task 2
# def gcd(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print('Наибольший общий делитель:', a + b)
#
#
# gcd(4782, 698)


# # Unit 1.5 - task 3
# print("Введите первую точку")
# x1 = float(input('X: '))
# y1 = float(input('Y: '))
# print("\nВведите вторую точку")
# x2 = float(input('X: '))
# y2 = float(input('Y: '))
#
# x_diff = x1 - x2
# y_diff = y1 - y2
#
# if x_diff != 0:
#     k = y_diff / x_diff
#     b = y2 - k * x2
#     print("Уравнение прямой, проходящей через эти точки:")
#     print("y = ", k, " * x + ", b)
# else:
#     print("Уравнения прямой не существует.")
#


