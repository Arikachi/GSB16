# import module1
#1
# n = input("Input a Roman number:")
# a = 0
# for i in module1.numbers.keys():
#     if i == n:
#         print("Arabic number:", module1.numbers[i])
#         a+=1
# if a == 0:
#     print("Not found.")

#2
# for i,j in module1.numbers_2.items():
#     module1.numbers[i] = j
# n = input("Input a Roman number:")
# a = 0
# for i in module1.numbers.keys():
#     if i == n:
#         print("Arabic number:", module1.numbers[i])
#         a+=1
# if a == 0:
#     print("Not found.")

#3
# number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
# 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
# list = {}
# for i in range(len(number_list)):
#     list[number_list[i]] = i+1
# n = input("Input a Roman number:")
# a = 0
# for i in list.keys():
#     if i == n:
#         print("Arabic number:", list[i])
#         a+=1
# if a == 0:
#     print("Not found.")

#4
# students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
# {'firstName': 'Mervin', 'lastName': 'Friedland'},
# {'firstName': 'Aron', 'lastName': 'Wilkins'}]

# for i in students:
#     print("-", end ='')
#     for n in i.keys():
#         print(i[n], end = ' ')
#     print('\n')

#5
# names = {
# 'students': [
# {'firstName': 'Nikki', 'lastName': 'Roysden'},
# {'firstName': 'Mervin', 'lastName': 'Friedland'},
# {'firstName': 'Aron', 'lastName': 'Wilkins'}
# ],
# 'teachers': [
# {'firstName': 'Amberly', 'lastName': 'Calico'},
# {'firstName': 'Regine', 'lastName': 'Agtarap'}
# ]
# }

# for t in names.keys():
#     if t == "students":
#         for i in names[t]:
#             print("Students: ")
#             print("-", end ='')
#             for n in i.keys():
#                 print(i[n], end = ' ')
#             print('\n')
#     else:
#         for i in names[t]:
#             print("Teachers: ")
#             print("-", end ='')
#             for n in i.keys():
#                 print(i[n], end = ' ')
#             print('\n')

#6
# n = input("Input sequence: ")
# fr = {}
# for i in n:
#     fr[i] = 0
# for i in n:
#     for j in fr.keys():
#         if i == j:
#             fr[i] += 1
# print(fr)