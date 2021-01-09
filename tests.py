from maguro import Maguro


## Example #1
print("\nTest #1")
person = Maguro("tests.csv")

# clear
person.clear()

# add items
person.append("Juan")
person.append("Male")
person.append("23")

# show
print(person.pack())

# raw list
print(person.unpack())

# loop over items
for item in person.items():
    print(item)

# remove item
person.remove("23")
person.append("24")
print(person.pack())

# insert item
person.insert(1, "Dela Cruz")
print(person.pack())
