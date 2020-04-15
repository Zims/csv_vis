# sample_data = pd.read_csv(r'2014_apple_stock.csv')
# data = pd.read_csv(r'countries.csv')
# us = data[data.country == 'United States']
# china = data[data.country == 'China']

# plt.plot(sample_data.AAPL_x, sample_data.AAPL_y)
# plt.show()

# florida = cr_data[cr_data.State == 'Florida']
# cali = cr_data[cr_data.State == 'California']
# plt.plot(florida.Year, florida.Population/10**6)
# plt.plot(cali.Year, cali.Population/10**6)
#
# plt.legend(['Florida', 'California'])
# plt.xlabel('Year')
# plt.ylabel('Population (millions)')
#
# plt.show()

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