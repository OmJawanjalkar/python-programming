## CREATE THE DICTIONARY

my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)


## Accesing Values
print(my_dict["name"])
print(my_dict["city"])


## Adding and Updating Data

## Update existing key

my_dict["age"] = 31 # Update existing key
print(my_dict)

## Add new key-value pair

my_dict["mail"] = "Omjawanjalkar@gmail.com"
print(my_dict)

## Removing Key-Value Pairs
del my_dict["city"]


# 4. Dictionary Methods
#     keys()

#     values()

#     items()

#     get()

#     update()

#     pop()

#     clear()


## 5. Looping Through Dictionary

print("\nLooping through Dictionary:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")



## 6. Nested Dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

## 7. Dictionary Comprehension

squares = {x: x**2 for x in range(1, 6)}
print(squares)

Check_num ={X: "Even" if X % 2 ==0 else "Odd" for X in range(1, 11)}
print(Check_num)



# Checking if a key exists in the dictionary

if "name" in my_dict:
    print("Name exists in the dictionary.")
else:
    print("Name does not exist in the dictionary.")