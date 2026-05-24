# if   Executes code if condition is True

# a = int(input("Enter a age: "))

# if a >= 18:
#    print("You are elgible to vote")


#  if-else  Executes code if condition is True and another code if condition is False

# if a >= 18:
#    print("You are elgible to vote")
# else:
#    print("You are not eligible for the vote")


# check number is even or odd

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#  Check the Number is positive, negative

# num = int(input("Enter a number:"))

# if num >0:
#     print("Positive")
# else:
#   print("Negative")



#  if-elif-else Execute  code if condition is True and another code if condition is False and another code if condition is not True and not False

# mark = int(input("Enter a mark:"))

# if mark >= 90:
#   print("Grade A")
# elif mark >= 80:
#   print("Grade B")
# elif mark < 35:
#   print("Fail")
# else:
#   print("Grade C")


#  Print the  Largest of three numbers

# a = 55
# b = 20
# c = 100

# if a > b and a > c:
#     print(" A is largest")
# elif b > a and b > c:
#     print("B is Largest")
# else:
#     print("C is Largest")



#  Nested if-else

# age = 19
# license = False

# if age >= 18:
#   print("You are elgible for the license")
#   if license:
#     print("You can drive")
#   else:
#     print("You are not allowed to drive")
# else:
#     print("You are not elgible for the license")






#  one line if statement

num = 28

# print("The number is even") if num % 2 == 0 else print("The number is  odd")



# day = "Sunday"

# if day == "Monday" or day == "Thursday":
#   print(" thes day are not weekend")

# elif day == "Saturday" or day == "Sunday":
#   print("These day are weekend")

# else:
#   print("These day are not weekend")


#  Simple Login System

username = input("Enter your username:")
password = input("Enter your password:")

if username == "omjawanjalkar@gmail.com" and password == "Pass@123":
  print("Login Successful")
else:
  print("Invalid username or password")