# Q1. What is map()?

# map() applies a function to every element of an iterable.

# Example:

# from functools import reduce


# list(map(lambda x:x*x, [1,2,3]))

# Q2. What is filter()?
# filter() selects elements based on condition.
# Example:

# list(filter(lambda x:x%2==0, [1,2,3,4]))

# Q3. What is reduce()?
# reduce() reduces iterable into single value.
# Example:

# list(reduce(lambda a,b:a+b, [1,2,3]))



## Example of map, filter, reduce

list1 = [1, 2, 3, 4, 5]

# Using map to square each element

squared = list(map(lambda x: x**2, list1))
print("Squared:", squared)


l = [10, 15, 20, 25, 28, 30]

cube =list(map(lambda x: x**3, l))
print("cube:", cube)


# Cover into upper case
names = ["alice", "bob", "charlie", "jawanjalkar"]

upper_names = list(map(lambda x: x.upper(), names))
print("Upper Case Names:", upper_names)





## Using filter to select even numbers

even_numbers = list(filter(lambda x: x % 2 == 0, l))
print("Even Numbers:", even_numbers)



def num(n):
    return n > 15

greter = list(filter(num, l))
print("Greater than 15:", greter)


# Filter Positive Numbers

numbers = [-2,-1,0,1,2,3]

positive_numbers = list(filter(lambda x: x>0, numbers))
print("Positive Numbers:", positive_numbers)


## Using filter to select vowels from a string

text = "python programming"

vowels = list(filter(lambda x: x in "aeiou", text))

print(vowels)



## Use the reduce function

## Using reduce to calculate the sum of all numbers in a list

from functools import reduce


numbers_1 = [1, 2, 3, 4, 5]


sum_of_numbers =  reduce((lambda a,b : a + b ), numbers_1)
print("Sum of numbers:", sum_of_numbers)


## Using reduce to calculate the product of all numbers in a list

product_of_numbers =  reduce((lambda a,b : a*b ), numbers_1)
print("Product of numbers:", product_of_numbers)


# Find Maximum Using reduce()

numbers = [10,50,20,90,500,30]

max_number  = reduce(lambda a,b: a if a>b else b, numbers)
print("Maximum number:", max_number)



# Combined Program


from functools import reduce

num = [1,2,3,4,5]

# map()
square = list(map(lambda x:x*x, num))

# filter()
even = list(filter(lambda x:x%2==0, num))

# reduce()
total = reduce(lambda a,b:a+b, num)

print(square)
print(even)
print(total)