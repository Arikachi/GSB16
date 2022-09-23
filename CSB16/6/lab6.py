#1
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr2 = []
# arr3 = []
# arr4 = []
# for i in arr:
#     arr2.append(i+2)
# for i in arr:
#     arr3.append(i*2)
# for i in range(len(arr)):
#     arr4.append(arr[i-8])
# print(arr2)
# print(arr3)
# print(arr4)

#2
# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l',
# 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
# word = ''
# for i in range(len(arr)):
#     word += arr[-(i+1)]
# print(word)

#3
# n = int(input("Input a positive number: "))
# F = [1, 1]
# a = n-2
# for i in range(a):
#     t = F[i] + F[i+1]
#     F.append(t)
# print(f'First {n} Fibonacci number(s): ', F)

#4
# list = (
#     tuple(("Ribeye Steak", 30.5)),
#     tuple(("Potato Salad", 5)),
#     tuple(("Sparkling Wine", 7)),
#     tuple(("Smoked Salmon", 12)),
#     tuple(("Chicken Soup", 8.5)),
#     tuple(("Tiramisu Cake", 4.5)),
# )
# s = 0
# for i in list:
#     s += i[1]
# avr = s/6
# print("Average price: ", avr)
# print("Item(s) above average price: ", end = '')
# for i in list:
#     if i[1] > avr:
#         print(i, end = ' ')

#5
# n = input("Write a sentence: ")
# list = n.split(' ')
# list2 = []
# a = 0
# b = 0
# for i in list:
#     if i != '':
#         list2.append(i)
#         for j in list2:
#             if i == j:
#                 b += 1
#         if b < 2:
#             a += 1
#             b = 0
# print(f"Number of unique words: {a}")