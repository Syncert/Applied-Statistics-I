import pandas as pd
import math
import scipy



data_dict = [{'Pop': 12 , 'Mean': 129, 'Sample Std Dev': 1},
            {'Pop': 12 , 'Mean': 124, 'Sample Std Dev': 5}]

df = pd.DataFrame(data_dict, index = ['A','B'])

df

#calculate test statistic t

t_stat = (df.at['A', 'Mean'] - df.at['B', 'Mean']) \
        / math.sqrt( ((df.at['A', 'Sample Std Dev'] ** 2) / df.at['A', 'Pop']) + ((df.at['B', 'Sample Std Dev'] ** 2) / df.at['B', 'Pop']) )

print('T-Stat is', t_stat)

#degrees of freedom

deg_free = df['Pop'].sum() - len(df.index)

print('Degrees of Freedom', deg_free)

#p-stat

p_stat = 2 * (1 - scipy.stats.t.cdf(abs(t_stat), deg_free))

print('P-Stat is', p_stat)