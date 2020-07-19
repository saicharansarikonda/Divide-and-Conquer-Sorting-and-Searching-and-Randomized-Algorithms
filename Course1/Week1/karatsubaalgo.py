def karatsuba(n1,n2):
    n1Str = str(n1)
    n2Str = str(n2)
    if (n1 < 10) or (n2 < 10):
        return n1*n2
    
    maxLen = max(len(n1Str), len(n2Str))
    splitPos = maxLen // 2
    high1, low1= int(n1Str[:-splitPos]), int(n1Str[-splitPos:])
    high2, low2= int(n2Str[:-splitPos]), int(n2Str[-splitPos:])
    c0 = karatsuba(low1, low2)
    c1 = karatsuba((low1 + high1), (low2 + high2))
    c2 = karatsuba(high1, high2)

    return (c2*10**(2*splitPos)) + ((c1-(c2+c0))*10**(splitPos))+c0

n1=int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))
ans=karatsuba(n1,n2)


ansf=8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
if(ans==ansf):
    print("Yes")
else:
    print("No")