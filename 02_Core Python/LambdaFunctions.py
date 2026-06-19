# Lambda Functions in Python

# A lambda function is a small anonymous function.

# Anonymous means:

# Function without name

## Normal Function
def square(x):
    return x**x

print(square(2))

## Lambda Function

square_lambda = lambda x: x**x
print(square_lambda(2))

## Multiple Arguments
add = lambda x,y : x + y
print("Addition:", add(5, 3))





## Syntax

# lambda arguments : expression

## Cube of a number

cube = lambda x: x**3
print("Cube:", cube(3))


## Even or odd

even_odd = lambda X: "Even" if X % 2 == 0 else "Odd"
print("Even or Odd:", even_odd(9))
