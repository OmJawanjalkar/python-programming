Name = ("Om", "Pratik", "Satyarth", "Anshul")
print(Name)


## Accessing the  tuple elements
print(Name[0])
print(Name[1]) # output: Pratik
print(Name[-1]) # output: Anshul


# Tuple slicing
print(Name[1:3])

# Tuples are immutable, so we cannot modify them directly

print(Name[ : :-1])  # Reverse the tuple

# Tuples can contain different data types

MixedTuple = ("Hello", 42, 3.14, True)
print(MixedTuple)


## Tuple concatenation
tuple1 =(1, 2, 3)
tuple2 =(4, 5, 6)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)


# Length of the tuple
print(len(Name))

## Repetition of tuples
print(tuple1 * 9)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)


#  Mebership operators

print( 2 in tuple1)  # Output: True
print("om" in Name)  # Output: False (case-sensitive)
print("Om" in Name)  # Output: True



## Counting occurrences of an element in a tuple

data = (1,2,2,2)
print(data.count(2))  # Output: 3
print(data.count(5))


# index() Method

print(Name.index("Pratik"))
print(tuple1.index(2))


## neste Tuples

data = ((1,2), (3,4))

print(data[1][0])


## Tuple Packing and Unpacking

# Packing
person = ("Alice", 30, "Engineer")


# Unpacking
name, age, profession = person
print(name) #Output: Alice
print(age) # Output: 30


## Coversion of List to Tuple

my_list = [1,2,3,4]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4)

## Conversion of Tuple to List

my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print(my_list) ## Output: [1, 2, 3, 4]


## Modify a tuple by converting it to a list, making changes, and converting it back to a tuple

numbers = (10,20,30)

temp = list(numbers)

temp[0] = 100

numbers = tuple(temp)

print(numbers)


## finding the maximum and minimum values in a tuple

values = (5, 2, 9, 1)
print(max(values)) # Output: 9
print(min(values)) # Output: 1
print(sum(values)) # Output: 17



## Looping through a tuple

print("\nLooping through Tuple:")
for v in values:
    print(v)


## Deleting a tuple

college = ("MIT", "Stanford", "Harvard")

del college