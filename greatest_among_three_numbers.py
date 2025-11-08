# Using Nested If Statement
A = 1
B = 2
C = 3
if A > B:
    if A > C:
        print("A is greater.")
    else:
        print("C is greater.")
else:
    if B > C:
        print("B is greater.")
    else:
        print("C is greater.")