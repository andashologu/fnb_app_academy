try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An exception occurred")
finally: #will be executed regardless of error
    print("The 'try except' is finished")