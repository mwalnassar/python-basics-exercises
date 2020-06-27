# 9.3 - Nesting, Copying, and Sorting Lists and Tuples
# Solutions to review exercises


# Exercise 1
# Create a tuple called data with two values, (1, 2) and (3, 4)
data = ((1, 2), (3, 4))


# Exercise 2
# Loop over data a print the sum of each nested tuple
for i in range(len(data)):
    print(f"Row {i+1} sum: {data[i][0] + data[i][1]}")

# also the above exercise can written in the below way
for row in data:
    x, y = row
    print(f"Row {int(data.index(row)) + 1} sum {x + y}")

# Exercise 3
# Create the list [4, 3, 2, 1] and assign it to variable numbers
numbers = [4, 3, 2, 1]


# Exercise 4
# Create a copy of the number list using [:]
numbers_copy = numbers[:]


# Exercise 5
# Sort the numbers list in numerical order
numbers.sort()
print(numbers)
