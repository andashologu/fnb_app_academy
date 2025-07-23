my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)

print(my_set) # {1, 2, 3, 4, 5, 6}

my_set.remove(3)

print(my_set) # {1, 2, 4, 5, 6}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set) # results: {1, 2, 3, 4, 5} # duplicate 3 removed


inter_set = set1.intersection(set2) 

print(inter_set) # results: 3

# difference

diff_set = set1.difference(set2)

print(diff_set) # {1, 2}