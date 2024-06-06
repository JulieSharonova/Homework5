immutable_var = (1, 2.3, 'cucumber', False)
print(immutable_var)
print(immutable_var * 2)
immutable_var = (1, 2.3, 'cucumber', False) + (8, 7)
print(immutable_var)
# кортеж неизменяемый список, поэтому при попытке изменить элемент внутри него, то выдает ошибку. Если сделать список
# внутри кортежа, то тогда элемент можно поменять только внутри этого списка в кортеже. единственное, что доступно
# это умножение и прибавление элементов в кортеже


mutable_list = [1, 2.3, 'cucumber', False]
print(mutable_list + [7, 0])
mutable_list[0] = 'four'
print(mutable_list)
mutable_list[1] = 'seven'
print(mutable_list)
mutable_list.append('camel')
print(mutable_list)
mutable_list.remove('cucumber')
print(mutable_list)
mutable_list.extend(['sea', 9, 10, False])
print(mutable_list)

