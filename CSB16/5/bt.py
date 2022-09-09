c = input('Input: ')
# try:
#     char = int(c)
#     print('la so')
# except ValueError:
#     print('ko la so')

# char = []
# for i in c:
#     char.append(i)
# a = 0
# for i in char:
#     if (i>='0' and i <= '9'):
#         a += 1
#     else:
#         a += 0
# if a == len(char):
#     print('la so')
# else:
#     print('ko la so')

str = input("Nhap ...: ")
list = ['0','1','2','3','4','5','6','7','8','9']
a = 0
for i in str:
    if i not in list:
        a += 1
if a == 0:
    print('la so')
else:
    print('ko la so')
