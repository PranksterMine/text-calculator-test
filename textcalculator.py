print("Welcome to the calculator!")

#first value
print("Input first value:")
val1 = int(input())

#second value
print("Input second value:")
val2 = int(input())

#operation
print("Select operation type:")
print("Valid operations: Addition, Subtraction, Multiplication, Division, Floor Division, Exponentation, and Comparison")
operation = input()

#perform operations
if operation == "Addition":
    answer = val1 + val2
    print(answer)

elif operation == "Subtraction":
    answer = val1 - val2
    print(answer)

elif operation == "Multiplication":
    answer = val1 * val2
    print(answer)

elif operation == "Division":
    answer = val1 / val2
    print(answer)

elif operation == "Floor Division":
    answer = val1 // val2
    print(answer)

elif operation == "Exponentation":
    answer = val1 ** val2
    print(answer)

elif operation == "Comparison":
    #check for equality
    equality = val1 == val2

    if equality == True:
        print("The values are equal.")

    else:
        print("The values are not equal.")

    #check if the first value is greater than the second
    greaterthan = val1 > val2

    if greaterthan == True:
        print("The first value is the greater value.")
    
    else:
        print("The first value is the smaller value.")