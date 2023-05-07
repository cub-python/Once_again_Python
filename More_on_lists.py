# # Списки представляют собой упорядоченные коллекции элементов.
# # Они позволяют хранить в одном месте взаимосвязанные данные
#
#
#
# num_list = [2, 'ffadf', 45, 'fewf', 98]
# print(type(num_list))  # <class 'list'>
#
# new_list = num_list * 3
# print(new_list)  # [2, 'ffadf', 45, 'fewf', 98, 2, 'ffadf', 45, 'fewf', 98, 2, 'ffadf', 45, 'fewf', 98]
#
# numbers = [4, -89, 789, 3215, -2, 45219, 5654]
# min_num = (min(numbers))
# max_num = (max(numbers))
#
# print(min_num, max_num)  # -89 45219
#
# # Programma ishet element v spiske i esli nahodit True, net vyvodit False
#
# print(777 in numbers) # False
# print(-89 in numbers)  # True
#
# # Ishem is spiska usera
#
# my_list = list(map(int, input().split()))  # 56 56 56 35
# print(45 in my_list)  # False
# # 45 65 32 1   # True
#
#
# # Summa spiska
# print(sum(numbers))  # 54790
#
# # Poisk v spiske
#
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# add_el = ['zero']
# months = add_el + months
# users_num = int(input())
# print(months[users_num])

# Otsortirovat spisok v poryadkew ubyvania
#
# new_numbers = [-345, 45, 987, 236, -45, 1, 45, 321, -254, 11, -10, 876]
# new_numbers.sort(reverse=True)
# print(new_numbers)  # [987, 876, 321, 236, 45, 45, 11, 1, -10, -45, -254, -345]
#
# new_numbers.sort(reverse=False)
# print(new_numbers)  # [-345, -254, -45, -10, 1, 11, 45, 45, 236, 321, 876, 987]


# Pereobrazovanie fraz

# You can go to hone
user_text = "You can go to hone"
user_text = user_text.upper()
user_text = user_text.split()

word1 = list(user_text[0])
word2 = list(user_text[1])
word3 = list(user_text[2])
word4 = list(user_text[3])
word5 = list(user_text[4])


print(user_text)

print('-'.join(word1), '-'.join(word2), '-'.join(word3), '-'.join(word4), '-'.join(word5))



