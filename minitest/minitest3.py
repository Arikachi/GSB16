#1
# def even(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False
# n = int(input())
# if even(n):
#     print("chan")
# else:
#     print("le")

#2
# def cal_area(r):
#     return r**2*3.14
# r = int(input())
# print(cal_area(r))

#3
# def reverse_str(n):
#     A = []
#     t = ""
#     for i in n:
#         A.append(i)
#     for i in range(1, len(A)+1):
#         t += A[-i]
#     return t
# n = input()
# print(reverse_str(n))

#4
# def is_palindrome(n):
#     if n == reverse_str(n):
#         print("This is a palindrome.")
# n = input()
# is_palindrome(n)

#1
# def gith(n):
#     t = 1
#     for i in range(1, n+1):
#         t = t*i
#     return t
# n = int(input())
# print(gith(n))

#2
# def sort(n):
#     t = 1
#     while t > 0:
#         t = 0
#         for i in range(1, len(n)):
#             if n[i-1] > n[i]:
#                 n[i-1], n[i] = n[i], n[i-1]
#                 t = 1
#     return n

# n = [5,1,8,92,-1,30]
# print(sort(n))

#3
# def print_fibo(n):
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

# n = int(input("Nhap so > 0: "))
# sb = ""
# for i in range(n):
#     sb = sb + str(print_fibo(i)) + ", "
# print(sb)