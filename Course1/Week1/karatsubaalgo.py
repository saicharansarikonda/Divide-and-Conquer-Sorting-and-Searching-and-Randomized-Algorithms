def karatsuba(n1,n2):
    if (n1 < 10) or (n2 < 10):
        return n1*n2
    
    n1Str = str(n1)
    n2Str = str(n2)    
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
print(karatsuba(n1,n2))