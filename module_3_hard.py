data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
#for i in range(len(data_structure)):
#    print(data_structure[i], type(data_structure[i]))


def calculate_structure_sum(*args):
    summ = 0
    for j in args:
        if isinstance(j, (list, tuple, set)):
            summ += calculate_structure_sum(*j)
        elif isinstance(j, dict):
            summ += calculate_structure_sum(*j.keys())
            summ += calculate_structure_sum(*j.values())
        elif isinstance(j, int):
            summ += j
        elif isinstance(j, str):
            summ += len(j)
    return summ


result = calculate_structure_sum(data_structure)
print(result)
