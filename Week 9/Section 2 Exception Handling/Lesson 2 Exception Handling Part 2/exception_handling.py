try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
else:
    print("Everything went fine") # This runs only if no exceptions occur in try
finally: #will be executed regardless of error
    print("The 'try except' is finished")
    
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")