import matplotlib.pyplot as plt
Subjects = ["Maths","Science","Social","Tamil","English"] # X-axis
Marks = [83,76,77,92,80] # Y-axis
plt.bar(Subjects,Marks,color = "red")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Exam scores by subjects")
plt.grid()
plt.show()