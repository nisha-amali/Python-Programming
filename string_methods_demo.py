Text = " Black Magic lady"
Text1 = "Am I a joke to you? No, you are not."
Text2 = "Python"
Num = "2007"
Num1 = "year2007"
Num2 = "year 2007"
words = ["Green","apples","are","attractive","."]
# Lower method
print("Lower case:",Text.lower())
# Upper method
print("Upper case:",Text.upper())
# strip() method
print("After strip: ",Text.strip())
# replace() method
print("After replace: ",Text.replace("Magic","Heart"))
# split() method
print("Split result: ",Text.split())
# Find() method
print("Found at index: ",Text1.find("joke"))
# title() method
print("Title case:",Text.title())
# capitalize() method
print("Capitalize result: ",Text.capitalize())
# endswith() method
print(Text.endswith("Black"))
print(Text.endswith("Magic"))
# count() method
print("Total count: ",Text1.count("you"))
# isalpha() method
print(Text.isalpha())
print(Text2.isalpha())
# isdigit() method
print(Num.isdigit())
print(Num1.isdigit())
# isalnum() method
print(Num1.isalnum())
print(Num2.isalnum())
# join() method
print(" ".join(words))