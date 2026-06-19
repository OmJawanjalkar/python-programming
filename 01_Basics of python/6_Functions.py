



def my_function():
    print("Hello from the function!")


# my_function()



def Om_Info():
    print("My name is Om")
    print("I am 22 years old")
    print("I am a Data Scientist")


# Om_Info()
# my_function()



def add(a, b):
    print(a + b)

# add(5, 10)

# Positional Arguments

def Info(name, age):
    print("My name is : " + str(name))
    print("My age is :" + str(age))

# Info("Aditi", 20)
# Info("Payal", "22")

#  Keyword Arguments

def Info(name, age):
  print(name, age)


# Info(age=22, name="Aditi")

# Default Arguments

def City(name="Hyderabad"):
    print("I am form " + name)

# City()
# City("Bangalore")
# City("Amaravti")


#  Variable length Arguments
def my_function(*args):
    return sum(args)


# result = my_function(10, 20, 30, 40)
# print(result)


def demo(*args, **kwargs):
    print("Positional Aruments: ", args)
    print("Keywords Arguments:", kwargs)


# result = demo(10, 20, 30, name="Ramkrushna", age=56)
# print(result)

#  *args is used to pass a variable number of non-keyword arguments to a function, while **kwargs is used to pass a variable number of keyword arguments to a function. Both *args and **kwargs allow you to handle an arbitrary number of arguments in your functions, making them more flexible and adaptable to different use cases.


# Adding unlimited numbers: in  *args
# 1,2,3,4,5


# Form details:  **kwargs
# name="Om"
# age=21
# city="Nagpur"



## Recursion in Python

def show(n):
   if (n == 0):
      return
   print(n)
   show(n-1)


show(5)

