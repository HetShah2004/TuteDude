# lamda function to calculate the factorial of a number using recursion

factorial_lambda = lambda n: 1 if n == 0 or n == 1 else n * factorial_lambda(n - 1)


# user input for the number
num = int(input("Enter a number: "))

# storing the result of the factorial function in a variable
result = factorial_lambda(num)

# printing the result
print(f"The factorial of {num} is {result}")    