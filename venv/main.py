import pandas as pd
from matplotlib import pyplot as plt
import operator
from numpy.ma.core import sort

data = pd.read_csv('crime_rates.csv')

# data.State
# print(data['State'])


# alaska = data[data.State == 'Alaska']
# wyoming = data[data.State == 'Wyoming']
# florida = data[data.State == 'Florida']

# plt.plot(alaska.Year, alaska.Murder_Rate)
# plt.plot(wyoming.Year, wyoming.Murder_Rate)
# plt.plot(florida.Year, florida.Murder_Rate)


# plt.title('Murder rate')
# plt.legend(['Alaska', 'Wyoming', 'Florida'])
# plt.ylabel('Murder rate')
# plt.xlabel('Year')
# plt.show()


def most_murderous(chosen_year):
    chosen_year_data = data[data.Year == chosen_year]
    # returns top5 rows based on Murder rate
    top5 = chosen_year_data.nlargest(5, ['Murder_Rate'])
    print(top5)

    # sorte_mr = [chosen_year_data.State, sort(chosen_year_data['Murder_Rate'])]
    # print(sorte_mr)
    
    
    
    # data_for_year = murder_rates.where("Year", chosen_year) 
    # sorted_data = data_for_year.sort("Murder Rate", descending = True) 
    # top_5 = sorted_data.take(np.arange(5)).sort("Murder Rate") 
    # top_5.barh('State', 'Murder Rate') 
    # return top_5.column('State')


    # REQUIRED
    #           # Implement the function “most murderous”, which takes a year (an integer) as its argument.
    #           # It does two things:
    #           # 1.It 
    # .
    #           # 2.It returns an array of the names of these states in order of increasing murder rate.


most_murderous(1960)



