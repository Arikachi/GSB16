#1
# f = input('First name: ')
# l = input('First name: ')
# print(f'Your full name is {f} {l}')

#2
# n = input('Your input: ')
# c = n.upper()
# print(f'Capitallized: {c}')

#3
# s = int(input('Input a number: '))
# print(s**2)

#4
# from turtle import *
# r = int(input('Radius: '))
# shape('turtle')
# circle(r)
# mainloop()

#5
# for i in range(3, 13):
#     print(i)

#6
# n = int(input('Input a number: '))
# for i in range(-1, n):
#     print(i+1)

#7
# n = int(input('pls positive interger greater than 2:'))
# if n>2:
#     from turtle import *
#     shape('turtle')
#     for i in range(n):
#         forward(90)
#         right(180-(180*(n-2)/n))
#     mainloop()

#8
# n = int(input('Input a number: '))
# if n >13 :
#     print('larger than 13')
# else:
#     print('not larger than 13')

#9
# n = int(input('Input a number: '))
# if n%2 == 0 :
#     print('even')
# else:
#     print('odd')

#10
# n = int(input('Input a month: '))
# if n == 2:
#     print('28')
# else:
#     if n<8:
#         if n%2 == 0 :
#             print('31')
#         else:
#             print('30')
#     else:
#         if n%2 == 0 :
#             print('31')
#         else:
#             print('30')

#11
# print("== Registration ==")
# a = input("Username: ")
# b = input("Password: ")
# c = input("Email: ")
# print(f'''Username: {a}
# Password: {b}
# Email: {c}
# Registered successfully.
# ''')

#12
# i = 0
# while i<1:
#     print("== Registration ==")
#     a = input("Username: ")
#     b = input("Password: ")
#     d = input("Repassword: ")
#     c = input("Email: ")
#     if b == d:
#         print(f'''Username: {a}
#         Password: {b}
#         Email: {c}
#         Registered successfully.
#         ''')
#         break
#     else:
#         print('repeat password correctly.')

#13.
# t = 0
# r = 0
# m = 0
# print("== Registration ==")
# a = input("Username: ")
# b = input("Password: ")
# c = input("Email: ")
# for i in c:
#     if i == '@':
#         t += 1
# print(t)
# if t > 0:
#     for j in c:
#         if j == '.':
#             r += 1
# print(r)
# if r > 0:
#     for l in range(len(c)):
#         m += 1
# print(m)
# if m >= 8:
#     print(f'''Username: {a}
#     Password: {b}
#     Email: {c}
#     Registered successfully.
#     ''')
# else:
#     print('repeat email correctly.')

# extra 1
# from math import *
# i = 0
# while i < 1:
#     a = int(input('a: '))
#     b = int(input('b: '))
#     c = int(input('c: '))
#     if a == 0 or b == 0:
#         print('try again')
#     else:
#         if b**2 - 4*a*c > 0:
#             d = b**2 - 4*a*c
#             d1 = (-b + sqrt(d))/(2*a)
#             d2 = (-b - sqrt(d))/(2*a)
#             print(d1, d2)
#             break
#         elif b**2 - 4*a*c == 0:
#             d = b**2 - 4*a*c
#             print(-b/(2*a))
#             break
#         else:
#             print('no value')
#             break

# extra 2
# n = input('Nhap day so: ')
# t = 0
# for i in n:
#     if int(i)%2 == 0:
#         t += int(i)
# print(t)

# extra 3
# from turtle import *
# shape('turtle')
# fillcolor('red')
# begin_fill()
# pencolor('red')
# forward(300)
# right(90)
# forward(210)
# right(90)
# forward(300)
# right(90)
# forward(210)
# right(90)
# end_fill()
# penup()
# color('yellow')
# setposition(100, -90)
# pendown()
# fillcolor('yellow')
# begin_fill()
# for i in range(5):
#     forward(120)
#     right(144)
# end_fill()
# penup()
# setposition(-100, -100)
# mainloop()