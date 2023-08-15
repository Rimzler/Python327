# def outer(a, b, c):
#     def inner(x, y):
#         return x * y
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# def calculate_area(a, b, c):
#     total_area = 0
#
#     def calculate_rectangle_area(length, width):
#         return length * width
#
#     def calculate_parallelepiped_area():
#         rectangle_area = 2 * (
#                 calculate_rectangle_area(a, b) + calculate_rectangle_area(b, c) + calculate_rectangle_area(a, c))
#         nonlocal total_area
#         total_area += rectangle_area
#         return rectangle_area
#
#     area = calculate_parallelepiped_area()
#     return area
#
#
# solutions = [(2, 4, 6), (5, 8, 2), (1, 6, 8)]
# for solution in solutions:
#     a, b, c = solution
#     area = calculate_area(a, b, c)
#     print(f"The area of the rectangular parallelepiped with sides a={a}, b={b}, c={c} is {area}")
#
# print(f"The total area is {total_area}")
