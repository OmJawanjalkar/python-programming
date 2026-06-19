# f = open("test.txt", "r")
# content = f.read()
# print(content)


# f = open("test.txt", "r")

# line1 = f.readlines()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()



## perform the write operation


f = open("sample.txt", "w")
written_content = "This is a new line, \nthis will overwrite the existing content."
f.write(written_content)


# file = open("test.txt", "a")
# new_line = "\n This is a new line, \nthis will be added to the existing content."
# om =file.write(new_line)
# print(om)



## Real-World Programs


# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)


# with open("test.txt", "w") as f:
#     f.write("This is a new courese on file handling in python.")


# ## Delete a file
# import os

# os.remove("sample.txt")



## Practice Programs

# with open("practice.txt", "w") as f:
#     f.write("This is a java course, \nthis this will beneficial for java developers.")


# with open("practice.txt", "r") as f:
#     data = f.read()

#     replace = data.replace("java", "python")
#     print(replace)

# with open("practice.txt", "w") as f:
#   f.write(replace)

def Check_word():
      word = "benificial"
      with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
          print("Found")
        else:
          print("Not Found")



count = 0
with open("practice.txt", "r") as f:
  data = f.read()

  numbers = data.split(",")
  print(numbers)
  for val in numbers:
     if int(val) % 2 == 0 :
       count += 1

print(count)