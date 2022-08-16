import numpy as np
import itertools
k, n = 0, 4
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(a, b, c, d)
print(x)
print(k, n, k/n)
factorialn = 1
while n >1:
    factorialn *= n
    n -=1
print(factorialn)
factorialk = 1
while k >1:
    factorialk *= k
    k -= 1
print(factorialk)
f = n - k
print(f)
factorialf = 1
while f >1:
    factorialf *= k
    k -= 1
print(factorialf)
c = factorialn / (factorialk * factorialf)
print(c)
p = c / 16
print(p)



import numpy as np
import itertools
k, n = 0, 10
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(a, b, c, d)
print(x)
print(k, n, k/n)
factorialn = 1
while n >1:
    factorialn *= n
    n -=1
print(factorialn)
factorialk = 1
while k >1:
    factorialk *= k
    k -= 1
print(factorialk)
f = n - k
print(f)
factorialf = 1
while f >1:
    factorialf *= k
    k -= 1
print(factorialf)
c = factorialn / (factorialk * factorialf)
print(c)
p = c / 1024
print(p)