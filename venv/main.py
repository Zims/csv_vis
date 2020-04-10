import pandas as pd
import plotly.express as px

data = pd.read_csv(r'2014_apple_stock.csv')
data.head()
print(data.columns)


fig = px.line(data, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
fig.show()



# murder_data = data['Murder Rate'].iloc[0:1000].values
# year_data = data['Year'].iloc[0:1000].values
# population_data = data['Population'].iloc[0:1000].values
# print(murder_data)
# print(population_data)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title("First ten murder rates")
# 
# ax.plot(year_data,murder_data, c='r')

# plt.plot(year_data, murder_rate_data)
# plt.show()


