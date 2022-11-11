# n = input()
# L = n.split(" ")
# import string
# alphabet = list(string.ascii_lowercase)
# values = {}
# for index, letter in enumerate(string.ascii_lowercase):
#    values[letter] = index + 1
# K =[]
# for i in L:
#     t = 0
#     for j in i:
#        t += values[j]
#     K.append(t)

# for i in K:
#     max = K[0]
#     for i in range(len(K)):
#         if K[i]>max:
#             max = K[i]
# o = K.index(max)
# print(L[o])

n = input()
