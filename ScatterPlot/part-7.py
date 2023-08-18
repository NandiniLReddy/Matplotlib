import matplotlib.pyplot as plt
import pandas as pd
# basic plot

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
#          538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
# plt.scatter(x, y, c=colors, edgecolors='black', s=sizes, alpha=.75)
# cbar = plt.colorbar()
# cbar.set_label("Satisfaction")
# plt.title("X and Y values")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
plt.style.use("fivethirtyeight")
data = pd.read_csv("data:part7.csv")
likes = data['likes']
ratio = data['ratio']
ViewCount = data['view_count']
plt.scatter(ViewCount, likes, c=ratio, cmap="summer", edgecolors='black')
cbar = plt.colorbar()
cbar.set_label("Likes/Dislikes Ratio")
plt.title("YouTube Videos")
plt.xlabel("View Count")
plt.ylabel("Likes")
plt.xscale("log")
plt.yscale("log")
# plt.savefig("part-7.png")
plt.show()
