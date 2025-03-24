import random
import time

def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)

n = 1000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**7) for _ in range(n)]

start_time = time.time()
result = count_even(numbers)
end_time = time.time()

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")
