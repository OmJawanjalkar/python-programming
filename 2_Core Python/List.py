# =========================
# LIST OPERATIONS IN PYTHON
# =========================

# 1. Creating List
numbers = [10, 20, 30, 40, 50]

print("Original List:")
print(numbers)

# =========================
# 2. Accessing Elements
# =========================

print("\nFirst Element:")
print(numbers[0])

print("\nLast Element:")
print(numbers[-1])

# =========================
# 3. List Slicing
# =========================

print("\nSlicing [1:4]:")
print(numbers[1:4])

print("\nReverse List:")
print(numbers[::-1])

# =========================
# 4. Modifying Elements
# =========================

numbers[0] = 100

print("\nModified List:")
print(numbers)

# =========================
# 5. Append Method
# =========================

numbers.append(60)

print("\nAfter Append:")
print(numbers)

# =========================
# 6. Insert Method
# =========================

numbers.insert(1, 999)

print("\nAfter Insert:")
print(numbers)

# =========================
# 7. Extend Method
# =========================

numbers.extend([70, 80, 90])

print("\nAfter Extend:")
print(numbers)

# =========================
# 8. Remove Method
# =========================

numbers.remove(30)

print("\nAfter Remove:")
print(numbers)

# =========================
# 9. Pop Method
# =========================

numbers.pop()

print("\nAfter Pop:")
print(numbers)

# =========================
# 10. Pop with Index
# =========================

numbers.pop(1)

print("\nAfter Pop(1):")
print(numbers)

# =========================
# 11. Length of List
# =========================

print("\nLength:")
print(len(numbers))

# =========================
# 12. Searching Element
# =========================

print("\nChecking 50 in List:")
print(50 in numbers)

# =========================
# 13. Count Method
# =========================

data = [1, 2, 2, 2, 3]

print("\nCount of 2:")
print(data.count(2))

# =========================
# 14. Index Method
# =========================

print("\nIndex of 3:")
print(data.index(3))

# =========================
# 15. Sorting List
# =========================

values = [5, 1, 8, 2]

values.sort()

print("\nAscending Sort:")
print(values)

# =========================
# 16. Descending Sort
# =========================

values.sort(reverse=True)

print("\nDescending Sort:")
print(values)

# =========================
# 17. Reverse Method
# =========================

values.reverse()

print("\nReverse Method:")
print(values)

# =========================
# 18. Maximum and Minimum
# =========================

print("\nMaximum:")
print(max(numbers))

print("\nMinimum:")
print(min(numbers))

# =========================
# 19. Sum of List
# =========================

print("\nSum:")
print(sum(numbers))

# =========================
# 20. Loop Through List
# =========================

print("\nLooping List:")

for n in numbers:
    print(n)

# =========================
# 21. Nested List
# =========================

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("\nNested List:")
print(matrix)

print("\nAccess Nested Element:")
print(matrix[1][2])

# =========================
# 22. List Concatenation
# =========================

list1 = [1,2]
list2 = [3,4]

new_list = list1 + list2

print("\nConcatenated List:")
print(new_list)

# =========================
# 23. List Repetition
# =========================

print("\nRepeated List:")
print(list1 * 3)

# =========================
# 24. Copy List
# =========================

copied = numbers.copy()

print("\nCopied List:")
print(copied)

# =========================
# 25. Clear List
# =========================

temp = [1,2,3]

temp.clear()

print("\nAfter Clear:")
print(temp)

# =========================
# 26. List Comprehension
# =========================

squares = [x*x for x in range(1,6)]

print("\nSquares:")
print(squares)

# =========================
# 27. Even Numbers
# =========================

evens = [x for x in range(10) if x % 2 == 0]

print("\nEven Numbers:")
print(evens)

# =========================
# 28. Remove Duplicates
# =========================

duplicate = [1,2,2,3,4,4,5]

unique = []

for n in duplicate:

    if n not in unique:
        unique.append(n)

print("\nUnique List:")
print(unique)

# =========================
# 29. Largest Element
# =========================

largest = numbers[0]

for n in numbers:

    if n > largest:
        largest = n

print("\nLargest Element:")
print(largest)

# =========================
# 30. Delete List
# =========================

sample = [1,2,3]

del sample

print("\nList Deleted Successfully")