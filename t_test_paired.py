import pandas as pd
from statsmodels.stats.weightstats import ztest
import math
import scipy


data_dict = [{'Pop': 18 , 'Mean': 81, 'Sample Std Dev': 10},
            {'Pop': 18 , 'Mean': 75, 'Sample Std Dev': 10}]

df = pd.DataFrame(data_dict, index = ['A','B'])

df

#calculate test statistic t
#difference in means is 0

dif_mean = 0

t_stat = ((df.at['A', 'Mean'] - df.at['B', 'Mean']) - dif_mean) \
        / (((df.at['A', 'Sample Std Dev']) / math.sqrt(df.at['A', 'Pop']))) 

print('T-Stat is', t_stat)

#degrees of freedom

deg_free = df.at['A' , 'Pop'] - 1

#df['Pop'].sum() - len(df.index)

print('Degrees of Freedom', deg_free)

#p-stat

p_stat = 2 * (1 - scipy.stats.t.cdf(abs(t_stat), deg_free))

print('P-Stat is', p_stat)