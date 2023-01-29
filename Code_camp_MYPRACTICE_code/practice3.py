# return statement
def cube(num):
    return num*num*num

print(cube(4))

result = cube(4)
print(result)

# if statements
is_male = True

if is_male:
    print("You are a male.")

is_male = False
is_tall = True

if is_male or is_tall:     # one or both is True
    print("You are a male or tall or both.")
else:
    print("You are a female or short or both.")

if is_male and is_tall:     # both is True
    print("You are a male and tall.")
elif is_male and not(is_tall):
    print("Your are a male but not tall.")
else:
    print("You are a female or short or both.")

# if statements and comparisons
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

print(max_num(1,2,3))

# or
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(10,5,3))

# building a better calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator.")

# dictionaries
monthConversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
}
print(monthConversion["Jan"])
print(monthConversion.get("Jan"))
print(monthConversion.get("Nov", "Not a valid key."))

monthConversion = {
    0:"January",
    1:"February",
    5:"March",
}
print(monthConversion[0])
print(monthConversion.get(5))
print(monthConversion.get(3, "Not a valid key."))
