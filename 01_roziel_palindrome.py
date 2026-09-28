number = int(input("Enter a number: "))

originalnumber = number
reversednumber = 0

while number > 0:
    digit = number %10
    reversednumber = reversednumber * 10 + digit
    number = number //10

if originalnumber == reversednumber:
    print(f"{originalnumber} is a palindrome.")
else:
    print(f"{originalnumber} is not a palindrome.")