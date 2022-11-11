f = open("13/lab/names.txt", "r")
print("List of names:")

with open("13/lab/names.txt", "r") as fi:
    for i in fi.readlines():
        print("-", i, end = "")