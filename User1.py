# num_1 = int(input("Введите 1 число "))
# num_2 = int(input("Введите 2 число "))
#
#
# if num_1 < num_2:
#     start_1 = num_1
#     finish_1 = num_2
# else:
#     start_1 = num_2
#     finish_1 = num_1
# for i in range(start_1, finish_1 + 1, 2):
#     print(i)

# четное, нечетное
# def my_function(number):
#     if number%2 == 0:
#      print("odd")
#     else:
#         print("even")
#         return
#
#
# my_function(number=int(input()))

# возврат дня недели по числу в диапазоне

# def my_function(day):
#     weekly = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
#     if day in range(0, 7):
#         print(weekly[day])
#     else:
#         print('Нет такого дня недели')
#
#
# my_function(day=int(input()))

# Срез из списка
# [5, 4, 2, 3, 1]
# >>> print(lst[1:4])
# [3, 2, 4]

# f списки
# x = 10
# y = 25
# print(f"x = {x}, y = {y}")
# x = 10, y = 25


# При наличии строки вы должны вернуть строку, в которой каждый символ (с учетом регистра) повторяется один раз.

# def my_function(word):
#     a = len(word)
#     for i in range(a):
#         print(word[i]*2, end='')
#
#
# my_function(word=str(input()))

# создание списка через ввод
# def my_function():
#     sp = list(input())
#     print(sp)
#     print(sp[2])
#
#
# my_function()

# развернуть число через текстовые операции

def my_function(inv):
    inv_str = str(inv)
    s_inv = list(inv_str)
    s_inv.reverse()
    print(s_inv)


my_function(inv=int(input()))