# num = 20
# num += input()
#note type input a = int(a)

# a = ""
# print(bool(a))

# a = 33
# b = 33
# if b>a:
#     print('b is greater than a')
# elif b==a:
#     print('b is equal to a')
# else:
#     print('b is smaller than a')

# a = ""
# if bool(a) == True:
#     print(a)
# else:
#     print("bool(a) == False")

# shorthand
# a = 11
# b = 10
# print(" a > b ") if a>b else print('a<=b')

# print('nhập 3 số')
# a = int(input('so thu nhat'))
# b = int(input('so thu hai'))
# c = int(input('so thu ba'))
# if a>b:
#     if b>c:
#         print(a)
#     else:
#         if a>c:
#             print(a)
#         else:
#             print(c)
# else:
#     if a>c:
#         print(b)
#     else:
#         if b>c:
#             print(b)
#         else:
#             print(c)

# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# elif c>a and c>b:
#     print(c)
# else:
#     print('ko co so lon nhat')

y = int(input("chọn năm"))
if y%4 == 0:
    if y%100 == 0:
        if y%400 == 0:
            print('la nam nhuan')
        else:
            print('ko la nam nhuan do ko chia het 400')
    else: 
        print('la nam nhuan')
else:
    print('ko la nam nhuan')

# if (y%400 == 0) or ((y%4==0) and (y%100 != 0)):
#     print('la nam nhuan')
# else:
#     print('ko la nam nhuan')