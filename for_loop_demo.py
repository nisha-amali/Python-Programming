# Fruits
Fruits = ["apple", "banana", "cherry"]
for fruit in Fruits:
    print(fruit)
# Numbers
for number in range(1,6):
    print(number)
# Letters
Text = "Favourite"
for letter in Text:
    print(letter)
# Break statement in for loop
Fruits = ["apple", "banana", "cherry"]
for fruit in Fruits:
    if fruit == "banana":
        break
    print(fruit)
# Continue statement in for loop
for fruit in Fruits:
    if fruit == "apple":
        continue
    print(fruit)