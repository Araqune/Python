#2
my_dict = {'Антон': 1996,
           'Василий': 2001,
           'Григорий': 1997}
print(my_dict)
print(my_dict.get('Антон')) # значение по существующему ключу
print(my_dict.get('Сергей')) # значение по отсутствующему ключу
my_dict.update({'Алиса': 1995,
               'Роман': 1998})
a = my_dict.pop('Василий')
print(a)
print(my_dict)

#3
print()
my_set = {1, 'str', 2, 3, 2, 3, True, True, 'str', ''}
print(my_set)
my_set.update({4, 5})
my_set.discard('')
print(my_set)