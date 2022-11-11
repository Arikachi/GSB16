#1
# n1 = int(input("First number: "))
# n2 = int(input("Second number: "))
# print(f"{n1} + {n2} = ", n1+n2)

#2
# import math
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# d = b**2 - 4*a*c
# if d > 0:
#     x1 = (-b + math.sqrt(d))/(2*a)
#     x2 = (-b - math.sqrt(d))/(2*a)
#     print(x1, x2)
# elif d == 0:
#     x = (-b)/(2*a)
#     print(x)
# else:
#     print("no")

#3
# s = input("check: ")
# def is_palindrome(n):
#     A = []
#     t = ""
#     for i in n:
#         A.append(i)
#     for i in range(1, len(A)+1):
#         t += A[-i]
#     if t == n:
#         print("is palindrome")
# is_palindrome(s)

#4
# print("== Welcome to MindX Restaurant ==")
# t = 0
# A = []
# while t<1:
#     n = input("Please choose a dish: ")
#     if n in A:
#         n1 = input("You chose this already. Anythingelse? (y/n):")
#     else:
#         A.append(n)
#         n1 = input("Great choice! Anything else? (y/n):")
#     if n1 == "y":
#         t += 0
#     elif n1 == "n":
#         t += 1
#         print("Well done! Your order: ")
#         for i in A:
#             print(i)

#5
# phone = {
#     "Iphone12": 28000000,
#     "Samsung N10": 16000000,
#     "Oppo 93": 7500000,
#     "Vsmart": 7400000,
#     "Vivo": 4200000
# }
# n = input("Input name of a phone: ")
# print(phone[n])
# t = int(input("Input your budget: "))
# for i in phone:
#     if phone[i] < t:
#         print(i, phone[i])

#6
# n = int(input("Input a number > 0:"))
# t = 0
# for i in str(n):
#     t += 1
# print(t)

#7
# n = [5, 1, 8, 92, -1, 30]
# t = 1
# while t > 0:
#     t = 0
#     for i in range(1, len(n)):
#         if n[i-1] > n[i]:
#             n[i-1], n[i] = n[i], n[i-1]
#             t = 1
# print(n)

#8
# def fibo(n):
#     f0 = 1
#     f1 = 1
#     fn = 2
#     if (n < 0):
#         return False
#     elif (n == 0 or n == 1):
#         return 1
#     else:
#         for i in range(2, n):
#             f0 = f1
#             f1 = fn
#             fn = f0 + f1
#         return fn
# n = int(input("Input number > 0: "))
# sb = ""
# for i in range(n):
#     sb = sb + str(fibo(i)) + ", "
# print(sb)