from math import factorial

n = int(input())
triangle = []
for i in range(n):
    triangle.append([])
    for j in range(i + 1):
        triangle[i].append(factorial(i) // (factorial(j) * factorial(i - j)))


def print_pascal_tree(ps):
    """
    Выведение в виде дерева
    :param ps: список для треугольника
    """
    sep = ' ' * len(str(max(ps[-1])))
    max_len = len(sep.join(map(str, ps[-1])))
    for p in ps:
        print(sep.join(map(str, p)).center(max_len))


print_pascal_tree(triangle)
