import matplotlib.pyplot as plt
import pandas as pd

# Basic Plot
# ages = [20, 33, 45, 76, 89, 24, 56, 12, 67, 100, 77, 44]
# plt.hist(ages, bins=5, edgecolor='black')
# plt.title("Histogram Plot")
# plt.show()

data = pd.read_csv("data:part6.csv")
ages = data['Age']
ids = data['Responder_id']
median_age = ages.mean()
# print(median_age)
bins = [20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, edgecolor='black', log=True)
plt.axvline(median_age, color="red", linewidth=2, label="Median Age")
# plt.text(median_age, 10, f'Median Age: {median_age:.1f}', color='red',
#          verticalalignment='bottom', horizontalalignment='right')
plt.title("Ages of Respondents")
plt.xlabel("Ages")
plt.ylabel("Total Responses")
plt.legend()
# plt.savefig("part-7.png")
plt.show()
