# task 1
def grams_to_ounces(grams):
    return 28.3495231 * grams

# task 2
def faren_to_c(F):
    return (5 / 9) * (F – 32)

F = float(input())
print(faren_to_c(F))

# task 3
def solve(heads, legs):
    # rab + chi = heads
    # rab * 4 + chi * 2 = legs
    # rab * 4 + (heads - rab) * 2 = legs
    # rab * 2 = legs - 2 * heads
    # rab = (legs - 2 * heads) / 2
    rab = (legs - 2 * heads) // 2
    chi = heads - rab
    print(f'{rab} rabbits, {chi} chickens')

# task 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(primes):
    out = []
    for i in primes:
        if is_prime(i):
            out.append(i)
    return out

# task 5
# if we can use itertools:
from itertools import permutations

def permute(str):
    perms = permutations(str)
    for i in perms:
        print("".join(i))

# if we should write own:
from collections import deque #i used this to maintain order, can be built using default list too

def permute(str):
    deq = deque()
    for i in range(len(str)):
        deq.append((str[i], list(str[:i] + str[i + 1:])))
    while deq:
        cur, rem = deq.popleft()
        if len(cur) == len(str):
            print(cur)
        else:
            for i in range(len(rem)):
                deq.append((cur + rem[i], rem[:i] + rem[i + 1:]))

# task 6
def reverse(str):
    return str[::-1]

# task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False

# task 8
def spy_game(nums):
    stack = []
    for i in nums:
        if i == 0 or i == 7:
            stack.append(i)
    for i in range(len(stack) - 2):
        if stack[i:i + 3] == [0, 0, 7]:
            return True
    return False

# task 9
def volume(R):
    return (4 / 3) * 3.14 * (r ** 3)

# task 10
def unique(nums):
    were = {}
    for i in nums:
        if i not in were:
            were[i] = 0
        were[i] += 1
    out = []
    for i in were:
        if were[i] == 1:
            out.append(i)
    return out

# task 11
def is_palindrome(str):
    return str == str[::-1]

# task 12
def histogram(heights):
    for i in heights:
        print("*" * i)

# task 13
from random import randint

def game():
    num = randint(1, 20)
    user = input("Hello! What is your name?\n")
    print(f'Well, {user}, I am thinking of a number between 1 and 20.')
    guess = 0
    while:
        guess += 1
        unum = int(input("Take a guess.\n"))
        if num == unum:
            break
        elif num < unum:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
    print(f'Good job, {user}! You guessed my number in {guess} guesses!')

# task 14
# this file :^)
        
    

