
#message = 'Anda's World' #won't work, rather below:
message = "Anda's World"
message = """ Anda's world
    is cool
""" # """ for multiple lines

print(message) 

message = 'Hello'

print(message[0]) # result: H
print(message[1]) # results: e
print(message[-1]) # results: o
print(len(message)) # results: 5

message = ' Hello '

print(len(message)) # results: 7

message = ' Hello world! '

print(message.strip()) # removes leading and trailing whitespace # result: 'Hello world!'

print(message.lower()) # to lower case # result: 'hello world!'

message = ' Hello, world! '

print(message.split(',')) # split the string into a list based on the comma # results: [' Hello', ' world! ']

# to do: 
# upper method
# replace method