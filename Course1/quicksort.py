a=[]
with open("Quicksort.txt") as numbers:
    for number in numbers:
        a.append(int(number))
print(len(a))
comparisions=0
def partition(a,l,h):
    global comparisions
    if l<h:
        pivot=a[h-1]
        i=l
        j=h
        while 1:
            while((a[i]<pivot)):
                i+=1
                comparisions+=1
            while((a[j]>pivot)):
                j-=1
                comparisions+=1
            if i>=j:
                return j
            a[i],a[j]=a[j],a[i]

def quicksort(a,l,h):
    if l<h:
        i=partition(a,l,h)
        quicksort(a,l,i)
        quicksort(a,i+1,h)
 
n=len(a)
quicksort(a,0,n-1)
print(comparisions)