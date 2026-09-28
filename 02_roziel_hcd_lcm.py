large = int(input("Enter a large number: "))
small = int(input("Enter a small number: "))

while (small):
    numberstore = small
    small = large % small
    large = numberstore

print(f"The HCF is: {large}.")