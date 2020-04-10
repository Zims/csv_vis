import pandas as pd
from matplotlib import pyplot as plt

a = [1, 2, 3]
b = [7, 8, 9]
data = pd.read_csv(r'/Users/zims/PycharmProjects/csv_vis/venv/crime_rates.csv')
# plt.plot(df.index['Year'], df.index['Burglary Rate'])
print(data.columns)
x = pd.DataFrame(data, columns= ['Year'])
y = pd.DataFrame(data, columns= ['Murder Rate'])

# print(x, y)
plt.plot(x, y)
plt.show()
