#1
# color = ['red', 'blue', 'green']
# print("Color list: ", color[0], ",", color[1], ",", color[2])
# n = input("Input a new color: ")
# color.append(n)
# print("New color list: ", color[0], ",", color[1], ",", color[2], ",", color[3])

#2
# p = int(input('Input position: '))
# print("New color list: ", color[p-1])
# d = input("Item to delete: ")
# try:
#     check = int(d)
#     color.remove(color[int(d)]) 
# except ValueError:
#     color.remove(d)
# print("New color list: ", color[0], ",", color[1])

# L = ()
# for i in color:
#     c = (i,)
#     L += c
# from turtle import *
# shape('turtle')
# for i in L:
#     pencolor(i)
#     forward(100)
#     pencolor("white")
#     forward(100)
# mainloop()

#3
# num = [5, 1, 8, 92, -1, 30]
# n = int(input("Input a number: "))
# if n in num:
#     print(num.index(n)+1)
# else:
#     print("Number not found")

# a = 0
# for i in num:
#     a += i
# print(a)

# nu = []
# t = 0
# while t < 1:
#     n = int(input("Input the list of numbers: "))
#     if n != 0:
#         nu.append(n)
#     else:
#         a = 0
#         for i in nu:
#             a += i
#         print(a)
#         t = 1

#4
# num = [5, 1, 8, 92, -1, 30]
# e = []
# for i in num:
#     if i%2 == 0:
#         e.append(i)
# print("Even numbers: ", e)

# nu = []
# t = 0
# while t < 1:
#     n = int(input("Input the list of numbers: "))
#     if n != 0:
#         nu.append(n)
#     else:
#         e = []
#         for i in nu:
#             if i%2 == 0:
#                 e.append(i)
#         print("Even numbers: ", e)
#         t = 12

#5
# quan = ["BD", "BTL", "CG", "DD", "HBT"]
# ds = [247100, 333300, 266800, 420900, 318000]
# max = ds[0]
# for i in range(len(ds)):
#     if ds[i]>max:
#         max = ds[i]
# print(ds.index(max))
# min = ds[0]
# for i in range(len(ds)):
#     if ds[i]<min:
#         min = ds[i]
# print(ds.index(min))

# print(quan[ds.index(max)])
# print(quan[ds.index(min)])

#6
# s = [9.224, 43.35, 12.04, 9.96, 10.09]
# sum = 0
# for i in range(len(s)):
#     m = ds[i]/s[i]
#     print(quan[i],": ", m)
#     sum += m
# avr = sum/len(quan)
# print("Average population density: ", avr)

#7 #8
# hs = [78, 56, 67, 67, 45]
# for i in range(len(hs)):
#     print(i+1,". ", hs[i])
# n = int(input("Input new highscore: "))
# hs.append(n)
# hs.sort(reverse=True)
# for i in range(len(hs)):
#     print(i+1,". ", hs[i])
#     if i == 4:
#         break