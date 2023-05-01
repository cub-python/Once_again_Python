# f-Strings: новый и улучшенный способ форматирования строк в Python

user_name = input('What is your name:  ')
age = input('How old are you: ')
total_word = f"""Hi {user_name}. You are {age} old, its very good"""

print(total_word)

"""
Программа запрашивает курс доллара(float) и кол-во(int)которое юзер 
хочеть.В итоге выводит сообщение.
"""
current = float(input('Введите курс валты: '))
to_bue = int(input('Какое количество хотите купить ?: '))
must_pey = current * to_bue
total = f"""По курсу валюты {current} вы можете купить {'%.2f'% must_pey} валют"""

print(total)


"""
Программа перевода значения секунд в значение в минут опр формата.
"""

user_secund = int(input('Введите вещественное число: '))
minut = user_secund // 60
remainder_in_secunds = user_secund % 60
result = f"""{user_secund} секунда - это {minut} мин. {remainder_in_secunds} сек."""

print((result))