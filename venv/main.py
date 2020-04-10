import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv(r'crime_rates.csv', encoding='utf-8').fillna(0)
# plt.plot(df.index['Year'], df.index['Burglary Rate'])
print(data.columns)
murder_data = data['Murder Rate'].iloc[0:1000].values
population_data = data['Population'].iloc[0:1000].values

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("First ten murder rates")

print(murder_data)
ax.plot(murder_data, c='r')

# plt.plot(year_data, murder_rate_data)
# # plt.plot(x, y)
plt.show()


