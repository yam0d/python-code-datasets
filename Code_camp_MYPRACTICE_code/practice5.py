# for loop
for letter in "Giraffe Academy":
    print(letter)

friends = ["Kevin", "Karen", "Jim"]
for name in friends:
    print(name)

for index in range(len(friends)):  # range from 0 to n
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iter")
    elif index !=0 and index != 4:
        print("Not first")
    else:
        print("Last iter")
