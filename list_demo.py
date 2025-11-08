List = ["Apple","Banana","Mango","Peach"]
print(List)
Numbers = [10,20,30,40,50]
print(Numbers)
# Mixed data types
Mixed = ["Car", 10, 2.5, True]
print(Mixed)
# Empty list
Empty_List = []
print("Length: ", len(Empty_List))
# Accessing elements from list - index
Food = ["Biryani","Fried Rice","Noodles","Momos"]
print("Food items: ", Food)
# Accessing first item
first_item = Food[0]
print("First item: ", first_item)
# Accessing second item
second_item = Food[1]
print("Second item: ", second_item)
# Accessing last item
last_item = Food[3]
print("Last item: ", last_item)
# Access last item using negative index
last_item_access = Food[-1]
print("Last item using negative index: ", last_item_access)
# Updating list items
Colours = ["Red","Black","White","Brown"]
Colours[1] = "Violet"
print(Colours)
Colours[-1] = "Orange"
print(Colours)
Colours[0] = "Grey"
print(Colours)
# Adding items to a list
# Create empty list
Languages = []
# Append method
Languages.append("Python")
Languages.append("Java")
Languages.append("C++")
print(Languages)
# Insert method
Languages.insert(2,"C")
print(Languages)
# Extend method
Languages.extend(["MS Office","HTML"])
print(Languages)
# Removing items from list
Countries = ["India","London","Japan","Canada","UK","USA"]
print(Countries)
# Remove by value
Countries.remove("Canada")
print(Countries)
# Remove by index - pop
Countries.pop(2)
print(Countries)
Countries.pop()
print(Countries)
# Clear the list
Countries.clear()
print(Countries)
Clothes = ["Jean","Shirt","Frock","Shawl"]
print(Clothes)
# for loop
for item in Clothes:
    print("I want to purchase " + item)
for i in range (len(Clothes)):
    print("Clothes at index" + str(i)+ ": ", Clothes[i])
# while loop
index = 0
while index < len(Clothes):
    print(Clothes[index])
    index += 1