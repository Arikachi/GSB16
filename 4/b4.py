#for loop
# for i in range(6):
#     print(i)

# a = "abcdefaaa"
# for i in a:
#     print(i, end='\n')
# for i in range(len(a)):  # range(len(a)) = 0 -> 8
#     print(i)

# while loop
# i = 0
# while i<6:
#     i += 1
#     if(i==3):
#         continue ko chay lenh phia duoi
#     print(i)

# while i<6:
#     i += 1
#     if(i==3):
#         break dung vong lap while
#     print(i)

# b1: 
# a = [0, 1, 2, 3, 4, 5, 6]
# for i in a:
#     print(i)

# b2:
# for i in range(20):
#     if(i%3 == 0):
#         print(i)

# b3:
a = "classCSB7"
# for i in reversed(a):
#     print(i, end = "")
i = len(a) - 1
while i > 0:
    print(a[i], end = '')
    i -= 1
# for i in range(1, len(a)+1):
#     print(a[-i], end ='')