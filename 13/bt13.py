# r - read
# a - append
# w - write
f = open("13/file1.txt", "r")
num = f.readline()

ds = []
for i in num.split(" "):
    ds.append(int(i))
print(ds)

max = ds[0]
for i in range(len(ds)):
    if ds[i]>max:
        max = ds[i]
print(max)