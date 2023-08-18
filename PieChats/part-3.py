import pandas as pd
from matplotlib import pyplot as plt
# basic-one
# slices = [60, 40]
# labels = ["Sixty", "Fourty"]
# colors = ['#008fd5', '#fc4f30']
# explode = [0, 0.1]
# plt.pie(slices, labels=labels, wedgeprops={
#         'edgecolor': 'black'}, colors=colors, explode=explode)
# plt.title("Pie Chart")
# plt.tight_layout()
# # plt.savefig("part-3(basic).png")
# plt.show()


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f', 'red']
explode = [0, 0, 0, 0, 0.1]
plt.pie(slices, labels=labels, colors=colors, wedgeprops={
        'edgecolor': 'black'}, explode=explode, shadow=True, startangle=45, autopct="%1.1f%%")
# plt.savefig("part-3.png")
plt.show()
