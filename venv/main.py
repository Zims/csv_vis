import pandas as pd
from matplotlib import pyplot as plt


sample_data = pd.read_csv(r'2014_apple_stock.csv')
sample_data.head()
plt.plot(sample_data.AAPL_x, sample_data.AAPL_y)
plt.show()
