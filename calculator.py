num_1 = float(input("First Number "))
num_2 = float(input("Second Number "))
operator = input("Select Operator \nAdd  + \nSubstract  - \nDivide  / \nMultiply  * \nPower  ** \nRemainder  % \nSelect Operator ")

if(operator == "+"):
    print(num_1 + num_2)

elif(operator == "-"):
    print(num_1 - num_2)

elif(operator == "/"):
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("Cannot Divide by 0")

elif(operator == "*"):
    print(num_1 * num_2)

elif(operator == "**"):
    print(num_1 ** num_2)

elif(operator == "%"):
    print(num_1 % num_2)

else:
    print("Invalid Input")