# array = [15, 25, 20, 40, 70]

# print("Given Array is:", array)

# print("First Element is", array[0])
array = []
Re=int(input("Enter Your Range:"))

for i in range (Re):
    value = input(f"Enter {i+1} element")
    array.append(value)

print("Final array is",array)
