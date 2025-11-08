import matplotlib.pyplot as plt
days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
visit = [100,50,7,500,350,750,2000]
plt.plot(days,visit)
plt.title("Website traffic over a week")
plt.xlabel("Days of the week")
plt.ylabel("number of Visitors")
plt.show()