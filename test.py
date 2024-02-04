a = [1,2,3]
for i in range(len(a)):
    a[i] = str(a[i])
print(a)
b= '.'.join(a)
print(a, b)