# lists
friends = ["Kevin", "Karen", "Jim", "Oscar"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[1:3])  # excludes end point - in this case 4rd index

friends[1] = "Mike"  # update
print(friends)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# friends.extend(lucky_numbers)
# friends.append("Creed")
# friends.insert(1, "Kelly")
# friends.remove("Jim")
# friends.clear()
# friends.pop(1)
print(friends.index("Oscar"))
print(friends.count("Oscar"))

lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

# Tuple (immutable - cant be changed or modified)
# a type of data structure
# a container to store different values
# very similar to a list

coordinates = (4, 5)
print(coordinates[0])

# key differences between list and tuple
# tuple (immutable) cannot be changed or modified compared to list (mutable)
# Use tuple for data that will never be changed

# a list of tuples
coordinates1 = [(6,7), (4,5), (8,9)]
print(coordinates1)
# list can change but tuple within list cannot

# function
def say_hi(name, age):
    print("Hello " + name, " and i am " + str(age) + ".")

say_hi("Mike", 20)
