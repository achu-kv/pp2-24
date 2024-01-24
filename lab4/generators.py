# task 1

def Ngen(n):
    for i in range(n + 1):
        yield i ** 2

# task 2
def Egen(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(*list(Egen(n)), sep=", ")
    
# task 3
def tfgen(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i

# task 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

for i in squares(5, 15):
    print(i)

# task 5
def tozerogen(n):
    for i in range(n, -1, -1):
        yield i


