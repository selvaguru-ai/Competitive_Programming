import timeit
from datetime import datetime
import time

def special_sum(a):
    output = []
    for i in range (0, len(a)):
        j = i + 1
        if (len(a)==1):
            return a
        elif (j < len(a)):
            output.append(a[i]+a[j])
    return special_sum(output)

start = time.time()
a = list(map(int, input().split()))
stop = time.time()
print (special_sum(a))
print (stop - start)
