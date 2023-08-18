import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv("data:part2.csv")
Total_languages = data.LanguagesWorkedWith
ids = data.Responder_id

language_counter = Counter()
for items in Total_languages:
    language_counter.update(items.split(';'))
# print(language_counter)
languages = []
popularity = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
# print(languages, popularity)
languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)

plt.title("Most Polular Languages Used")
plt.ylabel("Programming Languages")
plt.xlabel("No of people using")
# plt.savefig("part-2(2).png")
plt.show()
