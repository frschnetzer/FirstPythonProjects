def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num -1)

print("The factorial of 100 is:")
print(factorial(3))
