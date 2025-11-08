# Implicit type casting
x = 10  # int
y = 2.5  # float
sum = x+y  # 10+2.5 = 12.5
print(sum)
print("Type of sum:", type(sum))
# Explicit type casting
value = "100"
num = int(value)
print("Type of num:", type(num))
f = float(value)
print("Type of value:", type(f))
price = float(value)
price_str = str(price)
print("Type of price:", type(price))
print("Type of price_str:", type(price_str))