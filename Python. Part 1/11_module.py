# # Unit 11.2 - task 1
# bet = float(input("Сколько ставим? "))
# k = float(input("Какой коэффициент? "))
#
# win = round(bet * k, 2)
#
# print("В положительном случае, Ваш выигрыш составит:", win)
#
#
# # Unit 11.2 - task 2
# age = int(input("Введите возраст: "))
# temp = float(input("Введите температуру тела: "))
# k = 1.5
#
# present = round(k * age * temp, 2)
#
# print("Сумма подарка составляет:", present)
#
#
# # Unit 11.2 - task 3
# height = float(input("Введите рост: "))
# weight = float(input("Введите вес: "))
#
# bmi = round(weight / height**2, 2)
#
# if bmi < 18.5:
#     print("Недостаточная масса тела. BMI =", bmi)
# elif bmi < 25:
#     print("Нормальная масса тела. BMI =", bmi)
# elif bmi < 30:
#     print("Избыточная масса тела. BMI =", bmi)
# else:
#     print("Ожирение.  BMI =", bmi)
#
#
# # Unit 11.3 - task 1
# chatle = int(input("Введите количество чатлов: "))
#
# cr = chatle / 2200
#
# print("Это", cr, "CR")
# print("Можно купить", int(cr * 2), "кораблей")
#
#
# # Unit 11.3 - task 2
# print("Введите местоположение фигуры в метрах")
# x = float(input("По горизонтали: "))
# y = float(input("По вертикали: "))
#
# if x > 0.8 or y > 0.8:
#     print("Клетки с такой координатой не существует")
# else:
#     xSquare = int(x * 10)
#     ySquare = int(y * 10)
#     print(f"Фигура находится в клетке ({xSquare}, {ySquare})")
#
#
# # Unit 11.3 - task 2
print("Введите местоположение фигуры в метрах")
x = float(input("По горизонтали: "))
y = float(input("По вертикали: "))

if x > 0.8 or y > 0.8:
    print("Клетки с такой координатой не существует")
else:
    xSquare = int(x * 10)
    ySquare = int(y * 10)
    xtemp = (50 - int(x * 1000 % 100))/1000
    ytemp = (50 - int(y * 1000 % 100))/1000
    print(f"Фигура находится в клетке ({xSquare}, {ySquare})")
    print(f"Поправьте положение фигуры на ({xtemp}, {ytemp})")
