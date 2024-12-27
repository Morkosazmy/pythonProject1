# Recursion

#iterative (for loop)
#def walk(steps):
#    for x in range(1, steps+1):
#        print(f"You took a step #{x}")
#walk(20)

#recusrive

def walk(steps):
    if steps <= 0:
        return
    walk(steps - 1)
    print(f"You took a step {steps} !")


walk(5)
"""
#FACTORIAL NUMBER
def factorial(n):
    if n <= 0:
        return fact
    fact = n * n-1
    factorial(n-1)

print(factorial(3))

"""
sum = 0
def factorial(n):
    if n == 1:
        return 1
    elif n < 0:
        print("Cant calculate factorial of a negative number !")
    elif n == 0:
        return 0
    else:
        x = n * (n-1)
        sum = x
        factorial(n-1)
    return sum
print(factorial(5))


# factorial function iteratively !
def factorial_iterative(n):
    factorial = 1
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        print("ERROR: cant have a negative value")
    else:
        while n > 1:
            factorial *= n
            n -= 1
            print(f"n = {n} and factorial = {factorial}")
            print()
        return factorial

print(factorial_iterative(5))

#Recursive way !
def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        print("ERROR: cant have a negative value")
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))



# 2nd attempt for recursive :

def recursive_factorial(x):
    if x == 0 or x == 1:
        return 1
    elif x < 0:
        print("Error ! (negative value entered)")
        return 0
    else:
        return x * recursive_factorial(x-1)

print(recursive_factorial(5))