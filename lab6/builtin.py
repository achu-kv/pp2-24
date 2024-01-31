import functools
import time, math

# task 1
def mult(nums):
    return functools.reduce(lambda x, y: x * y, nums)

# task 2
def up_low(line):
    up = 0
    low = 0
    for i in line:
        if i.isalpha():
            if i.isupper():
                up += 1
            else:
                low += 1
    return up, low

# task 3
def is_polyndrome(line):
    i = list(line)
    i.reverse()
    return list(line) == i

# task 4
def sq_after_time(num, ms):
    time.sleep(ms * 0.001)
    print(f'Square root of {num} after {ms} miliseconds is {math.sqrt(num)}')

# task 5
def all_true(tup):
    return all(tup)