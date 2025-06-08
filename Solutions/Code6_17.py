print("HI! I'm a calculator program.")
while True:#infinite loop
    numbers = list(map(float,input("Give me the two numbers\n").split()))
    choice = input("if you wish to perform a sum digit sum, a difference digit dif, a product pro, a ratio rat\n")
    if choice == "sum":
        print("the sum of the values is ", sum(numbers))
    if choice == "dif":
        print("the difference of the values is ", numbers[0]-numbers[1])
    if choice == "pro":
        print("the product of the values is ", numbers[0]*numbers[1])
    if choice == "rat":
        print("the ratio of the values is ", numbers[0]/numbers[1])
    if input("if you wish another ride digit yes, if not digit whatever\n") != "yes":
        break
