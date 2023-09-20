import datetime
from numpy import sqrt
from numpy import arange, reshape
import pandas as pd


# get the current date and time
now = datetime.datetime.now()
print(now)

# do sqrt
print(sqrt(5))

# 1d array in numpy
a = arange(6)                    # 1d array
print(a)

# testing pandas dataframe
pd.DataFrame({'A': [1, 2, 3]})


