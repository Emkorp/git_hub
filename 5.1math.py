import numpy as np
import random
np.random.randint(0, 37)
for i in range(0, 37):
    a = input()
    x = np.random.randint(0, 37)
    if x in [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36]:
        print('red')
    if x in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
        print("black")
    else:
        print('zero')
