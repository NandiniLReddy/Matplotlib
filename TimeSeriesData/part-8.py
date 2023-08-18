import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# basic plot

# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7]
# plt.plot(dates, y, marker='o')
# plt.xticks(rotation=45)
# plt.show()

data = pd.read_csv("data:part8.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)
dates = data['Date']
close_price = data['Close']
plt.plot_date(dates, close_price, marker='o', linestyle='solid')
plt.gcf().autofmt_xdate()
plt.title("Bitcoin Price")
plt.xlabel("Date")
plt.ylabel("Closing Price")
# plt.xticks(rotation=45)
plt.tight_layout()
# plt.savefig("part-8.png")
plt.show()
