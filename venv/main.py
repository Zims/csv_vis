import pandas as pd
from matplotlib import pyplot as plt


sample_data = pd.read_csv(r'2014_apple_stock.csv')
data = pd.read_csv(r'countries.csv')
cr_data = pd.read_csv(r'crime_rates.csv')
print(cr_data.columns)
# plt.plot(sample_data.AAPL_x, sample_data.AAPL_y)
# plt.show()

# us = data[data.country == 'United States']
# china = data[data.country == 'China']

alaska = cr_data[cr_data.State == 'Alaska']
minn = cr_data[cr_data.State == 'Minnesota']

plt.plot(alaska.Year, alaska.Murder_Rate)
plt.plot(minn.Year, minn.Murder_Rate)

plt.legend(['Alaska', 'Minnesota'])
plt.xlabel('Year')
plt.ylabel('Murder rate')

plt.show()



# plt.plot(us.year, us.population/ 10**6)
# plt.plot(china.year, china.population/ 10**6)
# plt.legend(['US', 'China'])
# plt.xlabel('Year')
# plt.ylabel('Population(millions)')

# Percentage growth
# us.population / us.population.iloc[0] * 100  #we get first year as 100% and so on
# plt.plot(us.year, us.population / us.population.iloc[0] * 100)
# plt.plot(china.year, china.population / china.population.iloc[0] * 100)
# plt.legend(['US', 'China'])
# plt.xlabel('Year')
# plt.ylabel('Population(growth in %)')
# plt.show()