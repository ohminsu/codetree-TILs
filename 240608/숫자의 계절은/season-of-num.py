a = int(input())

spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
winter = [12, 1, 2]

if a in spring :
    print("Spring")
elif a in summer :
    print("Summer")
elif a in fall :
    print("Fall")
elif a in winter :
    print("Winter")
else :
    print('없는 월 입니다.')