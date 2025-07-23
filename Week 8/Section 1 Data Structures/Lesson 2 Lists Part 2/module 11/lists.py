fruits = ["apple", "banana", "cherry"]

print(fruits[0])

fruits[1] = "blueberry" #modifies value in this index

print(fruits) # results: ['apple', 'blueberry', 'cherry']

fruits.append("kiwi")

print(fruits) # results: ['apple', 'blueberry', 'cherry', 'kiwi']

fruits.insert(1, "orange") # add at index 1

print(fruits) # results:['apple', 'orange', 'blueberry', 'cherry', 'kiwi']

fruits.remove("kiwi") # remove only the first one of there are duplicates

print(fruits) # results:['apple', 'orange', 'blueberry', 'cherry']

fruits.sort() # default sorting is ascending
print(fruits) # results: ['apple', 'blueberry', 'cherry', 'orange']

fruits.sort(reverse=True) # descending order
print(fruits) # results: ['orange', 'cherry', 'blueberry', 'apple']
