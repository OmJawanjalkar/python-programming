# Creating the striing using single quotes and double quotes
# course = 'Python'
# Name = "Om"
# city = "Amarvti"

# print("Name:", Name, "City:", city)


# Using triple quotes to create a string

Introduction = """
# Hiii I am Om Jawanjalkar........."""
# print(Introduction)

# Identifying the type of the variable
# print(type(city))


# Concanating the Strings

# print(Name +" " + city)


# Example of string



Name = "Ramkrushna"




# indexing the string

name = "Ramkrushna"

# print(name[5])
# print(name[-3])

# slicing the string
# print(name[1:5])
# print(name[ :5])
# print(name[2: ])
# print(name[2 : -4])


# Revrse a string
# print(name[ : : -1])

# Replace

# print(name.replace("a","@"))

# count
# print(name.count("a"))


# Write the program check the given string is palindrome or not

# Name = input("Enter the string: ")

# if Name == Name[:: -1]:
#     print("The string is palindrome")
# else:
#   print("The string is not palindrome")


# reverse the string using loop

# text = "python"
# reversed = ""Om

# for i in text:
#     reversed = i + reversed

# print(reversed)


# Count Vowels Program
text = input("Enter the string: ")
Count =0

for i in text.lower():
   if i in "aeiou":
       Count += 1
print("The number of vowels in the string is: ", Count)
