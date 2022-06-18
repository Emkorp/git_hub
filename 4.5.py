d = [i for i in range(100, 1001) if i % 2 == 0]

import functools
import operator
print(functools.reduce(operator.mul, d))
