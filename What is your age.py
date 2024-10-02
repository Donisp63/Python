# Prompting the user for their age
age = int(input("What is your age?\n"))

# Finding out if the user is old enough to drive
if age >= 16:
    print("\nYou are old enough to drive")
else:
    print(f"\nYou are not old enough to drive.\nMaybe you you can get your license in {str(16 - age)} years.")

# Finding out if the user can vote
if age >= 18:
    print("\nYou are old enough to vote")
else:
    print(f"\nYou are not old enough to vote.\nTry again in {str(18 - age)} years.")

# Finding out if the user can buy alcohol legally
if age >= 21:
    print("\nYou are old enough to buy alcohol")
else:
    print(f"\nYou are not old enough to buy alcohol.\nTry again in {str(21 - age)} years.")

# Finding out if the user is eligible for a senior discount.
if age >= 65:
    print("\nYou are eligible for a senior discount")
else:
    print(f"\nYou are not eligible for a senior discount.\nTry again in {str(65 - age)} years.")
