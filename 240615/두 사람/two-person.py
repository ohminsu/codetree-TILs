a1, a2 = map(str, input().split())
b1, b2 = map(str, input().split())

a1, b1 = int(a1), int(b1)
a2, b2 = str(a2), str(b2)

if (a1>=19 and a2=='M') or (b1>=19 and b2=='M') :
    print(1)

else :
    print(0)