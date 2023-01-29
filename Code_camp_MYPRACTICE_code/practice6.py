# exponent function
print(2**3)

def raised_to_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

# print(raised_to_power(2,3))

# 2d lists and nested loops
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)

# build a translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(translate("cat"))
