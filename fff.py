n = int(input("Сколько будет чисел? "))
a=[]
for j in range(n):
    c=int(input())
    a.append(c)
for i in range(n-1):
    for g in range(0, n-1-i):
       if a[g]>a[g+1]:
           a[g], a[g+1]=a[g+1], a[g]
           print(a)
           print(i)

print(a)
