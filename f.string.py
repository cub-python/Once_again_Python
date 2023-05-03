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

print(total)  # По курсу валюты 89.2 вы можете купить 356.80 валют


"""
Программа перевода значения секунд в значение в минут опр формата.
"""

user_secund = int(input('Введите вещественное число: '))
minut = user_secund // 60
remainder_in_secunds = user_secund % 60
result = f"""{user_secund} сек. - это {minut} мин. {remainder_in_secunds} сек."""

print((result))  # 89 сек. - это 1 мин. 29 сек.


# Вывод переменных
num_one = 11
num_two = 17
print(f"num_one = {num_one}, num_two = {num_two}")  # num_one = 11, num_two = 17

print(f"Переменные({num_one = }, {num_two = }")  # num_one = 11, num_two = 17

# Формат вывода дробной части с помошью f-строки

num_pi = 3.141592653589793
print(f'{num_pi: .6f}')  # 3.141592
