# from math import *
# 1
# r = float(input("Radius: "))
# P = r*2*3.14
# S = r**2*3.14
# print('Perimeter:', P)
# print('Area:', S)

# 2
# d = float(input("length: "))
# d2 = sqrt(2*d**2)
# print(d2)

#3
# name = input('Account name:')
# domain = input("Domain name:")
# print(f'Full email: {name}@{domain}')

#4
# from posixpath import split
# date = input('Date in MM/DD/YYYY:')
# print(date[3:6],date[0:3],date[6:10])
# print(f"{date[3:5]}/{date[0:2]}/{date[6:]}")
# x = date.split('/')
# print(f'{x[1]}/{x[0]}/{x[2]}')

#5
# A = float(input('Deposit: '))
# first = A * 105/100
# second = A * (105/100)**2
# tenth = A * (105/100)**10
# print(f'''
# Account after 1 year: {first}
# Account after 2 years: {second}
# Account after 10 years: {tenth}''')

#6
from turtle import *
pensize(2)
shape('turtle')
penup()
setposition(-90, 90)
pendown()
forward(150)
right(90)
pensize(5)
pencolor('#de5246')
forward(90)
right(90)
pensize(2)
color('black')
forward(150)
right(90)
pensize(5)
pencolor('#de5246')
forward(90)
right(135)
forward(sqrt(75**2 + 75**2))
left(90)
forward(sqrt(75**2 + 75**2))
penup()
setposition(-15, 120)
left(45)

mainloop().

#7
# from turtle import *
# pensize(10)
# pencolor('#cf8f03')
# shape('turtle')
# penup()
# setposition(-90, 0)
# pendown()
# left(30)
# forward(90)
# right(60)
# forward(90)
# right(120)
# forward(90)
# right(60)
# forward(90)
# penup()
# setposition(-60, 0)
# right(150)
# pencolor('#0b2c3c')
# pendown()
# left(30)
# forward(90)
# right(60)
# forward(90)
# right(120)
# forward(90)
# right(60)
# forward(90)
# penup()
# setposition(-600, 0)
# mainloop()