print("введите число")
def prost(n):
    d=2
    while n%d!=0:
        d+=1
    return d==n
def primfacs(n):
    i=2
    primfac=[]
    while i*i<=n:
        while n%i==0:
            primfac.append(i)
            n=n/i
        i=i+1
    if n>1:
        primfac.append(n)
    return primfac
n=int(input())
if prost(n)==True:
    print("число простое")
else:
    print("число составное", primfacs(n))
            
            
            
                
