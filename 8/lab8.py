#1
# def is_int(num):
#     if num == int(num):
#         return True
#     else:
#         return False
# num = float(input())
# if is_int(num):
#     print(f'{int(num)} is an integer')
# else:
#     print(f'{num} is not an integer')

#2
# def is_prime(n):
#     p = 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             p+=1
#     if p == 2:
#         return True
#     else:
#         return False

# num = int(input())
# if is_prime(num):
#     print(f'{int(num)} is prime')
# else:
#     print(f'{num} is not prime')

#3
# n = int(input())
# i = 0
# j = 0
# while j < n:
#     if is_prime(i) == True:
#         print(i)
#         i += 1
#         j += 1
#     else:
#         i += 1
    
#4
# def pow(n):
#     p = 1
#     for i in range(1, n+1):
#         p = p*i
#     return p
# def ans(n):
#     t = 0
#     for i in range(1, n+1):
#         t += pow(i)/i
#     return t
# n = int(input())
# print(ans(n))

#5
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(now.strftime('%d/%m/%Y'))
# print(now.strftime('%H:%M:%S'))