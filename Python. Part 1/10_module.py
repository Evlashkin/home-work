# # Unit 10.1 - task 1
# for num in range(1, 10):
#     print()
#     for sec_num in range(1, 10):
#         print(num * sec_num, end="\t")
#
#
# # Unit 10.1 - task 2
# n = int(input("Введите число N: "))
#
# for num in range(0, n + 1):
#     print()
#     for sec_num in range(0, n + 1):
#         print(num + sec_num, end="\t")
#
#
# # Unit 10.1 - task 3
# for num in range(10):
#     print()
#     for sec_num in range(10):
#         print(num - sec_num, end="\t")
#
#
# # Unit 10.2 - task 1
# n = int(input("Введите число N: "))
#
# for row in range(1, n + 1):
#     for col in range(1, n + 1):
#         if row % 2:
#             print(col, end="\t")
#         else:
#             print(row, end="\t")
#     print()
#
#
# # Unit 10.2 - task 2
# n = int(input("Введите число N: "))
#
# for row in range(1, n + 1):
#     for col in range(1, n + 1):
#         if col % 3 != 0:
#             print(row, end="\t")
#         else:
#             print(col, end="\t")
#     print()
#
#
# # Unit 10.2 - task 3
# for row in range(20):
#     if row != 9:
#         for col in range(50):
#             if col == 24:
#                 print("|", end="")
#             else:
#                 print(" ", end="")
#         print()
#     else:
#         for col in range(50):
#             print("-", end="")
#         print()
#
#
# # Unit 10.2 - task 3.1
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()
#
#
# # Unit 10.2 - task 3.2
# for row in range(20):
#     for col in range(50):
#         if col == 24:
#             print("|", end="")
#         elif row == 9:
#             print("-", end="")
#         else:
#             print(" ", end="")
#     print()
#
#
# # Unit 10.3 - task 1
# for row in range(20):
#     for col in range(30):
#         if row == 0:
#             print("-", end="")
#         elif col == 0 or col == 30 - 1:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()
#
#
# # Unit 10.3 - task 2
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == -row + 19:
#             print("/", end="")
#         elif col == row + 29:
#             print("\\", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()
#
#
# # Unit 10.3 - task 3
# size = int(input("Введите размер матрицы: "))
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if col + row == size + 1:
#             print(1, end=" ")
#         elif col + row > size + 1:
#             print(2, end=" ")
#         else:
#             print(0, end=" ")
#     print()
#
#
# # Unit 10.4 - task 1
# people = int(input("Введите количество людей в очереди: "))
#
# for hour in range(people):
#     print("Идет", hour, "час:")
#     for man in range(hour, people):
#         print("Сейчас", man, "человек в очереди")
#     print()
# print("Идет", people, "час: ")
# print("Очередь закончилась")
#
#
# # Unit 10.4 - task 2
# total_num = int(input("Сколько всего чисел будете вводить? "))
# count = 0
#
# for item in range(total_num):
#     num = input('Введите число: ')
#     for digit in num:
#         if int(digit) > 5:
#             count += 1
#
# print("Общее количество цифр больше 5 равно:", count)
#
#
# # Unit 10.4 - task 3
# n = int(input("Введите число: "))
#
# for row in range(n + 1):
#     for col in range(row, n + 1):
#         print(col, end=" ")
#     print()
#
#__________________________________________________________________________
# # Final work - task 1
# for row in range(0, 6):
#     for col in range(row, 11 + row, 2):
#         print(col, end="\t")
#     print()
#
#
# # Final work - task 2
# n = int(input("Введите число N: "))
#
# for row in range(1, n + 1):
#     for col in range(row):
#         print(row, end="\t")
#     print()
#
#
# # Final work - task 3
# width = int(input("Введите ширину рамки: "))
# height = int(input("Введите высоту рамки: "))
#
# for row in range(height):
#     for col in range(width):
#         if col == 0 or col == width - 1:
#             print("|", end="")
#         elif row == 0 or row == height - 1:
#             print("-", end="")
#         else:
#             print(" ", end="")
#     print()
#
#
# # Final work - task 4
# total_num = int(input("Введите количество чисел: "))
# count_denominator = 0
# count = 0
#
# for item in range(total_num):
#     num = int(input("Введите число: "))
#     count_denominator = 0
#     for denominator in range(1, num + 1):
#         if not num % denominator:
#             count_denominator += 1
#             if count_denominator >= 3:
#                 break
#     if count_denominator <= 2:
#         count += 1
#
# print("Количество простых чисел в последовательности:", count)
#
#
# # Final work - task 5
# total_num = int(input("Введите количество чисел: "))
# summ = 0
# new_summ = 0
# maximum = 0
#
# for item in range(total_num):
#     num = input("Введите число: ")
#     for digit in num:
#         new_summ += int(digit)
#     if new_summ > summ:
#         summ = new_summ
#         maximum = num
#     new_summ = 0
#
# print("Наибольшее число по сумме цифр:", maximum, "\nСумма цифр:", summ)
#
#
# # Final work - task 6
# height = int(input("Введите высоту пирамиды: "))
#
# for row in range(1, height * 2, 2):
#     for col in range(height * 2):
#         if col == height and row == 1:
#             print("#", end="")
#         elif (height - row // 2) <= col <= (height + row // 2) and row > 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
#
#
# # Final work - task 7
# height = int(input("Введите количество уровней пирамиды: "))
# num = 1
# for row in range(1, height + 1):
#     temp = row
#     for col in range(1, height + 1):
#         if temp == row:
#             print("\t" * (height - row), end="")
#         if row and col != 1:
#             print("\t", num, end="\t")
#             num += 2
#             row -= 1
#         elif row:
#             print(num, end="\t")
#             num += 2
#             row -= 1
#         else:
#             print("", end="\t")
#     print()
#
#
# # Final work - task 8
# n = int(input("Введите количество глубину ямы: "))
#
# for row in range(1, n + 1):
#     for col in range(1, n + 1):
#         if col > row:
#             print(".", end="")
#         else:
#             print(col, end="")
#     for col2 in range(n, 0, -1):
#         if col2 > row:
#             print(".", end="")
#         else:
#             print(col2, end="")
#     print()
