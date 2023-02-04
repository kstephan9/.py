import itertools

my_list = [1, 2, 3]

combinations = itertools.combinations(my_list, 2)
for c in combinations:
    print("2", c)

combinations = itertools.combinations(my_list, 3)
for c in combinations:
    print("3", c)

print("=================\n")
permutations = itertools.permutations(my_list, 2)
for c in permutations:
    print("2",c)

permutations = itertools.permutations(my_list, 3)
for c in permutations:
    print("3",c)
