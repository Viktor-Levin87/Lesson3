def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, True, 'Hi']
values_dict = {'a': False, 'b': 20, 'c': 'Привет'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [10, True]
print_params(*values_list_2, 42)
