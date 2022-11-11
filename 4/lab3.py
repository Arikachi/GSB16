#1
# num = int(input('Input number '))
# if num%2 == 0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd')

#2
# import math
# def interger(n):
#     check = 1
#     if (math.ceil(n) != math.floor(n)):
#         check = 0
#     return check
# n = float(input("Input number: "))
# if interger(n) == 1:
#     print(n," is an interger")
# else:
#     print(n," is not an interger")

# num = float(input('Input number: '))
# if int(num) == num:
#     print(num," is an interger")
# else:
#     print(num," is not an interger")

#3
# c = input('Input character: ')
# try:
#     check = int(c)
#     print(f'{c} is a digit')   
# except ValueError:
#     try:
#         check = float(c)
#         print(f'{c} is a digit')
#     except ValueError:   
#         print(f'{c} is not a digit')

# char = input('Input character: ')
# if (char>='0' and char <= '9'):
#     print(f'{char} is a digit')
# else:
#     print(f'{char} is not a digit')

#4
# n = int(input('Input number: '))
# if n%3 == 0:
#     if n%5 == 0:
#         print(f"{n} is divisible by 3 and 5")
#     else:
#         print(f"{n} is divisible by 3")
# else:
#     if n%5 == 0:
#         print(f"{n} is divisible by 5")
#     else:
#         print(f"{n} is not divisible by 3 or 5")

#5
# print('Welcome to The Ultimate Sercurity System')
# u = input('Username: ')
# p = input('Password: ')
# if u == 'admin':
#     if p == '12345':
#         print("You are logged in, admin.")
#     else:
#         print("Wrong username or password.")
# else:
#     print("Wrong username or password.")

#6
# a = float(input('canh 1: '))
# b = float(input('canh 2: '))
# c = float(input('canh 3: '))
# if (a <= 0) or (b <= 0) or (c <= 0):
#     print('nhap so duong pls')
# else:
#     if (a+b <= c) or (c+b <= a) or (c+a <= b):
#         print('The 3 line segments cannot form a triangle.')
#     else:
#         print('The 3 line segments can form a triangle.2')

#7
# a = float(input('canh 1: '))
# b = float(input('canh 2: '))
# c = float(input('canh 3: '))
# if (a <= 0) or (b <= 0) or (c <= 0):
#     print('nhap so duong pls')
# else:
#     if (a+b <= c) or (c+b <= a) or (c+a <= b):
#         print('The 3 line segments cannot form a triangle.')
#     else:
#         if (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (c**2 + a**2 == b**2):
#             print('The 3 line segments can form a right triangle.')
#         elif a==b==c:
#             print('The 3 line segments can form an equilateral triangle.')
#             from turtle import *
#             shape('turtle')
#             forward(a)
#             left(120)
#             forward(a)
#             left(120)
#             forward(a)
#             mainloop()
#         else:
#             print('The 3 line segments can form a triangle.2')