#2
immutable_var = ('name', False, 5, 4.1, [2, 3.1, True, 'str'])
print(immutable_var)

#3
#immutable_var[1] = 'surname'
#print(immutable_var)
# в кортеже нельзя изменять типы данных строка и число, потому что котреж не поддерживает изменения объектов с этими типами

#4
mutable_var = ([2, 3.1, True, 'str'], [3, 5.7, False, 'int'])
mutable_var[0][1] = 2.99
print(mutable_var)
