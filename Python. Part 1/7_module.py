# # Unit 7.2 - task 1
# for meters in 100,90,95,87,102:
#     if meters % 3 == 0:
#         print(meters, 'Подходит')
#     else:
#         print(meters, 'Не подходит')
#
#
# # Unit 7.2 - task 2
# for num in 3, 7, 5, 6, 4:
#     print(num**2, num**3, num**4)
#
#
# # Unit 7.2 - task 3
# winners = 0
#
# for ticket in 345, 19, 87, 1020, 421, 766, 234235, 2589, 555:
#     if 100 <= ticket <= 999 and ticket % 5 == 0:
#         print(f"Happy ticket - {ticket}")
#         winners += 1
#
# print(f"Количество победителей: {winners}")
#
#
# # Unit 7.3 - task 1
# for num in range(11):
#     print(num**2)
#
#
# # Unit 7.3 - task 2
# how_much_hours = int(input("Который час? "))
# for hour in range(how_much_hours):
#     print("Ку-ку!")
#
#
# # Unit 7.3 - task 3
# for item in range(21):
#     print(2**item)
#
#
# # Unit 7.4 - task 1
# for item in range(1, 11):
#     print(item**3)
#
#
# # Unit 7.4 - task 2
# first_num = int(input("Введите первое число: "))
# second_num = int(input("Введите второе число: "))
# summ = 0
#
# for num in range(first_num, second_num + 1):
#     summ += num
# print("Сумма чисел от", first_num, "до", second_num, "равна", summ)


# Unit 7.4 - task 3
up = int(input("Введите время подъема Саши: "))
total_hours = 0
total_calories = 0

for hours in range(up, 23):
    print(f"Сейчас {hours} часов")
    calories = int(input("Сколько калорий съел Саша? "))
    total_calories += calories
    if total_calories > 2000:
        print("Поели, теперь можно и поспать")
        break
    total_hours += 1

print("Саша был бодрым", total_hours, "часов.")
print("За это время он съел", total_calories, "калорий")
