fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break
    print(fruit)
# result:
"""
    apple
    banana
"""

for fruit in fruits:
    if fruit == "cherry":
        pass # placeholder, no action is need for cherry
    print(fruit)
# result:
"""
    apple
    banana
    cherry
    date
"""

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break # exits the loop when the count is reached

# results
"""
    0
    1
    2
"""