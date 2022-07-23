import pandas as pd
from statsmodels.stats.weightstats import ztest
import math
import scipy

#A transportation commission studies driving times
#Times for 40 cars driving on old highway
#times for 50 cars driving on new highway
#data from study is below

data_dict = [{'Pop': 8, 'Mean': 163, 'Pop Std Dev': 5},
            {'Pop': 8, 'Mean': 159, 'Pop Std Dev': 4}]

df = pd.DataFrame(data_dict, index = ['A','B'])

df

#Standard Error

standard_error = math.sqrt(((df.at['A','Pop Std Dev'] ** 2) / (df.at['A','Pop'])) +
((df.at['B','Pop Std Dev']**2) / (df.at['B','Pop'])))

print('Standard Error is', standard_error)

#z-score

z_stat = (df.at['A', 'Mean'] - df.at['B', 'Mean']) / standard_error

print('Z-Stat is', float(z_stat))

#p-value
p_val = scipy.stats.norm.sf(abs(z_stat))
print('P-Value is', p_val)