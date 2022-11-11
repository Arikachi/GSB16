# def sum(a,b):
#     a = 5
#     b = 0
#     return a+b
# a = 0
# b = 0
# print(a)

list = [3, 1, 5, 10, 12, 10, 20]
def print_list(input_list):
    for i in range(len(input_list)):
        if i >= 1:
            if input_list[i]<input_list[i-1]:
                input_list[i-1], input_list[i] = input_list[i], input_list[i-1]
    print(input_list)
print_list(list)

