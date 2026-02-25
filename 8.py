def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    max_of_rest = find_max_recursive(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest


def integer_partitions(n, max_part=None, current=None):
    if max_part is None:
        max_part = n
    if current is None:
        current = []

    if n == 0:
        return [current[:]]

    results = []
    for i in range(1, min(max_part, n) + 1):
        current.append(i)
        results.extend(integer_partitions(n - i, i, current))
        current.pop()
    return results


n = 7
partitions = integer_partitions(n)
print(f"Все разбиения числа {n}:")
for p in partitions:
    print(p)