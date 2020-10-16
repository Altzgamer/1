#n = int(input("Сколько будет чисел? "))
a=[4, 3, 2, 1]
for i in range(0, n-1):
    b = a[i]
    for g in range(1, n):
        if b > a[g]:
            a[g], a[g-1] = a[g-1], a[g]
print(a)
