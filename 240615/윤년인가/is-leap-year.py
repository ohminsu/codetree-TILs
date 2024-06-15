y = int(input())

if y % 4 == 0 :
    
    if 100 % y == 0 and 400 % y == 0 :

        print("false")

    else :

        print("true")

else :
    print("false")