# Basic function
def greet():
    print("Welcome to Python Programming")
greet()
greet()
greet()
# Greeting with name
def greet_user(name):
    print(f"Hello",name)
greet_user("Nisha")
greet_user("Sania")
greet_user("Jairesh")
greet_user("Ajay")
# Square function
def square(num):
    return num*num
result = square(5)
print("Square: ", result)
print(square(10))
print(square(100))
# Maximum of two numbers
def max(a,b):
    if a > b:
        return a
    else:
        return b
max_value = max(a = 5, b = 10)
print("Maximum: ", max_value)
# Calling functions inside a loop
def greet_user(name):
    print("Hello, " + name + "!")
names = ["Amali","Danish","Hazel","Wang"]
for name in names:
    greet_user(name)
# Functions with default values
def greet_default(name = "Guest"):
    print("Hello,",name)
greet_default()
greet_default("Sansha")