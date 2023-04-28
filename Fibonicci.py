# 0 1 1 2 3 5 8 13 21 34 55
# for i in range(1,11):
#     print(i,end =" ")
#     print(i,end =",")
def fibonicci(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b,end=" ")
fibonicci(20)
