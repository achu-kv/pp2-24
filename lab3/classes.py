# task 1
class CustomString:
    def __init__(self):
        self.str = ""
    
    def getString(self):
        str = input()
        self.str = str
    
    def printString(self):
        print(self.str.upper())

# task 2
class Shape:
    def __init__(self):
        self.figure_area = 0
    
    def area(self):
        print(self.figure_area)


class Square(Shape):
    def __init__(self, length):
        self.length = length
        self.figure_area = 4 * length 

# task 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.figure_area = 0
    
    def compute_area(self):
        self.figure_area = self.length * self.width

# task 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

# task 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, money):
        if money < 0:
            money = 0
        self.balance += money

    def withdraw(self, money):
        if money < 0 or money > self.balance:
            money = 0
        self.balance -= money

    def __repr__(self):
        return f'Account({self.owner}, {self.balance})'

# task 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = range(100)
nums = filter(lambda x: is_prime(x), nums) # even though we can just filter(is_prime, nums)


