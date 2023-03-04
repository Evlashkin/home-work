# MyProfile app


# Функция для вывода личной информации о пользователе
def private_information(user_name, user_age, user_phone, user_email, user_postcode, user_postal_address, other):
    if 11 <= user_age % 100 <= 19:
        years_parameter = 'лет'
    elif user_age % 10 == 1:
        years_parameter = 'год'
    elif 2 <= user_age % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print(
        f"{separator}\n"
        f"Имя:      {user_name}\n"
        f"Возраст:  {user_age} {years_parameter}\n"
        f"Телефон:  {user_phone}\n"
        f"E-mail:   {user_email}\n"
        f"Индекс:   {user_postcode}\n"
        f"Адрес:    {user_postal_address}"
    )
    if other:
        print(f"Дополнительная информация:\n{other}")


# Функция для вывода информации о предпринимателе
def entrepreneur_information(ogrnip, inn, checking_account, bank_name, bik, correspondent_account):
    print(
        f"\nИфнормация о предпринимателе\n"
        f"ОГРНИП:   {ogrnip}\n"
        f"ИНН:      {inn}\n"
        f"Банковские реквизиты\n"
        f"Р/с:      {checking_account}\n"
        f"Банк:     {bank_name}\n"
        f"БИК:      {bik}\n"
        f"К/с:      {correspondent_account}"
    )


def main():
    # base general info
    name = ''
    age = 0
    phone_number = ''
    email = ''
    postcode = ''
    postal_address = ''
    other_information = ''

    # base entrepreneur info
    ogrnip = 0
    inn = 0
    checking_account = 0
    bank_name = ''
    bik = 0
    correspondent_account = 0

    while True:
        print(separator)
        print('ГЛАВНОЕ МЕНЮ')
        print('1 - Ввести или обновить информацию')
        print('2 - Вывести информацию')
        print('0 - Завершить работу')

        option_1 = int(input('Введите номер пункта меню: '))
        if option_1 == 0:
            break
        elif option_1 == 1:

            while True:
                print(separator)
                print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
                print('1 - Личная информация')
                print('2 - Информация о предпринимателе')
                print('0 - Назад')

                option_2 = int(input('Введите номер пункта меню: '))
                if option_2 == 0:
                    break
                elif option_2 == 1:
                    # input general info

                    name = input('Введите имя: ')
                    while True:
                        # validate user age
                        age = int(input('Введите возраст: '))
                        if age > 0:
                            break
                        print('Возраст должен быть положительным')

                    phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                    phone_number = ''
                    for symbol in phone:
                        if symbol == '+' or ('0' <= symbol <= '9'):
                            phone_number += symbol

                    email = input('Введите адрес электронной почты: ')

                    postcode = input('Введите почтовый индекс: ')
                    postcode_temp = ''
                    for symbol in postcode:
                        if '0' <= symbol <= '9':
                            postcode_temp += symbol
                    postcode = postcode_temp

                    postal_address = input('Введите почтовый адрес (без индекса): ')

                    other_information = input('Введите дополнительную информацию:\n')

                elif option_2 == 2:
                    # input entrepreneur info

                    while True:
                        ogrnip = int(input("Введите ОГРНИП: "))
                        if ogrnip // 10**14 in range(1, 10):
                            break
                        else:
                            print("ОГРНИП должен содержать 15 цифр")

                    inn = int(input("Введите ИНН: "))

                    while True:
                        checking_account = int(input("Введите рассчетынй счет: "))
                        if checking_account // 10**19 in range(1, 10):
                            break
                        else:
                            print("Рассчетный счет должен содержать 20 цифр")

                    bank_name = input("Введите название банка: ")

                    bik = int(input("Введите БИК: "))

                    correspondent_account = int(input("Введите корреспондентский счет: "))

                else:
                    print('Введите корректный пункт меню')

        elif option_1 == 2:
            # submenu 2: print info
            while True:
                print(separator)
                print('ВЫВЕСТИ ИНФОРМАЦИЮ')
                print('1 - Личная информация')
                print('2 - Вся информация')
                print('0 - Назад')

                option_3 = int(input('Введите номер пункта меню: '))
                if option_3 == 0:
                    break

                elif option_3 == 1:
                    private_information(name, age, phone_number, email, postcode, postal_address, other_information)

                elif option_3 == 2:
                    private_information(name, age, phone_number, email, postcode, postal_address, other_information)
                    entrepreneur_information(ogrnip, inn, checking_account, bank_name, bik, correspondent_account)

                else:
                    print('Введите корректный пункт меню')
        else:
            print('Введите корректный пункт меню')


print("Приложение MyProfile\n"
      "Сохраняй информацию о себе и выводи ее в разных форматах")
separator = '------------------------------------------'
main()
