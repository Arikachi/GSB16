year = int(input("nhap nam:"))

if (year%400 == 0) or ((year%4==0) and (year%100 != 0)):
    print('la nam nhuan')
else:
    print('ko la nam nhuan')

if (year%4 == 0):
    if(year%100==0) and (year%400!=0):
        print('ko la nam nhuan')
    else:
        print('la nam nhuan')
else:
    print('la nam nhuan')