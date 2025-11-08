import matplotlib.pyplot as plt
Department = ["IT","Finance","HR"] # X-axis
Salary = [30000,75000,100000] # Y-axis
plt.bar(Department,Salary,color = ["red","yellow","green"],width = 0.5)
plt.xlabel("Department")
plt.ylabel("Salary")
plt.title("Average salaries by department")
plt.show()