# mylist = [6,7,8]
# print(mylist[0])
# mylist2 = ['a','6','abc',6.3,True]
# print(type(mylist2[4]))
# list = mylist + mylist2
# list.append('x')
# list.remove('6')
# list.remove(6)
# list.pop()
# print(list)

# mylist3 = [6,7,8,6,'orange']
# mylist3.remove(6)
# mylist3.pop(2)
# print(mylist3)

# for i in mylist3:
#     print(i)
# for i in range(len(mylist3)):
#     print(mylist3[i])

# i = 0
# while i < len(mylist3):
#     print(mylist3[i])
#     i += 1

# mylist3[0] = 10
# print(mylist3)

# lisEx = list(('1',2))
# mylist3.extend(lisEx)
# print(mylist3)

# listCopy = mylist3
# print(listCopy)

#Tuple
# myTuple = (1,2,3,4)
# myTuple2 = tuple(("abcv","def"))
# myTuple = (15,)
# print(myTuple)
# print(myTuple[0])

# L = [1,2,3,4]
# i = 0
# while i < len(L):
#     print(L[i])
#     i += 1

# L = [1,'2ra',3, 10, 'fs']
# s = 0
# for i in L:
#     if type(i) == int:
#         s += i
# print(s)

# mylist = [5,2,7,3,-3]

# for i in range(len(mylist)):
#     for j in range(len(mylist)):
#         if mylist[i] < mylist[j]:
#             if i > j:
#                 mylist[i], mylist[j] = mylist[j], mylist[i]
# print(mylist)

# list = ['adf','jtr','olj']
# for i in list:
#     print('\n')
#     print(i,":", end = '')
#     for j in i:
#         print(j, end = ',')