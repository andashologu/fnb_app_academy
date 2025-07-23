# tuples are ordered and unchangable but also allow duplicates

my_tuples = (1, 2, 3, 4, 5)

print(my_tuples) # result: (1, 2, 3, 4, 5)

print(my_tuples[0]) # result: 1

print(my_tuples[2]) # result: 3

print(my_tuples[-1]) # result: 3

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2

print(conc_tuple) # result: (1, 2, 3, 4, 5, 6)

rep_tuple = tuple1 * 3

print(rep_tuple) # results: (1, 2, 3, 1, 2, 3, 1, 2, 3)

