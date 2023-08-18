import matplotlib.pyplot as plt
import pandas as pd
# plt.xkcd()
data = pd.read_csv("data:part5.csv")
# print(data)
ages = data['Age']
All_dev = data['All_Devs']
Python_dev = data['Python']
JavaScript_dev = data['JavaScript']
median_value = int(Python_dev.mean())

# print(median_value)
plt.plot(ages, All_dev, label="All Developers")
plt.plot(ages, Python_dev, label="Python Developers")

# plt.fill_between(ages, Python_dev, median_value, alpha=0.3)


plt.fill_between(ages, Python_dev, median_value, where=(
    Python_dev > median_value),  alpha=0.3, label="Above Median", interpolate=True)

plt.fill_between(ages, Python_dev, median_value, where=(
    Python_dev < median_value), color='red', alpha=0.3, label="Below Median", interpolate=True)
plt.title("Developers Salary by Age - Fill Between (python_Dev)")
plt.legend()
plt.xlabel("Age")
plt.ylabel("Salary")
# plt.savefig("part-5.png")
plt.show()
