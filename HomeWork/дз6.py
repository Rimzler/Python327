import random

size = int(input("Введите размер списка: "))

nums = []

while len(nums) < size:
    num = random.randint(1, 100)
    if num not in nums:
        nums.append(num)

print(nums)
