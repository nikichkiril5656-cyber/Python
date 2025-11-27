#Нахождение наибольшего элемента в списке
#Реализуйте функцию, которая рекурсивно
#находит наибольший элемент в списке.

def find_max_number(list):
    if not list:
        return None
    if len(list)==1:
        return list[0]
    max_of_rest = find_max_number(list[1:])
    if list[0] > max_of_rest:
        return list[0]
    else:
        return max_of_rest
numbers=[5,0,23,1,89,5]
result=find_max_number(numbers)
print(result)