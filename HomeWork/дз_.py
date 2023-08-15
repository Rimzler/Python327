# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# res = sorted(students, key=lambda item: item['name'])
# print(res)
#
# res2 = sorted(students, key=lambda item: item['final'], reverse=True)
# print(res2)

nums = [3, 5, 7, 3, 9, 5, 7, 2]
res1 = list(map(lambda x: x ** 2, nums))
res2 = list(map(lambda x: x ** 3, nums))
print(res1)
print(res2)