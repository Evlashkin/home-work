# # Unit 5.2 - task 1
# name = input("Enter your name: ")
# order_num = int(input("Enter your order number: "))
#
# hello_str = "Hello, {name}! Your order number: {order_num}. Good luck!".format(
#     name=name,
#     order_num=order_num
# )
# print(hello_str)


# # Unit 5.2 - task 2
# freind_name = input("Enter name of your friend: ")
# debt = int(input("Enter sum of {name} debt: ".format(name=freind_name)))
#
# #Том! Том, привет! Как дела, Том? Где мои 100 рублей? Том!
# prompt = "{0}! {0}, hello! How are you, {0}? Where is my {1} rubles? {0}!".format(
#     freind_name,
#     debt
# )
# print(prompt)


# # Unit 5.2 - task 3
# contain_ip = []
# for i in range(1, 5):
#     num = int(input("Enter {0} num for IP: ".format(i)))
#     while 0 > num or num > 255:
#         num = int(input("Enter num in range (0 - 255): "))
#     else:
#         contain_ip.append(num)
#
# ip_address = "{}.{}.{}.{}".format(*contain_ip)
# print("Your IP-address:", ip_address)


# # Unit 5.3 - task 1
# def replit_count(words_list, text):
#     total_replit_list = []
#     for word in words_list:
#         count = 0
#         for other_word in text.split():
#             if word == other_word:
#                 count += 1
#         new_note = ': '.join([word, str(count)])
#         total_replit_list.append(new_note)
#     return total_replit_list
#
#
# words_list = input("Введите 3 слова используя ', ' в качестве разделителей: ").split(', ')
# text = input("Введите текст произведения в одну строку: ")
#
# punkt_list = ['.', ',', ':', ';', '-']
#
# new_text = "".join([sym if sym not in punkt_list else '' for sym in text])
#
# print("Повторения слов (Слово: кол-во повторений):", "; ".join(replit_count(words_list, new_text)))


# # Unit 5.3 - task 2
# def remove_space(text):
#     new_text = ' '.join(text.split())
#     print(new_text)
#
#
# text = input("Введите текст: ")
# remove_space(text)


# # Unit 5.3 - task 3
# congat_format = input("Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: "
#                       "Например: С днём рождения, {name}! С {age}-летием тебя!: ")
# people_list = input("Введите список людей через запятую, в формате (Имя Фамилия): ").split(', ')
# ages_list = input("Введите возраст людей через пробел: ").split()
# people_age_list = []
# for index in range(len(people_list)):
#     print(congat_format.format(
#         name=people_list[index],
#         age=ages_list[index]
#         ))
#     people_age = ' '.join([people_list[index], str(ages_list[index])])
#     people_age_list.append(people_age)
#
# print("Именниники:", ', '.join(people_age_list))


# # Unit 5.4 - task 1
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# text = input("Введите текст, который необходимо зашифровать: ")
# shift = int(input("Введите сдвиг шифровки: "))
# cesar_text = [alphabet[(alphabet.index(i) + shift) % len(alphabet)] if i != ' ' else ' ' for i in text.lower()]
# print(''.join(cesar_text))


# # Unit 5.4 - task 2
# path_to_file = input("Введите путь до файла: ")
# disk = input("На каком диске должен лежать файл? ")
# extension = input("Какое должно быть расширение? ")
# if not path_to_file.endswith(extension):
#     print("Расширение файла не соответствует требуемому")
# elif not path_to_file.startswith(disk):
#     print("Файл на диске {} отсутсвует".format(disk))
# else:
#     print("Путь корректен!")


# # Unit 5.4 - task 3
alphabet_low = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_high = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
count_low = 0
count_high = 0
text = input("Введите текст: ")
for sym in text:
    if sym in alphabet_low:
        count_low += 1
    elif sym in alphabet_high:
        count_high += 1

if count_low > count_high:
    print(text.lower())
elif count_high > count_low:
    print(text.upper())
else:
    print("Количество прописных букв равно количеству строчных")
    print(text)