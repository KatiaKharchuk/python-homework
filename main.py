import random
a = [random.randint(-10,10) for i in range(10)]
print (a)
b = [random.randint(-10,10) for i in range(10)]
print (b)
c = list()
for i in range(1, 10):
    for j in range(1, 10):
        if a[i] == b[j]:
            c.append(a[i])

print(c)





