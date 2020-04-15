import pandas as pd
from matplotlib import pyplot as plt
import operator

cr_data = pd.read_csv(r'crime_rates.csv')
print(cr_data.columns)


def most_murderous(chosen_year):
    chosen_year_data = cr_data[cr_data.Year == chosen_year]



    # REQUIRED
    #           # Implement the function “most murderous”, which takes a year (an integer) as its argument.
    #           # It does two things:
    #           # 1.It draws a horizontal bar chart of the 5 states that had the highest murder rate in that year.
    #           # 2.It returns an array of the names of these states in order of increasing murder rate.


most_murderous(1999)



