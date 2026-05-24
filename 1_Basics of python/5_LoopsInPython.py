#  Loops in Python
# 1. While Loop

# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# count = 5
# while count >= 1:
#     print(count)
#     count -= 1


#  Print numbers from 1 to 100 using while loop

# count = 1
# while count <= 100:
#   print(count)
#   count += 1


# print number 100 to 1 using while loop

# count = 100
# while count >= 1:
#   print(count)
#   count -= 1

# n= int(input("Enter a number: "))
# i = 1
# while i <= 10:
#   print(n*i)
#   i += 1


# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# i = 0

# while i <= len(numbers)-1:
#   print(numbers[i])
#   i += 1

# numbers = (10, 20, 30, 40, 50, 60, 70, 80, 50, 100)
# i = 0
# x = 50
# while i < len(numbers):
#   if x == numbers[i]:
#     print("found")
#     break
#   else:
#     print("not found")
#   i += 1


#  For loop in Python

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for ch in range(len(list)):
#     print(ch)


# name = "Om Jawanjalkr"

# for char in name:
#     print(char)


# num = (4, 9, 16, 25, 36, 49, 64, 81, 100, 16)
# x= 16
# index=0
# for n in num:
#    if x== n:
#      print("found at index", index)
#      break
#    index += 1



# for i in range(1, 101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)



#  Calculate the factorial of a number using for loop

# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("Factorial =", fact)


#  Prime number check using for loop

# num = int(input("Enter a number: "))
# is_prime = True

# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# Fibonacci Series

n = 55
a = 0
b= 1

for i in range(n):
    print(a)
    c = a+b
    a = b
    b = c