# Строки и методы строк
"""
При вызове методов необходимо помнить, что строки в Python относятся к
категории неизменяемых последовательностей, то есть все
функции и методы могут лишь создавать новую строку.
"""

your_comment = "This is your short comment"

print(your_comment)  # This is your short comment

print(your_comment[2])  # i
print(your_comment[0:])  # This is your short comment
print(your_comment[1:11])  # his is you
print(your_comment[:18])  # This is your short

print(id(your_comment))  #  139678391139536

print(len(your_comment))  # 26

print(your_comment.replace('short', 'long'))  # This is your long comment

print(your_comment.upper())  # THIS IS YOUR SHORT COMMENT
print(your_comment.lower())  # this is your short comment
print(your_comment.count('is'))  # 2 находит колич символа

new_comment = "THIS IS YOUR SHORT COMMENT"
print(new_comment.capitalize())  # This is your short comment
print(your_comment.index('s'))  # 3

# Форматирование строк.
# Программа считывает слово потом выводит

user_word = input('Скажите скороговорку: ')
question = 'Уух тыы,'
total_word = 'какое интересное скороговорка'

print(question + ' ' + user_word + ' ' + total_word)

