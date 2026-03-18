from Calculate import math_functions

# user input for the number
num = int(input("Enter a number: "))

# calling the funtion to perfom operations
sqr_res, log_res, sin_res = math_functions(num)

print(f"Square of {num} is {sqr_res}") #sqrt is used to print  square root of a number
print(f"Logarithm of {num} is {log_res}") #log is to print garithm of a number   
print(f"Sine of {num} is {sin_res}") # sin is used to print sine of a number
