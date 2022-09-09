#1
# n = int(input('Num of stairs: '))
# for i in range(n):
#     print('#'*(i+1), end='\n')

#2
# i = 0
# while i<1:
#     n = float(input('Input a positive number: '))
#     if int(n) == n:
#         if (n>0):
#             print('thank you')
#             break

#3
# n = int(input("Input number: "))
# if n > 0:
#     t = 1
#     for i in range(n):
#         t = t*(i+1)
#     print(t)
# elif n == 0:
#     print(1)
# else:
#     print("Invalid")

#4
# i = 0
# while i<1:
#     n = int(input('Input a positive number: '))
#     if (n>0):
#         di = 0
#         for t in str(n):
#             di = di+int(t)
#         print(di)
#         break

#5
# m = 0
# for t in range(1000, 9999):
#     i = 0
#     while i<1:
#         di = 0
#         for n in str(t):
#             di = di+int(n)
#         if di == 9:
#             print(t)
#             m += 1
#         break
#     if m == 10:
#         break

#6
# n = int(input('pls positive interger greater than 2:'))
# if n>2:
#     from turtle import *
#     shape('turtle')
#     for i in range(n):
#         forward(90)
#         right(180-(180*(n-2)/n))
#     mainloop()

#7
# from turtle import *
# shape('turtle')
# r = 10
# while r < 250:
#     circle(r, 180)
#     r += 10
# mainloop()