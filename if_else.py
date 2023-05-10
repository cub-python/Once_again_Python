# # Программа получает на вход список и удаляет потоврящейся элементы, выодит
# # новый спиок
#
# # elements = list(map(int, input().split()))
# # if 2 in elements:
# #     elements.remove(2)
# # if 9 in elements:
# #     elements.remove(9)
# # if 17 in elements:
# #     elements.remove(17)
# # print(elements)
# # elemens = 1 23 56 9 14 17
# # [1, 23, 56, 14]
#
# # Морожевой оператор
# '''
# Благодаря моржу можно выполнить присвоение и вывод в одну строку
# '''
# print(see_walrus := "Posmotri  na moiu morju, kakoi on  krasivyi")
# print(see_walrus[:18] + 'loshadku')
#
# """
# Morja mojno uvidet i vnutri uslovii
# """
# # bez morja
# words = input("Vvedite slova cherez probel: ").split()
# count = len(words)
# if count > 3:
#     print(f" Ogo skolko slov vy znaete, aj {count}")
# else:
#     print(f"Slovarnyi zapas popolnit nado, {count} eto malovato")
#
#
# # s morjom
#
# words_two = input("Vvedite slova cherez probel: ").split()
#
# if(count := len(words_two)) > 3:
#    print(f" Ogo skolko slov vy znaete, aj {count}")
# else:
#     print(f"Slovarnyi zapas popolnit nado, {count} eto malovato")
#
# # iz frazy nahodim slovo
# # Python стал одним из самых популярных языков
#
# # word = 'Python стал одним из самых популярных языков'
#
# if 'Python' in (word := input()):
#     print('Нашли слово Python')
# else:
#     print('Не нашли')
#
#

# Operactia c 6 znachnymi ctiframi

# numbers = int(input())
#
# num1 = numbers % 10
# num2 = numbers // 10 % 10
# num3 = numbers // 100 % 10
# num4 = numbers // 1000 % 10
# num5 = numbers // 10000 % 10
# num6 = numbers // 100000
#
# if num6 + num5 + num4 == num3 + num2 + num1:
#     print('yes')
# else:
#     print('no')


# # Shahmatnaya doska
#
# letters = '_abcdefgh'
#
# position1 = input()
# position2 = input()
#
# letter1 = position1[0]
# letter2 = position2[0]
#
# column1 = letters.find(letter1)
# column2 = letters.find(letter2)
#
# row1 = int(position1[1])
# row2 = int(position2[1])
#
# if(row1 + column1) % 2 == (row2 + column2) % 2:
#     print('YES')
# else:
#     print('NO')

# TERNARNYI OPERATOR

# condition - logich vyrajenie kotoroe prinimaet TRUE ili FALSE

# prostoi primer
# if age >= 18:
#     price_ticket = 20
# else:
#      price_ticket = 10

# # primer cherez ternarnyi operator
#
# age = int(input("Vvedite vash vozrast: "))
# price_ticket = 20 if age >= 18 else 10
# print(f"Sctena bileta sostavit {price_ticket} rubl.")

# minimum or maximum

minimum = int(input())  # 900
maximum = int(input())  # 300

print(minimum, maximum) if minimum < maximum else print(maximum, minimum)  # 300  900

