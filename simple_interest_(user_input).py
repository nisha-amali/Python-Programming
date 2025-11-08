p = int(input("Enter your principle amount: "))
n = int(input("Enter the number of years: "))
r = float(input("Enter the rate of interest: "))
SI = (p*n*r)/100
print("Interest amount:",SI)
Total = SI+p
print("Total amount:",Total)
Monthly = SI/12*n
print("Monthly amount:",Monthly)