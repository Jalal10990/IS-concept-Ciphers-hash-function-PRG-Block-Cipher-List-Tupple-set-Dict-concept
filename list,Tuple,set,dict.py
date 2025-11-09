

# collection
# list - order, mutable
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print("List:", fruits)

# Tuple - ordered, immutable
coords = (10, 20)
# coords[0] = 5  would raise error
print("Tuple:", coords)

# Set- unordered, unique
nums ={1, 2, 3}
nums.add(2)  
# no duplicate added
nums.add(4)
print("Set: ", nums)


# Dict -key value mapping
student ={"name": "Ali", "id": 101, "grade": [85, 90]}
student["major"] = "CS"
print("DIct: ", student)

# useful patterns
# iterate dict
for k,v in student.items():
    print(k, "->" ,v)

    # list comprehensive: squares
squares = [x*x for x in range(6)]
print("Squares:", squares)

