mojodi=int(input("mojodi ro bogo:"))
print("chi mikhay?1-mojodi 2-variz 3-bardasht 4-hale")
n=int(input("kodom?"))
while 1 :
    print("chi mikhay?1-mojodi 2-variz 3-bardasht 4-hale")
    n=int(input("kodom?"))
    if n==1:
        print(mojodi)
    elif n==2:
        print("che gadr mirizi?")
        w=int(input())
        mojodi+=w
        print("ok")
    elif n==3:
        print("che gadr varmidari?")
        b=int(input())
        if mojodi>=b:
            mojodi-=b
            print("ok")
        else:
            print("nemishe")
            break
    elif n==4 :
        break

print(mojodi)


