import matplotlib.pyplot as plt
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation
import random

# basic plot:
# x_vals = []
# y_vals = []
# index = count()


# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 10))

#     plt.cla()
#     plt.plot(x_vals, y_vals)


# animation = FuncAnimation(plt.gcf(), animate, interval=1000)
# plt.tight_layout()
# plt.show()


def animate(i):
    data = pd.read_csv("data:part-9.csv")
    x_values = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    plt.plot(x_values, y1, label="plot-1")
    plt.plot(x_values, y2, label="plot-2")
    plt.legend()


animation = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
