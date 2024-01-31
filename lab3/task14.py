import functions1 as f1

nums = range(100)
print(f'Filtered primes 0-99: {f1.filter_prime(nums)}\n')

to_reverse = "The quick brown fox jumps over a lazy dog"
print(f'"{to_reverse}" reversed:\n{f1.reverse(to_reverse)}\n')

some_nums = [1, 2, 0, 3, 4, 0, 1, 2, 3, 3, 7]
print(f'{some_nums} has 2 "3" somewhere: {f1.has_33(some_nums)}')
print(f'{some_nums} has "007" in order: {f1.spy_game(some_nums)}\n')

heights = [1, 3, 2, 5, 10, 9]
print(f'Histogram for {heights}:')
f1.histogram(heights)