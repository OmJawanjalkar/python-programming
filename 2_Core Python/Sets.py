# Set Creation
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A =", A)
print("B =", B)

# Add Element
A.add(10)

print("\nAfter Add")
print(A)

# Update Set
A.update([20, 30])

print("\nAfter Update")
print(A)

# Remove Element
A.remove(2)

print("\nAfter Remove")
print(A)

# Discard Element
A.discard(100)

print("\nAfter Discard")
print(A)

# Pop Element
A.pop()

print("\nAfter Pop")
print(A)

# Length
print("\nLength")
print(len(A))

# Membership Operator
print("\nCheck Element")
print(4 in A)

# Union
print("\nUnion")
print(A | B)

# Intersection
print("\nIntersection")
print(A & B)

# Difference
print("\nDifference")
print(A - B)

# Symmetric Difference
print("\nSymmetric Difference")
print(A ^ B)

# Loop Through Set
print("\nLoop")

for x in A:
    print(x)

# Copy Set
C = A.copy()

print("\nCopied Set")
print(C)

# Subset
X = {1, 2}
Y = {1, 2, 3, 4}

print("\nSubset")
print(X.issubset(Y))

# Superset
print("\nSuperset")
print(Y.issuperset(X))

# Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = set(numbers)

print("\nUnique Values")
print(unique)

# Convert Set to List
data = list(unique)

print("\nConverted List")
print(data)

# Frozen Set
f = frozenset([1, 2, 3])

print("\nFrozen Set")
print(f)

# Clear Set
B.clear()

print("\nAfter Clear")
print(B)