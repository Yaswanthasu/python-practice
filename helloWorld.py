print("Hello World")
a = "hi"
print(a)
print("Hello\n \"World\"",7,0,9 ,sep="-")
(str) = "hello"
print(str,end=" dhobbey\n")
array = ["hello","hi","tata","bye"]
print(array)
print(array[0])
print(array[1])
print(array[2])
print(array[3])
array.append(4)
array.remove("tata")
print(array)
num = float(input("Enter a number : "))
print(num)
# Create a dictionary
student = {
    "name": "John",
    "age": 25,
    "courses": ["Math", "CompSci"]
}

# Print the dictionary
print("Student:", student)

# Access elements
print("Name:", student["name"])

# Add a new key-value pair
student["grade"] = "A"
print("After adding a grade:", student)

# Remove a key-value pair
del student["age"]
print("After removing age:", student)
