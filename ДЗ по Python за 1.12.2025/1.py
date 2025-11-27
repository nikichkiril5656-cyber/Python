#Рекурсивное разбиение Создайте функцию,
#которая рекурсивно разбивает целое число на
#все возможные комбинации меньших чисел,
#сумма которых равна исходному числу.
#Например, для числа 4 результатом могут быть
#[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3] и т.д.

def partition_recursive(n, min_part=1):

    if n == 0:
        return [[]]

    partitions = []
    for i in range(min_part, n + 1):
        for j in partition_recursive(n - i, i):
            partitions.append([i] + j)

    return partitions

number = 10
result = partition_recursive(number)
print(f"Разбиения числа {number}:")
for j in result:
    print(*j)